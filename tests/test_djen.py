from esaj_datajud import djen
from esaj_datajud.djen import _parse_data
from esaj_datajud.exceptions import AcessoRestrito


def test_parse_data_iso():
    assert _parse_data({"data_disponibilizacao": "2026-07-30T10:00:00"}) == "2026-07-30"


def test_parse_data_brasileira():
    assert _parse_data({"datadisponibilizacao": "30/07/2026"}) == "2026-07-30"


def test_parse_data_vazia():
    assert _parse_data({}) == ""


class FakeResponse:
    def __init__(self, status_code, payload):
        self.status_code = status_code
        self._payload = payload

    def json(self):
        return self._payload


class FakeSession:
    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = []

    def get(self, url, params=None, timeout=None):
        self.calls.append({"url": url, "params": dict(params or {}), "timeout": timeout})
        return self.responses.pop(0)


def test_consultar_processo_pagina_e_deduplica():
    session = FakeSession(
        [
            FakeResponse(
                200,
                {
                    "items": [
                        {"id": "1", "texto": "um", "data_disponibilizacao": "2026-07-30"},
                        {"id": "1", "texto": "duplicado", "data_disponibilizacao": "2026-07-30"},
                    ]
                },
            )
        ]
    )

    resultado = djen.consultar_processo(
        "1076539-20.2019.8.26.0100",
        session=session,
        page_size=20,
        sleep=lambda _: None,
    )

    assert len(resultado) == 1
    assert resultado[0]["texto"] == "um"


def test_consultar_processo_retries_429():
    session = FakeSession(
        [
            FakeResponse(429, {}),
            FakeResponse(200, [{"id": "2", "texto": "ok", "datadisponibilizacao": "30/07/2026"}]),
        ]
    )

    resultado = djen.consultar_processo(
        "1076539-20.2019.8.26.0100",
        session=session,
        retry=2,
        sleep=lambda _: None,
    )

    assert len(resultado) == 1
    assert len(session.calls) == 2


def test_consultar_processo_403_vira_acesso_restrito():
    session = FakeSession([FakeResponse(403, {})])

    try:
        djen.consultar_processo("1076539-20.2019.8.26.0100", session=session)
    except AcessoRestrito:
        pass
    else:
        raise AssertionError("403 deveria gerar AcessoRestrito")
