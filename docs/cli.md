# CLI

A CLI `esaj` foi criada para consultas rápidas e geração de arquivos JSON sem escrever código Python.

## Ajuda

```bash
esaj --help
```

## Buscar resumo

```bash
esaj search 1076539-20.2019.8.26.0100
```

Imprime um JSON resumido com dados básicos e última movimentação encontrada.

## Gerar extrato

```bash
esaj extrato 1076539-20.2019.8.26.0100 --out extrato.json
```

Salva o extrato completo em um arquivo JSON.

Flags úteis:

- `--inspecionar-pecas`: tenta obter metadados de peças públicas candidatas.
- `--baixar-pecas`: tenta baixar peças públicas candidatas quando tecnicamente possível.
- `--limite-pecas 3`: limita a quantidade de peças baixadas.
- `--salvar-html`: salva HTML bruto da consulta para auditoria local.

## Listar partes

```bash
esaj partes 1076539-20.2019.8.26.0100
```

Imprime as partes classificadas por polo quando a estrutura da página permite.

## Consultar DJEN

```bash
esaj djen 1076539-20.2019.8.26.0100 --data-inicio 2026-01-01 --out djen.json
```

Salva comunicações encontradas no DJEN/DataJud em JSON.

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
