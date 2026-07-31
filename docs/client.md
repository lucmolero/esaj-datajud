# Cliente Configurável

O `EsajDatajudClient` é a interface recomendada para automações profissionais, serviços internos, jobs agendados e notebooks que precisam de controle operacional.

## Exemplo

```python
from esaj_datajud import EsajDatajudClient, EsajDatajudConfig

config = EsajDatajudConfig(
    timeout=20,
    rate_limit_interval=1.0,
    cache_enabled=True,
    cache_dir=".esaj_datajud_cache",
    cache_ttl_seconds=6 * 60 * 60,
)

client = EsajDatajudClient(config)
resumo = client.search_processo("1076539-20.2019.8.26.0100")
print(resumo["classe"])
```

## Quando usar

Use o cliente configurável quando precisar de:

- timeout consistente em todas as chamadas;
- intervalo mínimo entre requisições;
- cache local para evitar consultas repetidas;
- `User-Agent` identificável;
- logging para auditoria técnica;
- uma sessão `requests` injetável em testes.

## Cache

O cache é opt-in e gravado em JSON por namespace. Ele não deve ser usado para armazenar dados sensíveis sem política interna de retenção, acesso e descarte.

Recomendação prática:

- deixe o cache desligado em scripts exploratórios;
- ligue cache em rotinas repetidas com TTL curto;
- nunca versione a pasta de cache;
- trate o cache como dado jurídico operacional.

## Rate limit

`rate_limit_interval` define o intervalo mínimo entre requisições da sessão. Ele não substitui leitura de termos de uso, políticas do tribunal, limitação de volume ou avaliação jurídica. É uma proteção técnica básica para reduzir pressão sobre fontes públicas.
