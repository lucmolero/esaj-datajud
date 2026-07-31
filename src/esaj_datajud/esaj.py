"""eSAJ extraction helpers organized into small functions.

This module focuses on clean separation of responsibilities:
- URL construction: `montar_url_busca`
- HTTP loading: `carregar_pagina`
- Parsing primitives: `extrair_dados_basicos`, `extrair_partes`, `extrair_movimentacoes`
- Orchestration: `montar_extrato`

The implementation is a compact, maintainable rework inspired by the reference
scripts; it is suitable to be extended and unit-tested against saved HTML fixtures.
"""
from __future__ import annotations

import re
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode, urljoin, urlparse, parse_qs, unquote_plus

try:
    import requests
    from bs4 import BeautifulSoup
except Exception:  # pragma: no cover - tests may run without network libs
    requests = None
    BeautifulSoup = None

from .utils import limpar, normalizar_chave, adicionar_unico, classificar_polo

ESAJ_BASE = "https://esaj.tjsp.jus.br/cpopg"
PASTA_BASE = "https://esaj.tjsp.jus.br/pastadigital/"
RAW_HTML_DIR = Path(__file__).parent.parent / "esaj_raw" / "tjsp" / "cpopg"

CNJ_RE = re.compile(r"^(\d{7})-(\d{2})\.(\d{4})\.8\.26\.(\d{4})$")


def montar_url_busca(numero: str) -> str:
    m = CNJ_RE.match(numero)
    if not m:
        raise ValueError("Número fora do formato CNJ esperado para eSAJ/TJSP")
    params = {
        "conversationId": "",
        "cbPesquisa": "NUMPROC",
        "numeroDigitoAnoUnificado": f"{m.group(1)}-{m.group(2)}.{m.group(3)}",
        "foroNumeroUnificado": m.group(4),
        "dadosConsulta.valorConsultaNuUnificado": numero,
        "dadosConsulta.tipoNuProcesso": "UNIFICADO",
    }
    return f"{ESAJ_BASE}/search.do?{urlencode(params)}"


def carregar_pagina(session: requests.Session, entrada: str) -> requests.Response:
    if not requests:
        raise RuntimeError("requests/bs4 não disponíveis no ambiente")
    if entrada.lower().startswith(("http://", "https://")):
        parsed = urlparse(entrada)
        if parsed.netloc != "esaj.tjsp.jus.br" or not parsed.path.startswith("/cpopg/"):
            raise ValueError("URL deve ser do eSAJ/TJSP cpopg.")
        resp = session.get(entrada, timeout=30, allow_redirects=True)
        return resp
    # assume it's a CNJ number
    session.get(f"{ESAJ_BASE}/open.do", timeout=20)
    resp = session.get(montar_url_busca(entrada), timeout=30, allow_redirects=True)
    return resp


def extrair_dados_basicos(soup: "BeautifulSoup", url_final: str) -> dict:
    campos_rotulados = {}
    for container_id in ("containerDadosPrincipaisProcesso", "maisDetalhes"):
        cont = soup.find(id=container_id)
        if cont:
            for label in cont.find_all(class_=lambda c: c and "unj-label" in c):
                chave = normalizar_chave(label.get_text(" ", strip=True))
                if not chave:
                    continue
                parent = label.find_parent()
                valor = ""
                if parent:
                    partes = []
                    for child in parent.children:
                        if child is label:
                            continue
                        texto = child.get_text(" ", strip=True) if hasattr(child, "get_text") else str(child)
                        texto = limpar(texto)
                        if texto:
                            partes.append(texto)
                    valor = limpar(" ".join(partes))
                if valor:
                    campos_rotulados[chave] = valor
    dados = {
        "numero": (soup.find(id='numeroProcesso').get_text(' ', strip=True) if soup.find(id='numeroProcesso') else ""),
        "classe": (soup.find(id='classeProcesso').get_text(' ', strip=True) if soup.find(id='classeProcesso') else ""),
        "url": url_final,
        "campos_rotulados": campos_rotulados,
    }
    return dados


