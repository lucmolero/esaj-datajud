# API Reference

## `api.search_processo(numero)`

Consulta o eSAJ/TJSP e retorna um resumo estruturado.

## `api.get_extrato(numero, baixar_pecas=False, limite_pecas=3, *, inspecionar_pecas=False, limite_inspecao_pecas=10, salvar_html=False)`

Monta o extrato completo do processo.

Parâmetros:

- `numero`: número CNJ TJSP.
- `baixar_pecas`: tenta baixar peças públicas candidatas.
- `limite_pecas`: limite de peças para download.
- `inspecionar_pecas`: busca metadados da pasta digital para documentos candidatos.
- `limite_inspecao_pecas`: limite de inspeções.
- `salvar_html`: salva HTML bruto da consulta em `esaj_raw/tjsp/cpopg`.

## `api.get_partes(numero)`

Retorna partes classificadas por polo quando a estrutura da página permite.

## `api.baixar_pecas(extrato, destino, sobrescrever=False, limite=0)`

Baixa documentos públicos candidatos presentes em um extrato.

## `api.resumo_rapido(numero)`

Retorna texto curto para triagem, briefing ou e-mail.

## `api.consultar_djen(numero, data_inicio="")`

Consulta comunicações do DJEN/DataJud para o número CNJ informado.
