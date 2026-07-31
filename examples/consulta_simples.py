"""Consulta simples usando a API pública."""

from esaj_datajud import api


def main() -> None:
    numero = "1076539-20.2019.8.26.0100"
    resumo = api.search_processo(numero)
    print(resumo)


if __name__ == "__main__":
    main()
