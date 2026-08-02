"""Gera um extrato JSON de processo."""

import json
from pathlib import Path

from nanojud import api


def main() -> None:
    # Processo público institucional usado para demonstração.
    numero = "0015020-23.2010.8.26.0053"
    destino = Path("extrato.json")
    extrato = api.get_extrato(numero)
    destino.write_text(json.dumps(extrato, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Extrato salvo em {destino}")


if __name__ == "__main__":
    main()
