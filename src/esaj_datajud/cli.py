"""Interface de linha de comando para esaj-datajud."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, TypeAlias, cast

from . import api
from .exceptions import EsajDatajudError

JsonPayload: TypeAlias = dict[str, Any] | list[Any]


def _format_json(data: JsonPayload) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2)


def _print_result(result: JsonPayload) -> None:
    print(_format_json(result))


def _erro_json(exc: Exception) -> str:
    return _format_json({"status": "erro", "erro": exc.__class__.__name__, "mensagem": str(exc)})


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="esaj",
        description="Ferramenta profissional de linha de comando para eSAJ/TJSP e DJEN.",
    )
    sub = parser.add_subparsers(dest="command")

    search = sub.add_parser("search", help="Consultar resumo rápido de processo eSAJ")
    search.add_argument("numero", help="Número CNJ do processo")

    extrato = sub.add_parser("extrato", help="Gerar extrato completo de processo eSAJ")
    extrato.add_argument("numero", help="Número CNJ do processo")
    extrato.add_argument("--out", default="extrato.json", help="Arquivo de saída JSON")
    extrato.add_argument(
        "--baixar-pecas",
        action="store_true",
        help="Baixar peças públicas candidatas quando tecnicamente possível",
    )
    extrato.add_argument(
        "--inspecionar-pecas",
        action="store_true",
        help="Inspecionar metadados de peças públicas candidatas",
    )
    extrato.add_argument(
        "--limite-pecas", type=int, default=3, help="Número máximo de peças para baixar"
    )
    extrato.add_argument("--salvar-html", action="store_true", help="Salvar HTML bruto consultado")

    partes = sub.add_parser("partes", help="Listar partes do processo")
    partes.add_argument("numero", help="Número CNJ do processo")

    baixar = sub.add_parser("baixar", help="Baixar peças públicas a partir de um extrato JSON")
    baixar.add_argument("extrato_json", help="Arquivo JSON gerado pelo comando extrato")
    baixar.add_argument("--out", default="pecas", help="Pasta de saída")
    baixar.add_argument(
        "--limite", type=int, default=0, help="Limite de peças; 0 significa sem limite"
    )
    baixar.add_argument(
        "--sobrescrever", action="store_true", help="Sobrescrever arquivos existentes"
    )

    djen_cmd = sub.add_parser("djen", help="Consultar comunicações DJEN/DataJud")
    djen_cmd.add_argument("numero", help="Número CNJ do processo")
    djen_cmd.add_argument("--data-inicio", default="", help="Data inicial ISO yyyy-mm-dd")
    djen_cmd.add_argument("--out", default="djen.json", help="Arquivo de saída JSON")

    args = parser.parse_args(argv)
    try:
        if args.command == "search":
            _print_result(cast(JsonPayload, api.search_processo(args.numero)))
            return 0

        if args.command == "extrato":
            extrato_resultado = api.get_extrato(
                args.numero,
                baixar_pecas=args.baixar_pecas,
                limite_pecas=args.limite_pecas,
                inspecionar_pecas=args.inspecionar_pecas,
                salvar_html=args.salvar_html,
            )
            Path(args.out).write_text(
                _format_json(cast(JsonPayload, extrato_resultado)), encoding="utf-8"
            )
            print(f"Extrato salvo em: {args.out}")
            return 0

        if args.command == "partes":
            _print_result(api.get_partes(args.numero))
            return 0

        if args.command == "baixar":
            extrato_data = json.loads(Path(args.extrato_json).read_text(encoding="utf-8"))
            baixar_resultado = api.baixar_pecas(
                extrato_data,
                Path(args.out),
                sobrescrever=args.sobrescrever,
                limite=args.limite,
            )
            _print_result(baixar_resultado)
            return 0

        if args.command == "djen":
            djen_resultado = api.consultar_djen(args.numero, data_inicio=args.data_inicio)
            Path(args.out).write_text(_format_json(djen_resultado), encoding="utf-8")
            print(f"DJEN salvo em: {args.out}")
            return 0

        parser.print_help()
        return 1
    except EsajDatajudError as exc:
        print(_erro_json(exc))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
