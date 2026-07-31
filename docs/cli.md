# CLI

A CLI `esaj` foi criada para consultas rápidas e geração de arquivos JSON sem escrever código Python.

## Ajuda

```bash
esaj --help
```

## Buscar resumo

```bash
esaj search 0015020-23.2010.8.26.0053
```

Imprime um JSON resumido com dados básicos e última movimentação encontrada.

## Gerar extrato

```bash
esaj extrato 0015020-23.2010.8.26.0053 --out extrato.json
```

Salva o extrato completo em um arquivo JSON.

Flags úteis:

- `--inspecionar-pecas`: tenta obter metadados de peças públicas candidatas.
- `--baixar-pecas`: tenta baixar peças públicas candidatas quando tecnicamente possível.
- `--limite-pecas 3`: limita a quantidade de peças baixadas.
- `--salvar-html`: salva HTML bruto da consulta para auditoria local.

## Listar partes

```bash
esaj partes 0015020-23.2010.8.26.0053
```

Imprime as partes classificadas por polo quando a estrutura da página permite.

## Consultar DJEN

```bash
esaj djen 0015020-23.2010.8.26.0053 --data-inicio 2026-01-01 --out djen.json
```

Salva comunicações encontradas no DJEN em JSON.

## Consultar DataJud

```bash
esaj datajud 0015020-23.2010.8.26.0053 --out datajud.json
```

Salva dados processuais estruturados da API pública DataJud/CNJ em JSON.

A biblioteca usa a chave pública vigente documentada na Wiki oficial do DataJud/CNJ como fallback. Use `--api-key` apenas se o CNJ rotacionar a chave ou se você quiser informar outra explicitamente.

## Extração Agregada

```bash
esaj extract 0015020-23.2010.8.26.0053 --source datajud --source djen --out extraction.json
```

Gera envelope versionado por fonte.

## Timeline

```bash
esaj timeline 0015020-23.2010.8.26.0053 --source esaj --source djen --source datajud --out timeline.json
```

Gera timeline cronológica de registros extraídos, sem classificação de fase, risco ou relevância.

## Baixar peças públicas candidatas

```bash
esaj baixar extrato.json --out pecas --limite 3
```

Usa um extrato já gerado para tentar baixar documentos públicos candidatos.

## Erros

Erros previstos são impressos em JSON e retornam código `2`.

## Boas práticas

- Evite automações agressivas.
- Salve saídas em ambiente protegido.
- Não publique JSONs reais com dados pessoais em issues ou exemplos.
