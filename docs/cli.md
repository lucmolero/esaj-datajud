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

## Listar partes

```bash
esaj partes 1076539-20.2019.8.26.0100
```

Imprime as partes classificadas por polo quando a estrutura da página permite.

## Consultar DJEN

```bash
esaj djen 1076539-20.2019.8.26.0100 --out djen.json
```

Salva comunicações encontradas no DJEN/DataJud em JSON.

## Boas práticas

- Evite automações agressivas.
- Salve saídas em ambiente protegido.
- Não publique JSONs reais com dados pessoais em issues ou exemplos.
