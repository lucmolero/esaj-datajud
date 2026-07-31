# Validacao Real

Este projeto deve evoluir com testes offline e validacoes reais controladas.

## Corpus privado

HTMLs, PDFs e saidas reais de processos sao uteis para validar robustez, mas nao devem ser
publicados no repositorio sem curadoria. Antes de transformar um caso real em fixture publica:

- remova nomes, documentos, enderecos, e-mails, dados bancarios e identificadores sensiveis;
- reduza o HTML ao menor trecho que reproduz o comportamento;
- preserve seletores, IDs, classes e estrutura necessarios ao parser;
- troque numeros reais por exemplos sintaticamente validos quando o numero nao for essencial;
- nunca publique pecas processuais reais, mesmo quando o processo for publico.

## Cenarios obrigatorios

O corpus de regressao deve cobrir:

- processo publico com `popupSenha` oculto;
- processo realmente restrito, sem `numeroProcesso` publico;
- processo nao encontrado;
- pagina de lista de processos antes do detalhe;
- processo com muitas movimentacoes;
- processo com muitas partes;
- execucao fiscal;
- falencia ou recuperacao judicial;
- documentos publicos candidatos;
- documentos restritos por senha.

## Testes ao vivo

Testes ao vivo consultam fontes externas e podem falhar por rede, indisponibilidade, bloqueio
temporario, captcha ou mudanca da fonte. Por isso ficam fora do fluxo padrao.

Para rodar:

```bash
$env:ESAJ_DATAJUD_RUN_LIVE = "1"
python -m pytest -m live
```

Em Linux/macOS:

```bash
ESAJ_DATAJUD_RUN_LIVE=1 python -m pytest -m live
```

Use poucos processos, intervalos conservadores e nunca baixe pecas em testes automatizados sem
autorizacao explicita.

## Evidencia atual

A validacao de 31 de julho de 2026 usou um corpus privado local com 32 HTMLs reais de eSAJ/TJSP.
Sem publicar esses arquivos, o projeto confirmou:

- 17 processos publicos extraidos com sucesso;
- 10.310 movimentacoes parseadas;
- 42 partes principais;
- 2.451 partes em tabelas completas;
- 204 documentos publicos candidatos;
- 816 documentos restritos por senha.

As falhas restantes foram paginas realmente restritas ou nao encontradas, que devem continuar
retornando excecoes controladas.
