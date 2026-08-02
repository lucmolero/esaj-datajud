# Quickstart

Este guia mostra o caminho mais curto para instalar o projeto e fazer uma consulta básica usando a demonstração pública recomendada: `0015020-23.2010.8.26.0053`.

## Instalar

Para usar o pacote publicado:

```bash
python -m pip install nanojud
```

Para usar tambem o MCP local:

```bash
python -m pip install "nanojud[mcp]"
```

Para contribuir no repositorio clonado:

```bash
python -m pip install -e ".[dev]"
```

## Consultar um processo

```python
from nanojud import api

numero = "0015020-23.2010.8.26.0053"
resumo = api.search_processo(numero)

print(resumo["numero"])
print(resumo["classe"])
print(resumo["ultima_movimentacao"])
```

## Gerar extrato

```python
from nanojud import api

extrato = api.get_extrato("0015020-23.2010.8.26.0053")
print(extrato["dados_basicos"])
print(len(extrato["movimentacoes"]))
```

## Usar cliente configurável

```python
from nanojud import NanoJudClient, NanoJudConfig

client = NanoJudClient(
    NanoJudConfig(
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
from nanojud import api
from nanojud.exceptions import NanoJudError

try:
    extrato = api.get_extrato("0015020-23.2010.8.26.0053")
except NanoJudError as exc:
    print(type(exc).__name__, str(exc))
```

## Consultar pelo terminal

```bash
nanojud search 0015020-23.2010.8.26.0053
nanojud extrato 0015020-23.2010.8.26.0053 --inspecionar-pecas --out extrato.json
```

## Próximo passo

Leia a [Demonstração Pública](demonstracao-publica.md) para entender por que esse processo foi escolhido e consulte o guia de [uso responsável](uso-responsavel.md) antes de automatizar consultas recorrentes.
