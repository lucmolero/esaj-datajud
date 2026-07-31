<p align="center">
  <img src="docs/assets/logo.svg" alt="esaj-datajud" width="120" />
</p>

<h1 align="center">esaj-datajud</h1>

<p align="center">
  Toolkit Python para extração responsável, normalização e exportação de dados públicos judiciais do eSAJ/TJSP, DataJud/CNJ e DJEN.
</p>

<p align="center">
  <a href="https://github.com/lucmolero/esaj-datajud/actions/workflows/ci.yml"><img src="https://github.com/lucmolero/esaj-datajud/actions/workflows/ci.yml/badge.svg" alt="CI" /></a>
  <a href="https://github.com/lucmolero/esaj-datajud/actions/workflows/docs.yml"><img src="https://github.com/lucmolero/esaj-datajud/actions/workflows/docs.yml/badge.svg" alt="Docs" /></a>
  <a href="https://github.com/lucmolero/esaj-datajud/actions/workflows/codeql.yml"><img src="https://github.com/lucmolero/esaj-datajud/actions/workflows/codeql.yml/badge.svg" alt="CodeQL" /></a>
  <a href="https://github.com/lucmolero/esaj-datajud/releases"><img src="https://img.shields.io/github/v/release/lucmolero/esaj-datajud" alt="Release" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License: MIT" /></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.10%2B-blue.svg" alt="Python 3.10+" /></a>
</p>

<p align="center">
  <a href="https://lucmolero.github.io/esaj-datajud/">Documentação</a> ·
  <a href="https://github.com/lucmolero/esaj-datajud/releases">Releases</a> ·
  <a href="docs/uso-responsavel.md">Uso responsável</a> ·
  <a href="CHANGELOG.md">Changelog</a>
</p>

`esaj-datajud` oferece uma base profissional para soluções jurídicas: simples para advogados, previsível para times técnicos e transparente sobre limites, riscos e uso responsável.

> Projeto independente: não é um produto oficial do TJSP, CNJ, eSAJ ou DataJud. A biblioteca não burla autenticação, senha, captcha, segredo de justiça ou restrições técnicas das fontes consultadas.

## Por que este projeto existe

Advogados e escritórios precisam transformar consultas repetitivas em dados estruturados, sem perder rastreabilidade. `esaj-datajud` nasceu para ser uma camada pequena, auditável e extensível entre fontes públicas judiciais e fluxos internos de análise, relatório e automação.

O projeto também serve como vitrine técnica de engenharia legaltech: contratos tipados, testes automatizados, documentação de governança, cuidado com LGPD e releases verificáveis.

## Por que confiar

- CI em Python 3.10, 3.11 e 3.12.
- Cobertura automatizada acima de 90%.
- CodeQL, `pip-audit`, lint, type check, build e validação de pacote.
- Testes sem rede com fixtures sanitizadas.
- Testes `live` opcionais contra fonte real, fora do CI por estabilidade.
- Documentação de LGPD, uso responsável, modelo de ameaças, governança e reprodutibilidade.
- Releases versionadas com `wheel`, `sdist` e notas públicas.

## Recursos

- API Python de alto nível para scripts, notebooks e integrações.
- CLI para consultas rápidas e geração de JSON.
- Parser organizado para páginas públicas do eSAJ/TJSP, incluindo dados básicos, partes, movimentações, documentos vinculados, audiências, petições, incidentes e apensos.
- Cliente DataJud/CNJ para dados processuais estruturados, com retry, backoff e normalização.
- Cliente DJEN para comunicações e publicações, com paginação, retry, backoff e deduplicação.
- Cliente configurável com timeout, rate limit, cache local opcional, logging e sessão injetável.
- Servidor MCP local opcional por `stdio` para agentes e clientes compatíveis com MCP.
- Contratos tipados, exceções públicas e testes com fixtures sanitizadas.
- Pacote marcado como tipado (`py.typed`), com checagem `mypy` no CI.
- Foco em uso jurídico responsável, com atenção a LGPD, dados sensíveis e limites das fontes consultadas.

## Casos reais de robustez

O projeto é validado com fixtures sanitizadas e também com corpus privado local, sem publicar HTMLs, PDFs ou peças reais no repositório. A validação mais recente confirmou:

- 17 processos públicos extraídos em corpus privado de 32 HTMLs reais.
- 10.310 movimentações parseadas.
- 42 partes principais e 2.451 partes em tabelas completas.
- 204 documentos públicos candidatos e 816 documentos restritos por senha.
- Cobertura para página pública do eSAJ com `popupSenha` oculto.

## Instalação

Para desenvolvimento local:

```bash
python -m pip install -e ".[dev]"
```

Para usar o servidor MCP local:

```bash
python -m pip install -e ".[mcp]"
esaj-datajud-mcp
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

datajud = api.consultar_datajud(numero)
print(datajud["classe"])
```

A API pública do DataJud/CNJ usa chave pública documentada na Wiki oficial. A biblioteca inclui a chave vigente como fallback; se o CNJ rotacionar a chave, use `DATAJUD_API_KEY` ou passe `api_key` explicitamente.

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
esaj datajud 1076539-20.2019.8.26.0100 --out datajud.json
esaj timeline 1076539-20.2019.8.26.0100 --source esaj --source djen --out timeline.json
```

Também é possível executar via módulo:

```bash
python -m esaj_datajud.cli search 1076539-20.2019.8.26.0100
```

## MCP Local

O projeto inclui um servidor MCP local opcional por `stdio`, pensado para agentes que precisam consultar e estruturar dados judiciais sem expor endpoint público.

```bash
python -m esaj_datajud.mcp_server
```

As ferramentas MCP disponíveis validam CNJ, extraem números CNJ de texto, consultam eSAJ/TJSP, DataJud/CNJ e DJEN, geram envelope versionado e timeline cronológica.

Consulte [docs/mcp-local.md](docs/mcp-local.md) para configuração em clientes MCP.

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
- `esaj_datajud.datajud` - cliente DataJud/CNJ para dados processuais estruturados.
- `esaj_datajud.djen` - cliente para comunicações do DJEN.
- `esaj_datajud.extraction` - envelope versionado de extração por fonte.
- `esaj_datajud.timeline` - timeline cronológica sem interpretação jurídica.
- `esaj_datajud.exports` - exportadores JSON, JSONL, CSV e SQLite.
- `esaj_datajud.mcp_server` - servidor MCP local opcional por `stdio`.
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

Testes ao vivo ficam desativados por padrão. Para validar contra o eSAJ/TJSP real:

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
- [MCP local](docs/mcp-local.md)
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
- [Validação real](docs/validacao-real.md)
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
