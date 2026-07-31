# Erros

Erros previstos usam exceções públicas de `esaj_datajud.exceptions`.

## Exceções

- `FormatoCNJInvalido`: número CNJ mal formatado, fora do escopo TJSP ou com dígito inválido.
- `URLInvalida`: URL fora de `esaj.tjsp.jus.br/cpopg`.
- `ConsultaIndisponivel`: fonte indisponível, HTTP inesperado, timeout ou JSON inválido.
- `ProcessoNaoEncontrado`: a fonte indica ausência de processo ou página sem dados de processo.
- `AcessoRestrito`: captcha, HTTP 403, senha, bloqueio geográfico ou restrição de acesso.
- `DownloadIndisponivel`: falha prevista ao baixar peças públicas candidatas.

## Exemplo

```python
from esaj_datajud import api
from esaj_datajud.exceptions import EsajDatajudError

try:
    extrato = api.get_extrato("0015020-23.2010.8.26.0053")
except EsajDatajudError as exc:
    print(type(exc).__name__, str(exc))
```

## CLI

A CLI imprime erros previstos em JSON e retorna código `2`:

```json
{
  "status": "erro",
  "erro": "FormatoCNJInvalido",
  "mensagem": "Dígito verificador CNJ inválido."
}
```
