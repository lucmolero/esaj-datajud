"""High-level API for lawyers and systems.

This module exposes the public functions meant to be used by applications,
notebooks, scripts or command-line wrappers.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from . import djen, esaj
from .utils import limpar


def search_processo(numero: str) -> dict[str, Any]:
    """Retorna um resumo rápido do processo eSAJ."""
    extrato = esaj.montar_extrato(numero, baixar_pecas=False, limite_pecas=0, inspecionar_pecas=False, limite_inspecao_pecas=0, salvar_html=False)
    basicos = extrato.get("dados_basicos", {})
    movimento = extrato.get("movimentacoes", [])
    ultima = movimento[-1] if movimento else {}
    return {
        "numero": basicos.get("numero", ""),
        "classe": basicos.get("classe", ""),
        "assunto": basicos.get("assunto", ""),
        "foro": basicos.get("foro", ""),
        "vara": basicos.get("vara", ""),
        "juiz": basicos.get("juiz", ""),
        "ultima_movimentacao": ultima.get("titulo") or ultima.get("texto", ""),
        "ultima_data": ultima.get("data", ""),
        "url": extrato.get("origem", {}).get("url_final", ""),
        "status": "ok",
        "mensagem": "Processo consultado com sucesso",
    }


def get_extrato(numero: str, baixar_pecas: bool = False, limite_pecas: int = 3) -> dict[str, Any]:
    """Montar o extrato completo do processo eSAJ."""
    return esaj.montar_extrato(numero, baixar_pecas=baixar_pecas, limite_pecas=limite_pecas, inspecionar_pecas=False, limite_inspecao_pecas=0, salvar_html=False)


def get_partes(numero: str) -> dict[str, Any]:
    """Retorna as partes classificadas do processo eSAJ."""
    extrato = esaj.montar_extrato(numero, baixar_pecas=False, limite_pecas=0, inspecionar_pecas=False, limite_inspecao_pecas=0, salvar_html=False)
    return extrato.get("partes", {"principais": [], "todas": [], "polo_ativo": [], "polo_passivo": [], "polo_desconhecido": []})


def baixar_pecas(extrato: dict[str, Any], destino: Path, sobrescrever: bool = False) -> list[dict[str, Any]]:
    """Baixa peças públicas do extrato para a pasta de destino.

    Atualmente essa função percorre a lista de documentos públicos candidatos.
    Se a peça não estiver disponível ou for restrita, o retorno contém o status apropriado.
    """
    destino.mkdir(parents=True, exist_ok=True)
    resultado: list[dict[str, Any]] = []
    documentos = extrato.get("documentos", {}).get("publicos_candidatos_unicos", [])
    for documento in documentos:
        status = documento.get("status_acesso", "")
        cd_documento = documento.get("cd_documento", "")
        titulo = limpar(documento.get("titulo", "documento"))
        arquivo_nome = f"peca_{cd_documento or 'sem-id'}_{titulo[:40].replace(' ', '_')}.pdf"
        destino_path = destino / arquivo_nome
        if destino_path.exists() and not sobrescrever:
            resultado.append({"cd_documento": cd_documento, "arquivo": str(destino_path), "status": "existente"})
            continue
        resultado.append({"cd_documento": cd_documento, "arquivo": str(destino_path), "status": "nao_baixado_por_falta_de_download"})
    return resultado


def resumo_rapido(numero: str) -> str:
    """Gera um resumo de texto curto para uso em briefing ou e-mail."""
    info = search_processo(numero)
    partes = get_partes(numero)
    ativo_nomes = [parte['nomes'][0] if parte.get('nomes') else '' for parte in partes.get('polo_ativo', [])]
    passivo_nomes = [parte['nomes'][0] if parte.get('nomes') else '' for parte in partes.get('polo_passivo', [])]
    ativo = ", ".join([nome for nome in ativo_nomes if nome])[:250]
    passivo = ", ".join([nome for nome in passivo_nomes if nome])[:250]
    return (
        f"Processo {info.get('numero')} | Classe: {info.get('classe')} | Vara: {info.get('vara')}\n"
        f"Última movimentação: {info.get('ultima_movimentacao')} em {info.get('ultima_data')}\n"
        f"Parte ativa: {ativo or 'não disponível'} | Parte passiva: {passivo or 'não disponível'}"
    )


def consultar_djen(numero: str, data_inicio: str = "") -> list[dict[str, Any]]:
    """Consulta as comunicações do DJEN para um processo."""
    return djen.consultar_processo(numero, data_inicio=data_inicio)