def extrair_partes(soup: "BeautifulSoup") -> dict:
    def extrair_tabela(tabela):
        partes = []
        if not tabela:
            return partes
        tipo_atual = ""
        for row in tabela.find_all('tr'):
            label_tag = row.find('span', {'class': 'label'})
            if label_tag:
                tipo_atual = limpar(label_tag.get_text(' ', strip=True))
                continue

            tipo_tag = row.find(class_=lambda c: c and 'tipoDeParticipacao' in c)
            nome_tag = row.find('td', class_=lambda c: c and ('nomeParteEAdvogado' in c or 'nomeParteEAdvogados' in c))
            if not nome_tag:
                continue

            tipo = limpar(tipo_tag.get_text(' ', strip=True)) if tipo_tag else tipo_atual
            linhas = [limpar(x) for x in nome_tag.get_text('\n', strip=True).splitlines() if limpar(x)]
            nomes: list[str] = []
            advogados: list[str] = []
            proximo_adv = False
            for item in linhas:
                if re.match(r'^Advogad[oa]:', item, re.I):
                    resto = limpar(re.sub(r'^Advogad[oa]:', '', item, flags=re.I))
                    if resto:
                        advogados.append(resto)
                    proximo_adv = True
                    continue
                if proximo_adv:
                    advogados.append(item)
                    proximo_adv = False
                    continue
                if 'OAB' in item.upper():
                    advogados.append(item)
                    continue
                nomes.append(item)

            if nomes or advogados or tipo:
                partes.append({
                    'tipo': tipo,
                    'nomes': nomes,
                    'advogados': advogados,
                })
        return partes

    principais = extrair_tabela(soup.find('table', id='tablePartesPrincipais'))
    todas = extrair_tabela(soup.find('table', id='tableTodasPartes'))
    base = todas or principais
    polo_ativo = []
    polo_passivo = []
    polo_desconhecido = []
    for parte in base:
        tipo = parte.get('tipo', '')
        nomes = parte.get('nomes', []) or []
        polo = classificar_polo(tipo or ' '.join(nomes))
        parte_saida = {
            'tipo': tipo,
            'nomes': nomes,
            'advogados': parte.get('advogados', []),
        }
        if polo == 'ativo':
            polo_ativo.append(parte_saida)
        elif polo == 'passivo':
            polo_passivo.append(parte_saida)
        else:
            polo_desconhecido.append(parte_saida)
    return {
        'principais': principais,
        'todas': todas,
        'polo_ativo': polo_ativo,
        'polo_passivo': polo_passivo,
        'polo_desconhecido': polo_desconhecido,
    }


def extrair_movimentacoes(soup: "BeautifulSoup") -> list:
    tabela = soup.find(['table', 'tbody'], id='tabelaTodasMovimentacoes') or soup.find(['table', 'tbody'], id='tabelaUltimasMovimentacoes')
    if not tabela:
        return []
    movimentos = []
    for idx, tr in enumerate(tabela.find_all('tr', class_=lambda c: c and 'containerMovimentacao' in c), 1):
        data_tag = tr.find('td', class_=lambda c: c and 'dataMovimentacao' in c)
        desc_tag = tr.find('td', class_=lambda c: c and 'descricaoMovimentacao' in c)
        if not desc_tag:
            continue
        titulo = desc_tag.find('a').get_text(' ', strip=True) if desc_tag.find('a') else limpar(desc_tag.get_text(' ', strip=True))
        texto = limpar(desc_tag.get_text(' ', strip=True))
        movimentos.append({'ordem': idx, 'data': (data_tag.get_text(' ', strip=True) if data_tag else ''), 'titulo': titulo, 'teor': texto, 'texto': texto, 'documentos': []})
    return movimentos


def montar_extrato(entrada: str, baixar_pecas: bool = False, limite_pecas: int = 3, inspecionar_pecas: bool = False, limite_inspecao_pecas: int = 10, salvar_html: bool = True) -> dict:
    session = requests.Session() if requests else None
    if session is None:
        raise RuntimeError('requests/bs4 não disponíveis no ambiente')
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (esaj-datajud)',
        'Referer': f'{ESAJ_BASE}/open.do',
    })
    response = carregar_pagina(session, entrada)
    soup = BeautifulSoup(response.text, 'html.parser')
    dados_basicos = extrair_dados_basicos(soup, response.url)
    movimentos = extrair_movimentacoes(soup)
    partes = extrair_partes(soup)
    extrato = {
        'origem': {'sistema': 'eSAJ', 'tribunal': 'TJSP', 'consulta': 'cpopg', 'entrada': entrada, 'url_final': response.url, 'data_coleta': datetime.now(timezone.utc).isoformat()},
        'dados_basicos': dados_basicos,
        'partes': partes,
        'movimentacoes': movimentos,
        'documentos': {},
    }
    return extrato
