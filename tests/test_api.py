from esaj_datajud import api


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
