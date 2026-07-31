# Extração Agregada

A API de extração agregada combina eSAJ, DataJud e DJEN em um envelope versionado.

```python
from esaj_datajud import api

resultado = api.extract_process(
    "1076539-20.2019.8.26.0100",
    sources=("datajud", "djen"),
)

print(resultado["status"])
print(resultado["timeline"])
```

## Envelope

O retorno contém:

- `schema_version`: versão do contrato de extração.
- `package_version`: versão da biblioteca.
- `status`: `ok`, `partial` ou `error`.
- `numero_cnj`: número normalizado.
- `sources`: fontes solicitadas.
- `extracted_at`: data técnica da extração.
- `data`: resultado por fonte.
- `timeline`: registros cronológicos.
- `warnings`: avisos técnicos.
- `errors`: falhas isoladas por fonte.

## Timeline Cronológica

A timeline é apenas uma ordenação temporal dos registros extraídos.

Ela não contém:

- fase;
- risco;
- relevância;
- evento-chave;
- opinião jurídica.

Cada registro preserva:

- `fonte`;
- `tipo_registro`;
- `data`;
- `data_original`;
- `codigo_original`;
- `titulo`;
- `texto`;
- `documentos`;
- `payload_origem`, quando `include_raw=True`.

## CLI

```bash
esaj datajud 1076539-20.2019.8.26.0100 --out datajud.json
esaj extract 1076539-20.2019.8.26.0100 --source datajud --source djen --out extraction.json
esaj timeline 1076539-20.2019.8.26.0100 --source esaj --source djen --out timeline.json
```
