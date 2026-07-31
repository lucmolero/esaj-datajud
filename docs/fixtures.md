# Fixtures

Fixtures são amostras HTML ou JSON usadas para testar parsers sem depender de rede.

## Regras

- Remova nomes reais, CPFs, CNPJs, endereços, e-mails e documentos.
- Preserve apenas a estrutura necessária ao teste.
- Nomeie a fixture pelo cenário, não por pessoa ou processo real.
- Não adicione peças, PDFs ou documentos judiciais reais.

## Cenários recomendados

- processo básico encontrado;
- processo não encontrado;
- página com lista de processos;
- movimentação com documento público candidato;
- movimentação com documento restrito por senha;
- tabela de audiências;
- incidentes e apensos;
- DJEN com paginação;
- DJEN com HTTP 429 e retry;
- DJEN com HTTP 403.
