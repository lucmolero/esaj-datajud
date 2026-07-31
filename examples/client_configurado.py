from esaj_datajud import EsajDatajudClient, EsajDatajudConfig


def main() -> None:
    client = EsajDatajudClient(
        EsajDatajudConfig(
            timeout=20,
            rate_limit_interval=1.0,
            cache_enabled=True,
            cache_dir=".esaj_datajud_cache",
            cache_ttl_seconds=6 * 60 * 60,
        )
    )

    numero = "1076539-20.2019.8.26.0100"
    resumo = client.search_processo(numero)
    print(resumo["numero"], resumo["classe"])


if __name__ == "__main__":
    main()
