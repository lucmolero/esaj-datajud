# esaj-datajud v0.4.0

Release de extração multi-fonte.

## Destaques

- DataJud/CNJ passa a ser uma fonte própria para dados processuais estruturados.
- DJEN permanece separado para comunicações, publicações e intimações.
- Novo envelope versionado de extração com resultados por fonte, erros isolados e timeline cronológica.
- Nova timeline técnica sem fase, relevância, risco ou interpretação jurídica.
- Novos exportadores JSON, JSONL, CSV e SQLite.
- Novos comandos CLI: `datajud`, `extract` e `timeline`.
- Documentação nova para fontes e extração agregada.

## Escopo

Esta versão mantém o projeto no campo de extração de dados: coleta, normalização, preservação de fonte e exportação. Não adiciona análise jurídica, classificação de relevância, risco, contingência ou parecer.

## Compatibilidade

A API eSAJ e DJEN existente permanece compatível. As novas APIs são aditivas.
