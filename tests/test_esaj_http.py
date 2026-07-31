from esaj_datajud import esaj


class FakeResponse:
    def __init__(self, text: str, url: str, status_code: int = 200):
        self.text = text
        self.url = url
        self.status_code = status_code
        self.content = text.encode("utf-8")


class FakeSession:
    def __init__(self):
        self.calls = []

    def get(self, url, **kwargs):
        self.calls.append((url, kwargs))
        if "search.do" in url:
            html = (
                '<a class="linkProcesso" '
                'href="/cpopg/show.do?processo.foro=100&processo.codigo=ABC">Processo</a>'
            )
            return FakeResponse(
                html,
                url,
            )
        return FakeResponse('<span id="numeroProcesso">1076539-20.2019.8.26.0100</span>', url)


def test_carregar_pagina_segue_lista_de_processos():
    session = FakeSession()

    response = esaj.carregar_pagina(session, "1076539-20.2019.8.26.0100")

    assert "show.do" in response.url
    assert len(session.calls) == 3
