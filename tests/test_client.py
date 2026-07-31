import logging
from uuid import uuid4

import pytest

from esaj_datajud.client import EsajDatajudClient, RateLimitedSession
from esaj_datajud.config import EsajDatajudConfig


def _extrato():
    return {
        "status": "ok",
        "origem": {"url_final": "https://example.test"},
        "dados_basicos": {"numero": "1076539-20.2019.8.26.0100", "classe": "Classe"},
        "partes": {
            "principais": [],
            "todas": [],
            "polo_ativo": [],
            "polo_passivo": [],
            "polo_desconhecido": [],
        },
        "movimentacoes": [{"titulo": "Mov", "data": "31/07/2026"}],
        "documentos": {},
    }


def test_client_get_extrato_usa_cache(monkeypatch):
    chamadas = {"count": 0}

    def fake_montar(*args, **kwargs):
        chamadas["count"] += 1
        return _extrato()

    monkeypatch.setattr("esaj_datajud.client.esaj.montar_extrato", fake_montar)
    client = EsajDatajudClient(
        EsajDatajudConfig(cache_enabled=True, cache_dir=f".tmp/test-client-cache-{uuid4()}")
    )

    primeiro = client.get_extrato("1076539-20.2019.8.26.0100")
    segundo = client.get_extrato("1076539-20.2019.8.26.0100")

    assert primeiro == segundo
    assert chamadas["count"] == 1


def test_client_search_processo_resume_extrato(monkeypatch):
    monkeypatch.setattr("esaj_datajud.client.esaj.montar_extrato", lambda *a, **k: _extrato())

    resumo = EsajDatajudClient().search_processo("1076539-20.2019.8.26.0100")

    assert resumo["classe"] == "Classe"
    assert resumo["ultima_movimentacao"] == "Mov"


def test_rate_limited_session_define_user_agent():
    session = RateLimitedSession(
        timeout=10,
        rate_limit_interval=0,
        logger=logging.getLogger("test"),
        user_agent="teste-agent",
    )

    assert session.timeout == 10
    assert session.headers["User-Agent"] == "teste-agent"


def test_client_get_partes(monkeypatch):
    monkeypatch.setattr("esaj_datajud.client.esaj.montar_extrato", lambda *a, **k: _extrato())

    partes = EsajDatajudClient().get_partes("1076539-20.2019.8.26.0100")

    assert partes["principais"] == []


def test_client_consultar_djen_usa_cache(monkeypatch):
    chamadas = {"count": 0}

    def fake_consultar(*args, **kwargs):
        chamadas["count"] += 1
        return [{"id": "1"}]

    monkeypatch.setattr("esaj_datajud.client.djen.consultar_processo", fake_consultar)
    client = EsajDatajudClient(
        EsajDatajudConfig(cache_enabled=True, cache_dir=f".tmp/test-djen-cache-{uuid4()}")
    )

    primeiro = client.consultar_djen("1076539-20.2019.8.26.0100")
    segundo = client.consultar_djen("1076539-20.2019.8.26.0100")

    assert primeiro == segundo == [{"id": "1"}]
    assert chamadas["count"] == 1


def test_client_consultar_datajud_usa_cache(monkeypatch):
    chamadas = {"count": 0}

    def fake_consultar(*args, **kwargs):
        chamadas["count"] += 1
        return {"status": "ok", "numero_cnj": args[0]}

    monkeypatch.setattr("esaj_datajud.client.datajud.consultar_processo", fake_consultar)
    client = EsajDatajudClient(
        EsajDatajudConfig(cache_enabled=True, cache_dir=f".tmp/test-datajud-cache-{uuid4()}")
    )

    primeiro = client.consultar_datajud("1076539-20.2019.8.26.0100", api_key="abc")
    segundo = client.consultar_datajud("1076539-20.2019.8.26.0100", api_key="abc")

    assert primeiro == segundo
    assert chamadas["count"] == 1


def test_client_extract_process_delega(monkeypatch):
    chamadas = {}

    def fake_extract(numero, **kwargs):
        chamadas["numero"] = numero
        chamadas.update(kwargs)
        return {"status": "ok", "timeline": []}

    monkeypatch.setattr("esaj_datajud.client.extraction.extract_process", fake_extract)
    client = EsajDatajudClient(EsajDatajudConfig(datajud_api_key="abc"))

    resultado = client.extract_process("1076539-20.2019.8.26.0100", sources=("datajud",))

    assert resultado["status"] == "ok"
    assert chamadas["datajud_api_key"] == "abc"


def test_client_baixar_pecas_delega(monkeypatch):
    chamadas = {}

    def fake_baixar(session, movimentos, destino, limite, sobrescrever):
        chamadas["movimentos"] = movimentos
        chamadas["limite"] = limite
        chamadas["sobrescrever"] = sobrescrever
        return [{"status": "baixado"}]

    monkeypatch.setattr("esaj_datajud.client.esaj.baixar_pecas_publicas", fake_baixar)
    client = EsajDatajudClient()

    resultado = client.baixar_pecas(
        {"documentos": {"publicos_candidatos_unicos": [{"cd_documento": "1"}]}},
        destino=__import__("pathlib").Path("pecas"),
        sobrescrever=True,
        limite=1,
    )

    assert resultado == [{"status": "baixado"}]
    assert chamadas["movimentos"][0]["documentos"][0]["cd_documento"] == "1"
    assert chamadas["sobrescrever"] is True


def test_rate_limited_session_request_usa_timeout(monkeypatch):
    chamadas = {}

    def fake_request(self, method, url, **kwargs):
        chamadas["method"] = method
        chamadas["url"] = url
        chamadas["timeout"] = kwargs["timeout"]
        return type("Response", (), {"status_code": 200})()

    monkeypatch.setattr("requests.Session.request", fake_request)
    session = RateLimitedSession(
        timeout=7,
        rate_limit_interval=0,
        logger=logging.getLogger("test"),
        user_agent="agent",
    )

    response = session.request("GET", "https://example.test")

    assert response.status_code == 200
    assert chamadas["timeout"] == 7


def test_rate_limited_session_aguarda_intervalo(monkeypatch):
    sleeps = []
    tempos = iter([10.2])
    monkeypatch.setattr("esaj_datajud.client.time.monotonic", lambda: next(tempos))
    monkeypatch.setattr("esaj_datajud.client.time.sleep", lambda segundos: sleeps.append(segundos))
    session = RateLimitedSession(
        timeout=7,
        rate_limit_interval=1.0,
        logger=logging.getLogger("test"),
        user_agent="agent",
    )
    session._last_request_at = 10.0

    session._wait_if_needed()

    assert sleeps[0] == pytest.approx(0.8)


def test_client_baixar_pecas_usa_movimentacoes_quando_sem_documentos(monkeypatch):
    chamadas = {}

    def fake_baixar(session, movimentos, destino, limite, sobrescrever):
        chamadas["movimentos"] = movimentos
        return []

    monkeypatch.setattr("esaj_datajud.client.esaj.baixar_pecas_publicas", fake_baixar)
    extrato = {"documentos": {}, "movimentacoes": [{"documentos": []}]}

    EsajDatajudClient().baixar_pecas(extrato, destino=__import__("pathlib").Path("pecas"))

    assert chamadas["movimentos"] == [{"documentos": []}]
