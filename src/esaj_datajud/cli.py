"""Command-line interface for esaj_datajud."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from . import api


def _format_json(data: dict) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2)


def _print_result(result: dict | list) -> None:
    if isinstance(result, dict):
        print(_format_json(result))
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="esaj", description="Ferramenta de linha de comando para eSAJ e DJEN."
    )
    sub = parser.add_subparsers(dest="command")

    search = sub.add_parser("search", help="Consultar resumo rápido de processo eSAJ")
    search.add_argument("numero", help="Número CNJ do processo")

    extrato = sub.add_parser("extrato", help="Gerar extrato completo de processo eSAJ")
    extrato.add_argument("numero", help="Número CNJ do processo")
    extrato.add_argument("--out", default="extrato.json", help="Arquivo de saída JSON")
    extrato.add_argument(
        "--baixar-pecas", action="store_true", help="Baixar peças públicas vinculadas"
    )
    extrato.add_argument(
        "--limite-pecas", type=int, default=3, help="Número máximo de peças para baixar"
    )

    partes = sub.add_parser("partes", help="Listar partes do processo")
    partes.add_argument("numero", help="Número CNJ do processo")

    djen_cmd = sub.add_parser("djen", help="Consultar comunicações DJEN/DataJud")
    djen_cmd.add_argument("numero", help="Número CNJ do processo")
    djen_cmd.add_argument("--out", default="djen.json", help="Arquivo de saída JSON")

    args = parser.parse_args(argv)
    if args.command == "search":
        resultado = api.search_processo(args.numero)
        _print_result(resultado)
        return 0

    if args.command == "extrato":
        resultado = api.get_extrato(
            args.numero, baixar_pecas=args.baixar_pecas, limite_pecas=args.limite_pecas
        )
        Path(args.out).write_text(_format_json(resultado), encoding="utf-8")
        print(f"Extrato salvo em: {args.out}")
        return 0

    if args.command == "partes":
        resultado = api.get_partes(args.numero)
        _print_result(resultado)
        return 0

    if args.command == "djen":
        resultado = api.consultar_djen(args.numero)
        Path(args.out).write_text(
            json.dumps(resultado, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(f"DJEN salvo em: {args.out}")
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
