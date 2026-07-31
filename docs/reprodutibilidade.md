# Reprodutibilidade

Reprodutibilidade é essencial em tecnologia jurídica porque dados judiciais mudam ao longo do tempo.

## Ambiente

Recomendação mínima:

```bash
python -m venv .venv
.\.venv\Scripts\python -m pip install -e ".[dev]"
.\.venv\Scripts\python -m pytest --cov
```

Em Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
python -m pytest --cov
```

## Registro de execução

Para rotinas reais, registre:

- versão do pacote;
- número CNJ normalizado;
- data de execução;
- URL final consultada;
- status da consulta;
- quantidade de movimentações e documentos detectados;
- parâmetros de cache, timeout e rate limit.

## Artefatos

Os artefatos de build são gerados com:

```bash
python -m build
python -m twine check dist/*
```

As releases no GitHub são criadas a partir de tags `v*`, com pacote anexado ao release.
