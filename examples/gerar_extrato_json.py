"""Gera um extrato JSON de processo."""

import json
from pathlib import Path

from esaj_datajud import api


def main() -> None:
    numero = "1076539-20.2019.8.26.0100"
    destino = Path("extrato.json")
    extrato = api.get_extrato(numero)
    destino.write_text(json.dumps(extrato, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Extrato salvo em {destino}")


if __name__ == "__main__":
    main()
