import importlib


def test_imports():
    pkg = importlib.import_module("nanojud")
    assert pkg is not None
    esaj = importlib.import_module("nanojud.esaj")
    djen = importlib.import_module("nanojud.djen")
    cache = importlib.import_module("nanojud.cache")
    client = importlib.import_module("nanojud.client")
    config = importlib.import_module("nanojud.config")
    exceptions = importlib.import_module("nanojud.exceptions")
    models = importlib.import_module("nanojud.models")
    utils = importlib.import_module("nanojud.utils")
    assert hasattr(pkg, "NanoJudClient")
    assert hasattr(pkg, "NanoJudConfig")
    assert hasattr(cache, "JsonFileCache")
    assert hasattr(client, "NanoJudClient")
    assert hasattr(config, "NanoJudConfig")
    assert hasattr(esaj, "montar_extrato")
    assert hasattr(djen, "consultar_processo")
    assert hasattr(exceptions, "NanoJudError")
    assert hasattr(models, "Extrato")
    assert hasattr(utils, "limpar")


def test_import_mcp_server_opcional():
    mcp_server = importlib.import_module("nanojud.mcp_server")

    assert hasattr(mcp_server, "create_server")
