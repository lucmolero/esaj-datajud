import importlib


def test_imports():
    pkg = importlib.import_module("esaj_datajud")
    assert pkg is not None
    esaj = importlib.import_module("esaj_datajud.esaj")
    djen = importlib.import_module("esaj_datajud.djen")
    cache = importlib.import_module("esaj_datajud.cache")
    client = importlib.import_module("esaj_datajud.client")
    config = importlib.import_module("esaj_datajud.config")
    exceptions = importlib.import_module("esaj_datajud.exceptions")
    models = importlib.import_module("esaj_datajud.models")
    utils = importlib.import_module("esaj_datajud.utils")
    assert hasattr(pkg, "EsajDatajudClient")
    assert hasattr(pkg, "EsajDatajudConfig")
    assert hasattr(cache, "JsonFileCache")
    assert hasattr(client, "EsajDatajudClient")
    assert hasattr(config, "EsajDatajudConfig")
    assert hasattr(esaj, "montar_extrato")
    assert hasattr(djen, "consultar_processo")
    assert hasattr(exceptions, "EsajDatajudError")
    assert hasattr(models, "Extrato")
    assert hasattr(utils, "limpar")
