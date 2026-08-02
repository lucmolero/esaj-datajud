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

- Cliente configurável `NanoJudClient`.
- Configuração pública `NanoJudConfig`.
- Timeout padrão aplicado às chamadas HTTP.
- Rate limit simples por sessão.
- Cache JSON local, opt-in e com TTL.
- Pacote marcado como tipado com `py.typed`.
- Checagem `mypy` no CI.
- Site MkDocs Material.
- GitHub Pages preparado para publicação da documentação.
- CodeQL preparado para upload de resultados em Code Scanning.
- Workflow de release para tags `v*`.
- Documentos de metodologia, reprodutibilidade, LGPD, modelo de ameaças e governança.
- Arquivo `CITATION.cff` para uso acadêmico e institucional.
- Gate mínimo de cobertura elevado para 90%.

## Entregue em 0.4

- Cliente DataJud/CNJ separado do DJEN, com chave pública fallback, retry, backoff e normalização.
- Envelope versionado de extração por fonte.
- Timeline cronológica sem interpretação jurídica.
- Exportadores JSON, JSONL, CSV e SQLite.
- Documentação de fontes, contratos e extração agregada.

## Entregue em 0.5

- Servidor MCP local por `stdio`.
- Extra opcional `mcp`.
- Entry point `nanojud-mcp`.
- Ferramentas MCP somente leitura para validação CNJ, eSAJ, DataJud, DJEN, extração agregada e timeline.
- Testes reais manuais com eSAJ, DataJud, DJEN e MCP local.

## Próximas prioridades

- Publicar pacote no PyPI com Trusted Publishing.
- Ampliar fixtures sanitizadas com cenários reais de falha do eSAJ.
- Medir cobertura em badge público.
- Adicionar matriz de compatibilidade por tribunal/fonte.
- Adicionar testes live opcionais para DataJud, DJEN e MCP local.
- Reduzir gradualmente o `ignore_errors` do `mypy` no parser eSAJ.
- Aumentar cobertura incrementalmente para 95% com foco em branches críticos do parser.

## Critério de qualidade

Uma funcionalidade só deve ser apresentada como pronta quando tiver:

- contrato documentado;
- teste automatizado;
- exemplo de uso;
- comportamento de erro compreensível;
- limite conhecido declarado.
