# Quickstart

Este guia mostra o caminho mais curto para instalar o projeto e fazer uma consulta básica usando a demonstração pública recomendada: `0015020-23.2010.8.26.0053`.

## Instalar

```bash
python -m pip install -e ".[dev]"
```

## Consultar um processo

```python
from esaj_datajud import api

numero = "0015020-23.2010.8.26.0053"
resumo = api.search_processo(numero)

print(resumo["numero"])
print(resumo["classe"])
print(resumo["ultima_movimentacao"])
```

## Gerar extrato

```python
from esaj_datajud import api

extrato = api.get_extrato("0015020-23.2010.8.26.0053")
print(extrato["dados_basicos"])
print(len(extrato["movimentacoes"]))
```

## Usar cliente configurável

```python
from esaj_datajud import EsajDatajudClient, EsajDatajudConfig

client = EsajDatajudClient(
    EsajDatajudConfig(
        timeout=20,
        rate_limit_interval=1.0,
        cache_enabled=True,
    )
)

resumo = client.search_processo("0015020-23.2010.8.26.0053")
print(resumo["classe"])
```

## Tratar erros previstos

```python
from esaj_datajud import api
from esaj_datajud.exceptions import EsajDatajudError

try:
    extrato = api.get_extrato("0015020-23.2010.8.26.0053")
except EsajDatajudError as exc:
    print(type(exc).__name__, str(exc))
```

## Consultar pelo terminal

```bash
esaj search 0015020-23.2010.8.26.0053
esaj extrato 0015020-23.2010.8.26.0053 --inspecionar-pecas --out extrato.json
```

## Próximo passo

Leia a [Demonstração Pública](demonstracao-publica.md) para entender por que esse processo foi escolhido e consulte o guia de [uso responsável](uso-responsavel.md) antes de automatizar consultas recorrentes.
