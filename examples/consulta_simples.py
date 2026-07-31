"""Consulta simples usando a API pública."""

from esaj_datajud import api


def main() -> None:
    # Processo público institucional usado para demonstração.
    numero = "0015020-23.2010.8.26.0053"
    resumo = api.search_processo(numero)
    print(resumo)


if __name__ == "__main__":
    main()
