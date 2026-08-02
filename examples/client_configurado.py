from nanojud import NanoJudClient, NanoJudConfig


def main() -> None:
    client = NanoJudClient(
        NanoJudConfig(
            timeout=20,
            rate_limit_interval=1.0,
            cache_enabled=True,
            cache_dir=".nanojud_cache",
            cache_ttl_seconds=6 * 60 * 60,
        )
    )

    # Processo público institucional usado para demonstração.
    numero = "0015020-23.2010.8.26.0053"
    resumo = client.search_processo(numero)
    print(resumo["numero"], resumo["classe"])


if __name__ == "__main__":
    main()
