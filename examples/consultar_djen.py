"""Consulta comunicações do DJEN."""

from nanojud import api


def main() -> None:
    # Processo público institucional usado para demonstração.
    numero = "0015020-23.2010.8.26.0053"
    comunicacoes = api.consultar_djen(numero)
    print(f"Comunicações encontradas: {len(comunicacoes)}")


if __name__ == "__main__":
    main()
