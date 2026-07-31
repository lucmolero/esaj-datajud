esaj-datajud
=============

Biblioteca Python de alto nível para extração e consulta de processos no eSAJ/TJSP e DJEN/DataJud.

A proposta é oferecer uma API profissional para advogados, escritórios e sistemas jurídicos.

## Instalação

```bash
python -m pip install -r requirements.txt
python -m pip install -e .
```

## Uso rápido em Python

```python
from esaj_datajud import api

resumo = api.search_processo("1076539-20.2019.8.26.0100")
print(resumo)

extrato = api.get_extrato("1076539-20.2019.8.26.0100")
print(extrato["dados_basicos"])

comunicacoes = api.consultar_djen("1076539-20.2019.8.26.0100")
print(len(comunicacoes))
```

## CLI

```bash
python -m esaj_datajud.cli search 1076539-20.2019.8.26.0100
python -m esaj_datajud.cli extrato 1076539-20.2019.8.26.0100 --out extrato.json
python -m esaj_datajud.cli djen 1076539-20.2019.8.26.0100 --out djen.json
```

## Arquitetura

- `api` — camada pública de alto nível, pensada para advogados e sistemas.
- `esaj` — parser e orquestração de dados do eSAJ.
- `djen` — cliente para buscar comunicações do DJEN.
- `utils` — helpers de texto e normalização.
- `cli` — interface de linha de comando para uso rápido.

## Autor / Contato

- Luciano Molero — https://www.linkedin.com/in/luciano-molero/

