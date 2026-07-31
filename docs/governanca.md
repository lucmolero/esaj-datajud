# Governança

`esaj-datajud` segue uma governança simples, adequada a uma biblioteca aberta em evolução.

## Manutenção

O mantenedor principal é Luciano Molero (`lucmolero`). Mudanças relevantes devem preservar:

- compatibilidade razoável da API pública;
- documentação do comportamento;
- testes sem rede;
- respeito a dados pessoais e fontes públicas;
- histórico claro em `CHANGELOG.md`.

## Versionamento

O projeto usa versionamento semântico sempre que possível:

- `PATCH`: correções sem mudança de contrato;
- `MINOR`: novas funcionalidades compatíveis;
- `MAJOR`: mudanças incompatíveis na API pública.

## Pull requests

Um pull request profissional deve incluir:

- descrição objetiva do problema;
- teste automatizado quando houver mudança de comportamento;
- atualização de documentação quando o contrato público mudar;
- fixture sanitizada quando o parser for afetado.

## Decisões técnicas

Decisões importantes devem favorecer clareza, auditabilidade e manutenção. Em caso de dúvida, prefira uma API menor, mais previsível e bem documentada.
