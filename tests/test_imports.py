import importlib


def test_imports():
    pkg = importlib.import_module("esaj_datajud")
    assert pkg is not None
    esaj = importlib.import_module("esaj_datajud.esaj")
    djen = importlib.import_module("esaj_datajud.djen")
    utils = importlib.import_module("esaj_datajud.utils")
    assert hasattr(esaj, "montar_extrato")
    assert hasattr(djen, "consultar_processo")
    assert hasattr(utils, "limpar")
