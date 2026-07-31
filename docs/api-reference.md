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

Consulta comunicações do DJEN para o número CNJ informado.

## `api.consultar_datajud(numero, api_key=None, include_raw=False)`

Consulta dados processuais estruturados na API pública DataJud/CNJ.

## `api.extract_process(numero, sources=("esaj", "datajud", "djen"), include_raw=False, datajud_api_key=None, djen_data_inicio="")`

Extrai dados das fontes solicitadas em envelope versionado, preservando resultado, erros e timeline cronológica.

## `api.create_client(config=None)`

Cria um `EsajDatajudClient` configurável para automações profissionais.

```python
from esaj_datajud import api, EsajDatajudConfig

client = api.create_client(
    EsajDatajudConfig(timeout=20, rate_limit_interval=1.0, cache_enabled=True)
)
```

## `EsajDatajudClient`

Métodos principais:

- `search_processo(numero)`: retorna resumo estruturado.
- `get_extrato(numero, ...)`: retorna extrato completo.
- `get_partes(numero)`: retorna partes classificadas.
- `consultar_datajud(numero, ...)`: consulta dados processuais DataJud/CNJ.
- `consultar_djen(numero, data_inicio="")`: consulta comunicações DJEN.
- `extract_process(numero, ...)`: retorna envelope de extração por fonte.
- `baixar_pecas(extrato, destino, sobrescrever=False, limite=0)`: baixa peças públicas candidatas.

## `EsajDatajudConfig`

Campos principais:

- `timeout`: timeout padrão das requisições HTTP.
- `rate_limit_interval`: intervalo mínimo entre requisições da mesma sessão.
- `cache_enabled`: habilita cache JSON local.
- `cache_dir`: diretório de cache.
- `cache_ttl_seconds`: tempo de vida do cache.
- `salvar_html`: salva HTML bruto quando suportado pelo fluxo.
- `datajud_api_key`: API key do DataJud/CNJ para clientes configuráveis.
- `user_agent`: modelo de `User-Agent` com suporte a `{version}`.
