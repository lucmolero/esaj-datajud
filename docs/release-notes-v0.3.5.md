# esaj-datajud v0.3.5

Release de robustez baseada em validacao com corpus real privado de eSAJ/TJSP.

## Destaques

- Corrige falso positivo de acesso restrito em paginas publicas que contem o `popupSenha` oculto
  padrao do eSAJ.
- Adiciona teste automatizado para processo publico com popup oculto de senha.
- Adiciona teste `live` opcional para consulta real controlada ao eSAJ/TJSP.
- Documenta criterio de uso de corpus real privado e sanitizacao de fixtures.
- Release workflow passa a usar notas versionadas como corpo do GitHub Release.

## Validacao

- 86 testes automatizados.
- Cobertura acima do gate de 90%.
- Lint, formatacao, type check, build e metadados do pacote validados.
- Corpus privado local com 32 HTMLs reais: 17 processos publicos extraidos, 10.310 movimentacoes,
  42 partes principais, 2.451 partes em tabelas completas e 1.020 documentos classificados.

## Nota de uso responsavel

O projeto continua sem publicar HTMLs, PDFs ou pecas reais no repositorio. Casos reais devem ser
usados apenas como material privado de validacao ou convertidos em fixtures sanitizadas.
