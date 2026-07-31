import json
from pathlib import Path

from esaj_datajud import esaj


class FakeResponse:
    status_code = 200

    def __init__(self, text="", content=b"", url="https://esaj.tjsp.jus.br/pastadigital/doc"):
        self.text = text
        self.content = content or text.encode("utf-8")
        self.url = url


class FakeSession:
    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = []

    def get(self, url, **kwargs):
        self.calls.append({"url": url, "kwargs": kwargs})
        return self.responses.pop(0)


def _request_scope():
    scope = [
        {
            "data": {
                "title": "Decisão",
                "cdDocumento": "123456",
                "cdFormatoDoc": "1",
                "sigiloAbsoluto": False,
                "flPeticaoInicial": False,
                "flProtocolado": True,
            },
            "children": [
                {
                    "data": {
                        "title": "Página 1",
                        "indicePagina": 1,
                        "nuPaginas": 2,
                        "documentoSigiloso": False,
                        "possuiDocumentoOriginal": True,
                        "parametros": (
                            "numInicial=1&numFinal=2&nuPagina=1&idDocumento=ABC&"
                            "sigiloExterno=false&cdFormatoDoc=1"
                        ),
                    }
                }
            ],
        }
    ]
    return f"<script>var requestScope = {json.dumps(scope)};</script>"


def _movimentos(doc):
    return [{"documentos": [doc]}]


def test_obter_metadados_pasta_documento_parseia_request_scope():
    session = FakeSession([FakeResponse(text=_request_scope())])

    metadados = esaj.obter_metadados_pasta_documento(
        session,
        {"href": "https://esaj.tjsp.jus.br/pastadigital/viewer"},
    )

    assert metadados["status"] == "ok"
    assert metadados["cd_documento"] == "123456"
    assert metadados["total_paginas_no_documento"] == 1
    assert metadados["paginas"][0]["id_documento"] == "ABC"


def test_obter_metadados_pasta_documento_sem_request_scope():
    session = FakeSession([FakeResponse(text="<html>sem escopo</html>", url="https://final")])

    metadados = esaj.obter_metadados_pasta_documento(
        session,
        {"href": "https://esaj.tjsp.jus.br/pastadigital/viewer"},
    )

    assert metadados == {"status": "sem_request_scope", "url_final": "https://final"}


def test_iterar_docs_publicos_filtra_e_deduplica():
    docs = list(
        esaj.iterar_docs_publicos(
            [
                {
                    "documentos": [
                        {"cd_documento": "1", "status_acesso": "publico_candidato"},
                        {"cd_documento": "1", "status_acesso": "publico_candidato"},
                        {"cd_documento": "2", "status_acesso": "restrito_por_senha"},
                        {"cd_documento": "", "status_acesso": "publico_candidato"},
                    ]
                }
            ]
        )
    )

    assert docs == [{"cd_documento": "1", "status_acesso": "publico_candidato"}]


def test_inspecionar_pecas_publicas_respeita_limite(monkeypatch):
    monkeypatch.setattr(
        esaj,
        "obter_metadados_pasta_documento",
        lambda session, doc: {"status": "ok", "cd_documento": doc["cd_documento"]},
    )
    movimentos = _movimentos(
        {"cd_documento": "1", "titulo": "Decisão", "status_acesso": "publico_candidato"}
    )

    resultado = esaj.inspecionar_pecas_publicas(object(), movimentos, limite=1)

    assert resultado[0]["pasta_digital"]["cd_documento"] == "1"


def test_inspecionar_pecas_publicas_registra_erro(monkeypatch):
    def falha(session, doc):
        raise RuntimeError("fonte indisponível")

    monkeypatch.setattr(esaj, "obter_metadados_pasta_documento", falha)
    movimentos = _movimentos(
        {"cd_documento": "1", "titulo": "Decisão", "status_acesso": "publico_candidato"}
    )

    resultado = esaj.inspecionar_pecas_publicas(object(), movimentos, limite=0)

    assert resultado[0]["pasta_digital"]["status"] == "erro"
    assert "fonte indisponível" in resultado[0]["pasta_digital"]["mensagem"]


def test_baixar_pecas_publicas_baixa_pdf(monkeypatch):
    monkeypatch.setattr(Path, "mkdir", lambda self, parents=False, exist_ok=False: None)
    escritos = {}
    monkeypatch.setattr(
        Path, "write_bytes", lambda self, content: escritos.setdefault(str(self), content)
    )
    session = FakeSession([FakeResponse(content=b"%PDF-1.4 fake")])
    doc = {
        "cd_documento": "123",
        "titulo": "Decisão",
        "href": "https://viewer",
        "status_acesso": "publico_candidato",
        "pasta_digital": {"status": "ok", "paginas": [{"parametros_pdf": "idDocumento=ABC"}]},
    }

    resultado = esaj.baixar_pecas_publicas(session, _movimentos(doc), Path("pecas"), limite=1)

    assert resultado[0]["status"] == "baixado"
    assert list(escritos.values())[0].startswith(b"%PDF")


def test_baixar_pecas_publicas_marca_nao_pdf():
    session = FakeSession([FakeResponse(content=b"<html>erro</html>")])
    doc = {
        "cd_documento": "123",
        "titulo": "Decisão",
        "href": "https://viewer",
        "status_acesso": "publico_candidato",
        "pasta_digital": {"status": "ok", "paginas": [{"parametros_pdf": "idDocumento=ABC"}]},
    }

    resultado = esaj.baixar_pecas_publicas(session, _movimentos(doc), Path("pecas"), limite=1)

    assert resultado == []
    assert doc["download_status"] == "nao_pdf"


def test_baixar_pecas_publicas_marca_sem_paginas():
    doc = {
        "cd_documento": "123",
        "titulo": "Decisão",
        "status_acesso": "publico_candidato",
        "pasta_digital": {"status": "ok", "paginas": []},
    }

    resultado = esaj.baixar_pecas_publicas(
        FakeSession([]), _movimentos(doc), Path("pecas"), limite=1
    )

    assert resultado == []
    assert doc["download_status"] == "sem_paginas"


def test_baixar_pecas_publicas_marca_status_pasta_digital():
    doc = {
        "cd_documento": "123",
        "titulo": "Decisão",
        "status_acesso": "publico_candidato",
        "pasta_digital": {"status": "sem_request_scope"},
    }

    resultado = esaj.baixar_pecas_publicas(
        FakeSession([]), _movimentos(doc), Path("pecas"), limite=1
    )

    assert resultado == []
    assert doc["download_status"] == "sem_request_scope"


def test_baixar_pecas_publicas_respeita_limite_zero_com_multiplos_docs(monkeypatch):
    monkeypatch.setattr(Path, "mkdir", lambda self, parents=False, exist_ok=False: None)
    monkeypatch.setattr(Path, "write_bytes", lambda self, content: len(content))
    session = FakeSession([FakeResponse(content=b"%PDF one"), FakeResponse(content=b"%PDF two")])
    docs = [
        {
            "cd_documento": "1",
            "titulo": "Um",
            "status_acesso": "publico_candidato",
            "pasta_digital": {"status": "ok", "paginas": [{"parametros_pdf": "id=1"}]},
        },
        {
            "cd_documento": "2",
            "titulo": "Dois",
            "status_acesso": "publico_candidato",
            "pasta_digital": {"status": "ok", "paginas": [{"parametros_pdf": "id=2"}]},
        },
    ]

    resultado = esaj.baixar_pecas_publicas(session, [{"documentos": docs}], Path("pecas"), limite=0)

    assert [item["cd_documento"] for item in resultado] == ["1", "2"]
