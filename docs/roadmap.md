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

## Próximas prioridades

- Publicar pacote no PyPI/TestPyPI.
- Adicionar documentação visual com site MkDocs Material.
- Ampliar fixtures sanitizadas com cenários reais de falha do eSAJ.
- Medir cobertura em badge público.
- Adicionar pre-commit e guia de desenvolvimento local.
- Implementar cache opcional e rate limit configurável.
- Exportar CSV e integração opcional com pandas.

## Critério de qualidade

Uma funcionalidade só deve ser apresentada como pronta quando tiver:

- contrato documentado;
- teste automatizado;
- exemplo de uso;
- comportamento de erro compreensível;
- limite conhecido declarado.
