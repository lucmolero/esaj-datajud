# Quickstart

Este guia mostra o caminho mais curto para instalar o projeto e fazer uma consulta básica.

## Instalar

```bash
python -m pip install -e ".[dev]"
```

## Consultar um processo

```python
from esaj_datajud import api

numero = "1076539-20.2019.8.26.0100"
resumo = api.search_processo(numero)

print(resumo["numero"])
print(resumo["classe"])
print(resumo["ultima_movimentacao"])
```

## Gerar extrato

```python
from esaj_datajud import api

extrato = api.get_extrato("1076539-20.2019.8.26.0100")
print(extrato["dados_basicos"])
print(len(extrato["movimentacoes"]))
```

## Consultar pelo terminal

```bash
esaj search 1076539-20.2019.8.26.0100
esaj extrato 1076539-20.2019.8.26.0100 --out extrato.json
```

## Próximo passo

Leia o guia de [uso responsável](uso-responsavel.md) antes de automatizar consultas recorrentes.
