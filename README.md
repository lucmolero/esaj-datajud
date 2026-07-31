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
- Contratos tipados, exceções públicas e testes com fixtures sanitizadas.
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
- `esaj_datajud.esaj` - montagem de URLs, carregamento HTTP e parsing do eSAJ/TJSP.
- `esaj_datajud.djen` - cliente para comunicações do DJEN/DataJud.
- `esaj_datajud.cli` - interface de linha de comando.
- `esaj_datajud.utils` - normalização de texto, nomes de arquivo e classificação auxiliar.

## Status do projeto

O projeto está em fase beta. A API e a CLI já existem, mas algumas capacidades planejadas ainda estão em evolução, especialmente download de peças, parsing avançado de documentos, cache e cobertura ampla de cenários reais do eSAJ.

Mesmo em beta, o projeto já possui validação CNJ, exceções públicas, contratos tipados, CI, lint, build de pacote e testes sem rede para cenários centrais.

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
```

Antes de abrir um pull request, rode:

```bash
python -m pytest --cov
python -m ruff check src tests
python -m ruff format --check src tests
python -m build
python -m twine check dist/*
```

## Documentação

- [Quickstart](docs/quickstart.md)
- [API Reference](docs/api-reference.md)
- [Guia da CLI](docs/cli.md)
- [Contratos de dados](docs/contracts.md)
- [Erros](docs/errors.md)
- [Arquitetura](docs/architecture.md)
- [Fixtures](docs/fixtures.md)
- [Uso responsável](docs/uso-responsavel.md)
- [Roadmap](docs/roadmap.md)
- [Contribuindo](CONTRIBUTING.md)
- [Segurança](SECURITY.md)

## Autor

Luciano Molero - [LinkedIn](https://www.linkedin.com/in/luciano-molero/)

Projeto criado como base aberta para soluções jurídicas profissionais em Python.
