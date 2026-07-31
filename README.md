# esaj-datajud

[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-beta-orange.svg)](#status-do-projeto)
[![CI](https://github.com/lucmolero/esaj-datajud/actions/workflows/ci.yml/badge.svg)](https://github.com/lucmolero/esaj-datajud/actions/workflows/ci.yml)

Biblioteca Python e CLI para consultar, organizar e exportar informações públicas de processos do eSAJ/TJSP e comunicações do DJEN/DataJud.

O objetivo do projeto é oferecer uma base profissional para soluções jurídicas: simples para advogados, previsível para times técnicos e transparente sobre limites, riscos e uso responsável.

## Por que este projeto existe

Advogados e escritórios precisam transformar consultas repetitivas em dados estruturados, sem perder rastreabilidade. `esaj-datajud` nasceu para ser uma camada pequena, auditável e extensível entre fontes públicas judiciais e fluxos internos de análise, relatório e automação.

## Recursos

- API Python de alto nível para scripts, notebooks e integrações.
- CLI para consultas rápidas e geração de JSON.
- Parser organizado para páginas públicas do eSAJ/TJSP, incluindo dados básicos, partes, movimentações, documentos vinculados, audiências, petições, incidentes e apensos.
- Cliente DJEN/DataJud com paginação, retry, backoff e deduplicação.
- Cliente configurável com timeout, rate limit, cache local opcional, logging e sessão injetável.
- Contratos tipados, exceções públicas e testes com fixtures sanitizadas.
- Pacote marcado como tipado (`py.typed`), com checagem `mypy` no CI.
- Foco em uso jurídico responsável, com atenção a LGPD, dados sensíveis e limites das fontes consultadas.

## Instalação

Para desenvolvimento local:

```bash
python -m pip install -e ".[dev]"
```

Para uso direto a partir do repositório:

```bash
python -m pip install -r requirements.txt
python -m pip install -e .
```

## Uso rápido em Python

```python
from esaj_datajud import api

numero = "1076539-20.2019.8.26.0100"

resumo = api.search_processo(numero)
print(resumo["classe"])

extrato = api.get_extrato(numero)
print(extrato["dados_basicos"])

comunicacoes = api.consultar_djen(numero)
print(len(comunicacoes))
```

## Uso profissional com cliente configurável

```python
from esaj_datajud import EsajDatajudClient, EsajDatajudConfig

client = EsajDatajudClient(
    EsajDatajudConfig(
        timeout=20,
        rate_limit_interval=1.0,
        cache_enabled=True,
        cache_ttl_seconds=6 * 60 * 60,
    )
)

resumo = client.search_processo("1076539-20.2019.8.26.0100")
print(resumo["classe"])
```

## CLI

```bash
esaj search 1076539-20.2019.8.26.0100
esaj extrato 1076539-20.2019.8.26.0100 --out extrato.json
esaj partes 1076539-20.2019.8.26.0100
esaj baixar extrato.json --out pecas
esaj djen 1076539-20.2019.8.26.0100 --out djen.json
```

Também é possível executar via módulo:

```bash
python -m esaj_datajud.cli search 1076539-20.2019.8.26.0100
```

## Exemplo de saída

```json
{
  "numero": "1076539-20.2019.8.26.0100",
  "classe": "Ação Civil Pública",
  "assunto": "",
  "foro": "",
  "vara": "",
  "juiz": "",
  "ultima_movimentacao": "Publicação de intimação",
  "ultima_data": "30/07/2026",
  "url": "https://esaj.tjsp.jus.br/cpopg/...",
  "status": "ok",
  "mensagem": "Processo consultado com sucesso"
}
```

## Arquitetura

- `esaj_datajud.api` - camada pública de alto nível, pensada para advogados, escritórios e sistemas.
- `esaj_datajud.client` - cliente configurável para automações, jobs e integrações.
- `esaj_datajud.config` - configuração imutável de timeout, cache, rate limit e User-Agent.
- `esaj_datajud.cache` - cache JSON simples, local e opcional.
- `esaj_datajud.esaj` - montagem de URLs, carregamento HTTP e parsing do eSAJ/TJSP.
- `esaj_datajud.djen` - cliente para comunicações do DJEN/DataJud.
- `esaj_datajud.cli` - interface de linha de comando.
- `esaj_datajud.utils` - normalização de texto, nomes de arquivo e classificação auxiliar.

## Status do projeto

O projeto está em fase beta. A API, a CLI e o cliente configurável já existem, mas algumas capacidades planejadas ainda estão em evolução, especialmente cobertura ampla de cenários reais do eSAJ, exportadores analíticos e documentação publicada como site.

Mesmo em beta, o projeto já possui validação CNJ, exceções públicas, contratos tipados, cache opcional, rate limit, CI, lint, type check, build de pacote e testes sem rede para cenários centrais. O gate mínimo de cobertura é 90%.

Para acompanhar a evolução, consulte [SPECS.md](SPECS.md), [CHANGELOG.md](CHANGELOG.md) e [docs/roadmap.md](docs/roadmap.md).

## Uso responsável

Esta biblioteca deve ser usada apenas para consulta e organização de informações públicas ou legitimamente acessíveis pelo usuário. O projeto não tem como objetivo burlar autenticação, captcha, segredo de justiça, restrições de acesso, limites técnicos dos tribunais ou regras de uso das fontes consultadas.

Leia [docs/uso-responsavel.md](docs/uso-responsavel.md) antes de usar em rotinas de escritório ou automações recorrentes.

## Desenvolvimento

```bash
python -m pip install -e ".[dev]"
python -m pytest --cov
python -m ruff check src tests
python -m ruff format --check src tests
python -m mypy src
```

Testes ao vivo ficam desativados por padrao. Para validar contra o eSAJ/TJSP real:

```bash
$env:ESAJ_DATAJUD_RUN_LIVE = "1"
python -m pytest -m live
```

Antes de abrir um pull request, rode:

```bash
python -m pytest --cov
python -m ruff check src tests
python -m ruff format --check src tests
python -m mypy src
python -m build
python -m twine check dist/*
```

## Documentação

- [Quickstart](docs/quickstart.md)
- [Cliente configurável](docs/client.md)
- [API Reference](docs/api-reference.md)
- [Guia da CLI](docs/cli.md)
- [Contratos de dados](docs/contracts.md)
- [Erros](docs/errors.md)
- [Arquitetura](docs/architecture.md)
- [Metodologia](docs/metodologia.md)
- [Reprodutibilidade](docs/reprodutibilidade.md)
- [LGPD](docs/lgpd.md)
- [Modelo de ameaças](docs/threat-model.md)
- [Fixtures](docs/fixtures.md)
- [Validacao real](docs/validacao-real.md)
- [Uso responsável](docs/uso-responsavel.md)
- [Governança](docs/governanca.md)
- [Roadmap](docs/roadmap.md)
- [Contribuindo](CONTRIBUTING.md)
- [Segurança](SECURITY.md)

## Citação

Para uso acadêmico, técnico ou institucional, cite o projeto pelo arquivo [CITATION.cff](CITATION.cff).

## Autor

Luciano Molero - [LinkedIn](https://www.linkedin.com/in/luciano-molero/)

Projeto criado como base aberta para soluções jurídicas profissionais em Python.
