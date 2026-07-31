"""Gera envelope versionado com dados extraidos de multiplas fontes."""

import json

from esaj_datajud import api


def main() -> None:
    numero = "1076539-20.2019.8.26.0100"
    envelope = api.extract_process(
        numero,
        sources=("datajud", "djen"),
    )

    print(json.dumps(envelope, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
