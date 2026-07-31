from esaj_datajud.cache import JsonFileCache


def test_json_file_cache_roundtrip():
    cache = JsonFileCache(directory=".tmp/test-cache", ttl_seconds=60)

    cache.set("extrato", "processo-cache", {"status": "ok"})

    assert cache.get("extrato", "processo-cache") == {"status": "ok"}


def test_json_file_cache_miss():
    cache = JsonFileCache(directory=".tmp/test-cache", ttl_seconds=60)

    assert cache.get("extrato", "inexistente") is None
