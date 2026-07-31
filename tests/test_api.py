from pathlib import Path

from esaj_datajud import api


def _extrato():
    return {
        "status": "ok",
        "origem": {"url_final": "https://example.test"},
        "dados_basicos": {
            "numero": "1076539-20.2019.8.26.0100",
            "classe": "Ação Civil Pública",
            "assunto": "Meio Ambiente",
            "foro": "Foro Central",
            "vara": "2ª Vara",
            "juiz": "Dr. Exemplo",
        },
        "partes": {
            "principais": [],
            "todas": [],
            "polo_ativo": [{"nomes": ["Empresa Autora"]}],
            "polo_passivo": [{"nomes": ["Empresa Ré"]}],
            "polo_desconhecido": [],
        },
        "movimentacoes": [{"titulo": "Conclusos", "data": "31/07/2026"}],
        "documentos": {"publicos_candidatos_unicos": [{"cd_documento": "123"}]},
    }


def test_search_processo_signature():
    resultado = api.search_processo
    assert callable(resultado)


def test_get_partes_signature():
    resultado = api.get_partes
    assert callable(resultado)


def test_get_extrato_signature():
    resultado = api.get_extrato
    assert callable(resultado)


def test_resumo_rapido_signature():
    resultado = api.resumo_rapido
    assert callable(resultado)


def test_consultar_djen_signature():
    resultado = api.consultar_djen
    assert callable(resultado)


def test_create_client_signature():
    resultado = api.create_client
    assert callable(resultado)


def test_create_client_retorna_cliente_configuravel():
    client = api.create_client()

    assert client.config.timeout == 30.0
    assert client.cache is None


def test_search_processo_resume_extrato(monkeypatch):
    monkeypatch.setattr(api, "get_extrato", lambda numero: _extrato())

    resumo = api.search_processo("1076539-20.2019.8.26.0100")

    assert resumo["numero"] == "1076539-20.2019.8.26.0100"
    assert resumo["ultima_movimentacao"] == "Conclusos"


def test_resumo_rapido_usa_partes_do_extrato(monkeypatch):
    monkeypatch.setattr(api, "get_extrato", lambda numero: _extrato())

    resumo = api.resumo_rapido("1076539-20.2019.8.26.0100")

    assert "Empresa Autora" in resumo
    assert "Empresa Ré" in resumo


def test_baixar_pecas_delega_para_esaj(monkeypatch):
    chamadas = {}
    monkeypatch.setattr(api.esaj, "criar_session", lambda: object())

    def fake_baixar(session, movimentos, destino, limite, sobrescrever):
        chamadas["movimentos"] = movimentos
        chamadas["destino"] = destino
        chamadas["limite"] = limite
        chamadas["sobrescrever"] = sobrescrever
        return [{"status": "baixado"}]

    monkeypatch.setattr(api.esaj, "baixar_pecas_publicas", fake_baixar)

    resultado = api.baixar_pecas(_extrato(), Path("pecas"), sobrescrever=True, limite=1)

    assert resultado == [{"status": "baixado"}]
    assert chamadas["movimentos"][0]["documentos"][0]["cd_documento"] == "123"
    assert chamadas["limite"] == 1
