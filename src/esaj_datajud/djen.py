"""Minimal DJEN client adapted for the library.

This implementation is intentionally small and focused on returning a list of
communications for a given process number. It mirrors behavior of the reference
`djen_coletar.py` but is structured into small functions for reuse and testing.
"""
from datetime import datetime, timedelta
import time
import requests

API_BASE = "https://comunicaapi.pje.jus.br/api/v1/comunicacao"
PAGE_SIZE = 20
MAX_PAGES = 50


def _parse_data(item: dict) -> str:
    raw = item.get("data_disponibilizacao", "")
    if raw and raw[:4].isdigit():
        return raw[:10]
    dd = item.get("datadisponibilizacao", "")
    if dd and "/" in dd:
        p = dd.split("/")
        if len(p) == 3:
            return f"{p[2]}-{p[1]}-{p[0]}"
    return ""


def consultar_processo(numero: str, data_inicio: str = "") -> list:
    """Consulta comunicações do DJEN para um processo.

    Args:
        numero: número do processo no formato CNJ
        data_inicio: opcional, string ISO yyyy-mm-dd para filtrar a partir desta data

    Returns:
        lista de dicionários representando comunicacões
    """
    resultados = []
    ids_vistos = set()
    session = requests.Session()
    params = {"numeroProcesso": numero, "size": PAGE_SIZE, "page": 1}
    if data_inicio:
        params["dataInicio"] = data_inicio

    for page in range(1, MAX_PAGES + 1):
        params["page"] = page
        resp = None
        for tentativa in range(3):
            try:
                resp = session.get(API_BASE, params=params, timeout=30)
                if resp.status_code == 200:
                    break
                if resp.status_code == 429:
                    time.sleep(1 + tentativa)
                    continue
                if resp.status_code == 403:
                    return resultados
                resp = None
            except requests.RequestException:
                time.sleep(1)
        if not resp or resp.status_code != 200:
            break
        try:
            data = resp.json()
        except Exception:
            break
        items = []
        if isinstance(data, list):
            items = data
        elif isinstance(data, dict):
            for key in ("items", "content", "comunicacoes", "resultado"):
                if key in data:
                    items = data[key]
                    break
        if not items:
            break
        novos = 0
        for item in items:
            iid = item.get("id", "")
            if iid in ids_vistos:
                continue
            ids_vistos.add(iid)
            novos += 1
            resultados.append({
                "id": iid,
                "tipoComunicacao": item.get("tipoComunicacao", item.get("tipoDocumento", "")),
                "nomeOrgao": item.get("nomeOrgao", ""),
                "dataDisponibilizacao": _parse_data(item),
                "siglaTribunal": item.get("siglaTribunal", ""),
                "nomeClasse": item.get("nomeClasse", ""),
                "texto": str(item.get("texto", "")),
                "destinatarios": item.get("destinatarios", []),
                "link": item.get("link", ""),
                "meio": item.get("meio", ""),
            })
        if novos == 0 or len(items) < PAGE_SIZE:
            break
        time.sleep(0.2)
    return resultados
