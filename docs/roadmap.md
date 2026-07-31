# Roadmap

Este roadmap organiza a evolução do projeto em entregas pequenas, verificáveis e úteis para usuários jurídicos.

## Entregue em 0.2

- Exceções públicas para erros previstos.
- Contratos tipados com `TypedDict`.
- Validação CNJ com dígito verificador.
- Parser ampliado de eSAJ/TJSP.
- DJEN com paginação, retry, backoff e testes sem rede.
- CLI com erros em JSON, inspeção de peças e comando `baixar`.
- Documentação de arquitetura, contratos, erros e fixtures.
- CI com testes, cobertura, lint, formatação, build e validação de metadados.

## Entregue em 0.3

- Cliente configurável `EsajDatajudClient`.
- Configuração pública `EsajDatajudConfig`.
- Timeout padrão aplicado às chamadas HTTP.
- Rate limit simples por sessão.
- Cache JSON local, opt-in e com TTL.
- Pacote marcado como tipado com `py.typed`.
- Checagem `mypy` no CI.
- Site MkDocs Material.
- Workflow de release para tags `v*`.
- Documentos de metodologia, reprodutibilidade, LGPD, modelo de ameaças e governança.
- Arquivo `CITATION.cff` para uso acadêmico e institucional.

## Próximas prioridades

- Publicar pacote no PyPI/TestPyPI.
- Ampliar fixtures sanitizadas com cenários reais de falha do eSAJ.
- Medir cobertura em badge público.
- Publicar GitHub Pages a partir de `mkdocs.yml` quando o plano/configuração do repositório permitir Pages.
- Adicionar pre-commit como check documentado no guia de contribuição.
- Exportar CSV e integração opcional com pandas.
- Adicionar matriz de compatibilidade por tribunal/fonte.
- Aumentar cobertura para 90% com foco em branches críticos do parser.

## Critério de qualidade

Uma funcionalidade só deve ser apresentada como pronta quando tiver:

- contrato documentado;
- teste automatizado;
- exemplo de uso;
- comportamento de erro compreensível;
- limite conhecido declarado.
