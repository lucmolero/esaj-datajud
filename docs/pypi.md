# PyPI e MCP

Esta pagina define o modelo oficial de distribuicao do NanoJud no PyPI.

## Pacotes publicados

O projeto publica um unico pacote:

```text
nanojud
```

Esse pacote entrega tres formas de uso:

- biblioteca Python: `import nanojud`;
- CLI: `nanojud`;
- servidor MCP local opcional: `nanojud-mcp`.

## Instalacao para usuarios

Biblioteca e CLI:

```bash
python -m pip install nanojud
```

Biblioteca, CLI e MCP:

```bash
python -m pip install "nanojud[mcp]"
```

Validacao:

```bash
python -c "import nanojud; print(nanojud.__version__)"
nanojud --help
nanojud-mcp
```

## MCP direto com uvx

Para agentes e clientes MCP, o caminho mais simples e executar o servidor direto do pacote publicado:

```bash
uvx --from "nanojud[mcp]" nanojud-mcp
```

Configuracao MCP:

```json
{
  "mcpServers": {
    "nanojud": {
      "command": "uvx",
      "args": ["--from", "nanojud[mcp]", "nanojud-mcp"]
    }
  }
}
```

Esse modelo evita clonar repositorio para uso comum. Clone local fica reservado para contribuicao, auditoria ou desenvolvimento.

## Publicacao por Trusted Publishing

O fluxo recomendado e Trusted Publishing via GitHub Actions/OIDC. Isso evita salvar token longo do PyPI no GitHub.

Configuracao no PyPI:

- Project name: `nanojud`
- Owner: `lucmolero`
- Repository: `nanojud`
- Workflow filename: `publish-pypi.yml`
- Environment name: `pypi`

Configuracao no TestPyPI:

- Project name: `nanojud`
- Owner: `lucmolero`
- Repository: `nanojud`
- Workflow filename: `publish-testpypi.yml`
- Environment name: `testpypi`

## Ordem de release

1. Atualizar versao em `pyproject.toml` e `src/nanojud/version.py`.
2. Atualizar `CHANGELOG.md` e release notes.
3. Rodar os checks locais:

```bash
python -m pytest --cov
python -m ruff check src tests
python -m ruff format --check src tests
python -m mypy src
python -m build
python -m twine check dist/*
```

4. Publicar primeiro no TestPyPI pelo workflow `Publish TestPyPI`.
5. Testar instalacao isolada:

```bash
python -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ "nanojud[mcp]"
```

6. Publicar no PyPI pelo workflow `Publish PyPI`.
7. Testar instalacao final:

```bash
python -m pip install "nanojud[mcp]"
nanojud --help
nanojud-mcp
```

## Observacoes importantes

- Uma versao publicada no PyPI nao pode ser sobrescrita.
- Se um upload falhar depois de criar a versao, incremente a versao antes de tentar novamente.
- O MCP nao e outro pacote separado nesta fase; ele e um extra opcional do pacote `nanojud`.
- O servidor MCP local usa `stdio`, nao abre porta HTTP e nao hospeda dados em nuvem.
