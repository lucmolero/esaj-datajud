# esaj-datajud v0.3.2

Release final de preparação pública do projeto, focada em sinais de confiança para GitHub, documentação viva e qualidade mensurável.

## Destaques

- `SPECS.md` atualizado para refletir a arquitetura real do pacote.
- Templates profissionais para issues e pull requests.
- Workflow manual de publicação PyPI com Trusted Publishing.
- GitHub Actions atualizados para versões mais recentes apontadas pelo Dependabot.
- Cobertura elevada para 91,15%.
- Gate mínimo de cobertura elevado para 90%.

## Validação

- Testes: `85 passed`.
- Cobertura: `91.15%`.
- `ruff check`: aprovado.
- `ruff format --check`: aprovado.
- `mypy src`: aprovado.
- `mkdocs build --strict`: aprovado.
- `python -m build`: aprovado.
- `twine check`: aprovado.

## Limites conhecidos

- O repositório ainda precisa ser tornado público manualmente quando você decidir abrir.
- GitHub Pages depende do plano/configuração do repositório.
- Upload CodeQL para Code Scanning depende da feature estar habilitada.
- Publicação efetiva no PyPI requer criar/configurar o projeto `esaj-datajud` no PyPI com Trusted Publisher.
