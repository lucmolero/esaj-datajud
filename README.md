<p align="center">
  <img src="docs/assets/esaj-datajud-logo-primary.svg" alt="Marca esaj-datajud" width="220" />
</p>

<h1 align="center">esaj-datajud</h1>

<p align="center" style="max-width: 780px; margin: 0 auto 1rem; font-size: 1.05rem; color: #dce8ff;">
  Repositório central para buscar dados processuais, jurisprudência e contexto público do Brasil com uma camada de IA para advogados, desenvolvedores e pesquisadores.
</p>

<div align="center" style="margin: 0 0 1.2rem;">
  <div style="display: inline-block; padding: 0.7rem 1rem; border: 1px solid #244b6a; border-radius: 999px; background: linear-gradient(90deg, rgba(93,211,176,0.16), rgba(244,201,93,0.12)); color: #f6f9ff; font-size: 0.95rem; font-weight: 600;">
    Busca processual • Jurisprudência • IA local • Dados públicos brasileiros
  </div>
</div>

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

`esaj-datajud` oferece uma base profissional para soluções jurídicas: simples para advogados, previsível para times técnicos e transparente sobre limites, riscos e uso responsável. O foco é transformar fontes públicas judiciais em dados estruturados, timelines e integrações locais para automação com agentes de IA.

> Projeto independente: não é um produto oficial do TJSP, CNJ, eSAJ ou DataJud. A biblioteca não burla autenticação, senha, captcha, segredo de justiça ou restrições técnicas das fontes consultadas.

## Por que este projeto existe

Advogados e escritórios precisam transformar consultas repetitivas em dados estruturados, sem perder rastreabilidade. `esaj-datajud` nasceu para ser uma camada pequena, auditável e extensível entre fontes públicas judiciais e fluxos internos de análise, relatório e automação.

O projeto também serve como vitrine técnica de engenharia legaltech: contratos tipados, testes automatizados, documentação de governança, cuidado com LGPD e releases verificáveis.

## Por que confiar

- CI em Python 3.10, 3.11, 3.12 e 3.13.
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
- Leitura best-effort de documentos públicos candidatos em memória, sem salvar PDF em disco.
- Contratos tipados, exceções públicas e testes com fixtures sanitizadas.
- Pacote marcado como tipado (`py.typed`), com checagem `mypy` no CI.
- Foco em uso jurídico responsável, com atenção a LGPD, dados sensíveis e limites das fontes consultadas.

## Para advogados e agentes de IA

Este projeto foi pensado para ser usado de forma simples, inclusive por quem não conhece programação.

O fluxo recomendado é este:

1. Você escolhe um número CNJ público.
2. A IA ou alguém com acesso ao computador usa uma forma simples de instalar o projeto.
3. O ambiente é preparado com poucos comandos.
4. O sistema consulta o processo e entrega um resultado organizado.

### Caminho simples para advogados

Se você não usa GitHub nem sabe o que é `git clone`, a alternativa mais simples é:

1. abrir a página do repositório no GitHub;
2. clicar em "Code" e depois em "Download ZIP";
3. extrair a pasta em qualquer local do computador;
4. abrir o terminal dentro dessa pasta e seguir os comandos abaixo.

Esse caminho é suficiente para usar a biblioteca, o CLI e o MCP local sem precisar entender Git.

### Passo 1: baixar o repositório

No computador, abra o terminal e execute:

```bash
git clone https://github.com/lucmolero/esaj-datajud.git
cd esaj-datajud
```

Se não tiver `git`, a IA pode baixar o projeto como arquivo ZIP pelo GitHub e extrair na pasta desejada.

### Passo 2: preparar o ambiente

No Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[mcp]"
```

No Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[mcp]"
```

### Passo 3: usar o projeto

Depois da instalação, você pode usar o comando simples abaixo para iniciar o servidor MCP:

```bash
esaj-datajud-mcp
```

Ou, se preferir, usar a CLI diretamente:

```bash
esaj search 0015020-23.2010.8.26.0053
```

### Passo 4: consultar um processo

Use um número CNJ público, por exemplo:

```text
0015020-23.2010.8.26.0053
```

Se a pessoa estiver usando uma IA, ela pode seguir exatamente este roteiro sem precisar entender o código. Veja a jornada guiada em [docs/instalacao-com-ia.md](docs/instalacao-com-ia.md) e a visão jurídica em [docs/para-advogados.md](docs/para-advogados.md).

