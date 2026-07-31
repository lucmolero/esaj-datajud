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

## Corpus real privado

Use corpus real apenas como referencia privada. Quando um caso real revelar um bug, reduza o HTML
ao menor trecho sanitizado que reproduz o problema.

Cenarios adicionais obrigatorios:

- processo publico com `popupSenha` oculto;
- processo realmente restrito sem `numeroProcesso` publico;
- processo com muitas movimentacoes;
- processo com muitas partes;
- execucao fiscal;
- falencia ou recuperacao judicial.

Para validacoes com fonte real e corpus privado, veja [Validacao Real](validacao-real.md).
