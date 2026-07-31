"""Consulta comunicações do DJEN."""

from esaj_datajud import api


def main() -> None:
    numero = "1076539-20.2019.8.26.0100"
    comunicacoes = api.consultar_djen(numero)
    print(f"Comunicações encontradas: {len(comunicacoes)}")


if __name__ == "__main__":
    main()
