"""Gera envelope versionado com dados extraidos de multiplas fontes."""

import json

from esaj_datajud import api


def main() -> None:
    # Processo público institucional usado para demonstração.
    numero = "0015020-23.2010.8.26.0053"
    envelope = api.extract_process(
        numero,
        sources=("datajud", "djen"),
    )

    print(json.dumps(envelope, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