## Demonstração pública recomendada

Para demonstrações, tutoriais e vídeos, o projeto usa um processo público institucional previamente testado pelo MCP local:

```text
0015020-23.2010.8.26.0053
```

Trata-se de um Mandado de Segurança Cível envolvendo sindicato e Administração Pública estadual. Em validação manual realizada em 31/07/2026, o MCP retornou dados do eSAJ/TJSP, DJEN e DataJud/CNJ, com timeline agregada e sem erros. A demonstração completa está em [docs/demonstracao-publica.md](docs/demonstracao-publica.md).

## Casos reais de robustez

O projeto é validado com fixtures sanitizadas e também com corpus privado local, sem publicar HTMLs, PDFs, peças reais ou estudos de caso empresariais identificáveis no repositório. A validação mais recente confirmou:

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

numero = "0015020-23.2010.8.26.0053"  # demo pública institucional

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

resumo = client.search_processo("0015020-23.2010.8.26.0053")
print(resumo["classe"])
```

## CLI

```bash
esaj search 0015020-23.2010.8.26.0053
esaj extrato 0015020-23.2010.8.26.0053 --out extrato.json
esaj partes 0015020-23.2010.8.26.0053
esaj baixar extrato.json --out pecas
esaj ler-pecas extrato.json --limite 3 --out pecas_texto.json
esaj djen 0015020-23.2010.8.26.0053 --out djen.json
esaj datajud 0015020-23.2010.8.26.0053 --out datajud.json
esaj timeline 0015020-23.2010.8.26.0053 --source esaj --source djen --source datajud --recent-first --limit 20 --out timeline.json
```

Também é possível executar via módulo:

```bash
python -m esaj_datajud.cli search 0015020-23.2010.8.26.0053
```

## MCP Local

O projeto inclui um servidor MCP local opcional por `stdio`, pensado para agentes que precisam consultar e estruturar dados judiciais sem expor endpoint público.

```bash
python -m esaj_datajud.mcp_server
```

As ferramentas MCP disponíveis validam CNJ, extraem números CNJ de texto, consultam eSAJ/TJSP, DataJud/CNJ e DJEN, geram envelope versionado, timeline cronológica e leitura em memória de documentos públicos candidatos quando tecnicamente possível.

Sobre PDFs: a ferramenta `ler_documentos_publicos` não salva arquivos em disco. Quando a fonte retorna PDF público, os bytes são processados em memória e o texto é extraído com `pypdf`. Documentos com senha, captcha, sigilo ou restrição de acesso continuam fora do escopo.

Consulte [docs/mcp-local.md](docs/mcp-local.md) para configuração em clientes MCP.

## Exemplo de saída

```json
{
  "numero": "0015020-23.2010.8.26.0053",
  "classe": "Mandado de Segurança Cível",
  "assunto": "Organização Político-administrativa / Administração Pública",
  "foro": "Foro Central - Fazenda Pública/Acidentes",
  "vara": "7ª Vara de Fazenda Pública",
  "ultima_movimentacao": "Extinta a Execução/Cumprimento da Sentença pela Satisfação da Obrigação",
  "ultima_data": "2026-07-19",
  "url": "https://esaj.tjsp.jus.br/cpopg/...",
  "status": "ok",
  "mensagem": "Processo consultado com sucesso"
}
```

Em demonstrações públicas, mantenha outputs reduzidos e sanitize dados pessoais, nomes de advogados, documentos e trechos extensos. Para casos de clientes, use apenas processos escolhidos pelo próprio usuário.

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
- [Instalação com IA](docs/instalacao-com-ia.md)
- [Para advogados](docs/para-advogados.md)
- [Demonstração pública](docs/demonstracao-publica.md)
- [Aprendizados MCP](docs/aprendizados-mcp.md)
- [Exemplos seguros](docs/exemplos-seguros.md)
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

Luciano Molero (`lucmolero`) - [LinkedIn](https://www.linkedin.com/in/luciano-molero/)

Luciano atua na intersecção entre Direito, tecnologia e automação jurídica. O projeto reflete essa combinação: rigor jurídico, engenharia reprodutível, experiência de usuário e responsabilidade no uso de dados públicos.
