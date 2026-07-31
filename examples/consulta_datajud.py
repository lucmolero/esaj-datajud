"""Consulta dados processuais estruturados no DataJud/CNJ."""

import os

from esaj_datajud import api


def main() -> None:
    numero = "1076539-20.2019.8.26.0100"
    resultado = api.consultar_datajud(
        numero,
        api_key=os.getenv("DATAJUD_API_KEY"),
    )

    print(resultado["status"])
    print(resultado.get("classe", ""))
    print(len(resultado.get("movimentos", [])))


if __name__ == "__main__":
    main()
