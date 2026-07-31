"""Consulta dados processuais estruturados no DataJud/CNJ."""

from esaj_datajud import api


def main() -> None:
    # Processo público institucional usado para demonstração.
    numero = "0015020-23.2010.8.26.0053"
    resultado = api.consultar_datajud(numero)

    print(resultado["status"])
    print(resultado.get("classe", ""))
    print(len(resultado.get("movimentos", [])))


if __name__ == "__main__":
    main()
