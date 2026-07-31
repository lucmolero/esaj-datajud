# esaj-datajud v0.3.5

Release de robustez baseada em validação com corpus real privado de eSAJ/TJSP.

## Destaques

- Corrige falso positivo de acesso restrito em páginas públicas que contêm o `popupSenha` oculto
  padrão do eSAJ.
- Adiciona teste automatizado para processo público com popup oculto de senha.
- Adiciona teste `live` opcional para consulta real controlada ao eSAJ/TJSP.
- Documenta criterio de uso de corpus real privado e sanitizacao de fixtures.
- Release workflow passa a usar notas versionadas como corpo do GitHub Release.

## Validação

- 86 testes automatizados.
- Cobertura acima do gate de 90%.
- Lint, formatacao, type check, build e metadados do pacote validados.
- Corpus privado local com 32 HTMLs reais: 17 processos públicos extraídos, 10.310 movimentações,
  42 partes principais, 2.451 partes em tabelas completas e 1.020 documentos classificados.

## Nota de uso responsavel

O projeto continua sem publicar HTMLs, PDFs ou peças reais no repositório. Casos reais devem ser
usados apenas como material privado de validação ou convertidos em fixtures sanitizadas.
