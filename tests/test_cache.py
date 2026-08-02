from uuid import uuid4

from nanojud.cache import JsonFileCache


def test_json_file_cache_roundtrip():
    cache = JsonFileCache(directory=".tmp/test-cache", ttl_seconds=60)

    cache.set("extrato", "processo-cache", {"status": "ok"})

    assert cache.get("extrato", "processo-cache") == {"status": "ok"}


def test_json_file_cache_miss():
    cache = JsonFileCache(directory=".tmp/test-cache", ttl_seconds=60)

    assert cache.get("extrato", "inexistente") is None


def test_json_file_cache_expirado():
    cache = JsonFileCache(directory=f".tmp/test-cache-expirado-{uuid4()}", ttl_seconds=1)
    path = cache.set("extrato", "processo-expirado", {"status": "ok"})
    path.write_text('{"created_at": 0, "value": {"status": "ok"}}', encoding="utf-8")

    assert cache.get("extrato", "processo-expirado") is None


def test_json_file_cache_ignora_json_corrompido():
    cache = JsonFileCache(directory=f".tmp/test-cache-corrompido-{uuid4()}", ttl_seconds=60)
    path = cache.set("extrato", "processo-corrompido", {"status": "ok"})
    path.write_text("{json inválido", encoding="utf-8")

    assert cache.get("extrato", "processo-corrompido") is None
