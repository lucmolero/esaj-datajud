import pytest

from esaj_datajud import mcp_server


class FakeFastMCP:
    def __init__(self, name, **kwargs):
        self.name = name
        self.kwargs = kwargs
        self.tools = {}
        self.ran = False
        self.run_kwargs = {}

    def tool(self):
        def decorator(func):
            self.tools[func.__name__] = func
            return func

        return decorator

    def run(self, **kwargs):
        self.ran = True
        self.run_kwargs = kwargs


def test_create_server_exige_extra_mcp(monkeypatch):
    monkeypatch.setattr(mcp_server, "FastMCP", None)

    with pytest.raises(RuntimeError, match="extra MCP"):
        mcp_server.create_server()


def test_create_server_registra_ferramentas(monkeypatch):
    monkeypatch.setattr(mcp_server, "FastMCP", FakeFastMCP)

    server = mcp_server.create_server()

    assert server.name == "esaj-datajud"
    assert "extracao responsavel" in server.kwargs["instructions"]
    assert set(server.tools) == {
        "server_info",
        "validar_cnj",
        "extrair_numeros_cnj_de_texto",
        "consultar_esaj",
        "consultar_datajud",
        "consultar_djen",
        "extrair_processo",
        "gerar_timeline",
    }


def test_create_server_real_quando_sdk_mcp_instalado():
    if mcp_server.FastMCP is None:
        pytest.skip("SDK MCP nao instalado")

    server = mcp_server.create_server()

    assert type(server).__name__ == "FastMCP"


def test_ferramentas_mcp_basicas(monkeypatch):
    monkeypatch.setattr(mcp_server, "FastMCP", FakeFastMCP)
    server = mcp_server.create_server()

    info = server.tools["server_info"]()
    validacao = server.tools["validar_cnj"]("1076539-20.2019.8.26.0100")
    numeros = server.tools["extrair_numeros_cnj_de_texto"]("Processo 1076539-20.2019.8.26.0100")

    assert info["transport"] == "stdio"
    assert info["scope"] == "local_read_only_extraction"
    assert validacao["digitos"] == "10765392020198260100"
    assert numeros["count"] == 1


def test_ferramentas_mcp_delegam_para_api(monkeypatch):
    monkeypatch.setattr(mcp_server, "FastMCP", FakeFastMCP)
    monkeypatch.setattr(
        mcp_server.api,
        "get_extrato",
        lambda numero, salvar_html=False: {"numero": numero, "salvar_html": salvar_html},
    )
    monkeypatch.setattr(
        mcp_server.api,
        "consultar_datajud",
        lambda numero, include_raw=False, api_key=None: {
            "numero": numero,
            "include_raw": include_raw,
            "api_key": api_key,
        },
    )
    monkeypatch.setattr(
        mcp_server.api,
        "consultar_djen",
        lambda numero, data_inicio="": [{"numero": numero, "data_inicio": data_inicio}],
    )
    monkeypatch.setattr(
        mcp_server.api,
        "extract_process",
        lambda numero, **kwargs: {
            "schema_version": "1.0",
            "package_version": "0.5.0",
            "status": "ok",
            "numero_cnj": numero,
            "sources": list(kwargs["sources"]),
            "timeline": [{"fonte": "datajud"}],
            "errors": [],
            "kwargs": kwargs,
        },
    )
    server = mcp_server.create_server()

    assert server.tools["consultar_esaj"]("1076539-20.2019.8.26.0100", True)["salvar_html"] is True
    assert (
        server.tools["consultar_datajud"]("1076539-20.2019.8.26.0100", True, "abc")["api_key"]
        == "abc"
    )
    djen = server.tools["consultar_djen"]("1076539-20.2019.8.26.0100", "2026-01-01")
    assert djen["count"] == 1
    assert djen["comunicacoes"][0]["data_inicio"] == "2026-01-01"

    envelope = server.tools["extrair_processo"](
        "1076539-20.2019.8.26.0100",
        sources=["datajud", "djen"],
        include_raw=True,
    )
    linha = server.tools["gerar_timeline"](
        "1076539-20.2019.8.26.0100",
        sources=["datajud"],
    )

    assert envelope["kwargs"]["sources"] == ("datajud", "djen")
    assert envelope["kwargs"]["include_raw"] is True
    assert linha["timeline"] == [{"fonte": "datajud"}]


def test_main_executa_servidor(monkeypatch):
    server = FakeFastMCP("esaj-datajud")
    monkeypatch.setattr(mcp_server, "create_server", lambda: server)

    mcp_server.main()

    assert server.ran is True
    assert server.run_kwargs == {"transport": "stdio"}
