# Especificações do Projeto `esaj-datajud`

## Visão

`esaj-datajud` é uma biblioteca Python e CLI para consultar, estruturar e exportar informações públicas de processos do eSAJ/TJSP e comunicações do DJEN/DataJud.

O projeto foi desenhado para servir como base aberta, auditável e profissional para tecnologia jurídica, equilibrando três mundos:

- advocacia, com uso simples e linguagem compreensível;
- academia, com metodologia, rastreabilidade e reprodutibilidade;
- ambiente corporativo, com contratos, testes, governança, segurança e automação de qualidade.

## Escopo

O projeto oferece:

- API Python de alto nível;
- CLI `esaj`;
- parser eSAJ/TJSP para dados básicos, partes, movimentações, documentos, audiências, petições, incidentes e apensos;
- cliente DJEN/DataJud com paginação, retry, backoff e deduplicação;
- cliente configurável com timeout, rate limit, cache local opcional, logging e sessão injetável;
- contratos tipados com `TypedDict`;
- pacote marcado como tipado com `py.typed`;
- testes sem rede com fixtures sanitizadas;
- documentação de arquitetura, contratos, erros, LGPD, metodologia, reprodutibilidade, governança e modelo de ameaças.

## Fora de Escopo

O projeto não fornece e não deve fornecer:

- bypass de captcha;
- automação de login;
- acesso a processos sigilosos;
- contorno de senha, autenticação ou restrição técnica;
- coleta massiva sem finalidade, rate limit e avaliação jurídica;
- aconselhamento jurídico automatizado.

## Público-Alvo

- Advogados e escritórios que precisam estruturar consultas públicas recorrentes.
- Desenvolvedores de legaltech e lawtech.
- Pesquisadores que precisam de dados rastreáveis e metodologia clara.
- Times corporativos que exigem previsibilidade, logs, testes e governança.

## Estrutura Atual

```text
src/esaj_datajud/
├── __init__.py
├── api.py
├── cache.py
├── cli.py
├── client.py
├── config.py
├── djen.py
├── esaj.py
├── exceptions.py
├── models.py
├── py.typed
├── utils.py
└── version.py
```

## Camadas

### `esaj_datajud.api`

Fachada pública simples para scripts, notebooks, CLI e integrações:

- `search_processo(numero)`
- `get_extrato(numero, ...)`
- `get_partes(numero)`
- `baixar_pecas(extrato, destino, ...)`
- `resumo_rapido(numero)`
- `consultar_djen(numero, data_inicio="")`
- `create_client(config=None)`

### `esaj_datajud.client`

Cliente configurável para uso profissional:

- `EsajDatajudClient`
- `RateLimitedSession`

Responsabilidades:

- aplicar timeout padrão;
- aplicar intervalo mínimo entre requisições;
- controlar cache local opt-in;
- permitir logging;
- permitir injeção de sessão em testes.

### `esaj_datajud.config`

Configuração imutável:

- `timeout`
- `rate_limit_interval`
- `cache_enabled`
- `cache_dir`
- `cache_ttl_seconds`
- `salvar_html`
- `user_agent`

### `esaj_datajud.cache`

Cache JSON local por namespace, com TTL.

O cache é desativado por padrão e deve ser tratado como dado jurídico operacional quando ligado.

### `esaj_datajud.esaj`

Cliente/parser eSAJ/TJSP:

- valida e normaliza CNJ;
- monta URL de consulta;
- carrega página pública;
- detecta captcha, senha, indisponibilidade e processo não encontrado;
- extrai dados básicos, partes, movimentações e documentos;
- identifica documentos públicos candidatos e restritos por senha;
- inspeciona metadados da pasta digital quando solicitado;
- baixa peças públicas candidatas quando tecnicamente possível.

### `esaj_datajud.djen`

Cliente DJEN/DataJud:

- consulta por número CNJ;
- pagina resultados;
- aplica retry/backoff;
- deduplica por `id`;
- normaliza datas.

### `esaj_datajud.cli`

Interface de linha de comando:

- `esaj search <numero>`
- `esaj extrato <numero> --out extrato.json`
- `esaj partes <numero>`
- `esaj baixar <extrato.json> --out pecas`
- `esaj djen <numero> --out djen.json`

## Contratos

Os retornos públicos são documentados em `docs/contracts.md` e tipados em `esaj_datajud.models`.

Contratos principais:

- `ResumoProcesso`
- `Extrato`
- `DadosBasicos`
- `Partes`
- `Movimentacao`
- `Documento`
- `Documentos`

## Exceções Públicas

Erros previsíveis devem usar exceções próprias de `esaj_datajud.exceptions`:

- `EsajDatajudError`
- `FormatoCNJInvalido`
- `URLInvalida`
- `AcessoRestrito`
- `ConsultaIndisponivel`
- `ProcessoNaoEncontrado`
- `DownloadIndisponivel`

## Qualidade

O projeto deve manter:

- testes sem rede;
- fixtures sanitizadas;
- `ruff check`;
- `ruff format --check`;
- `mypy src`;
- `pytest --cov`;
- build de pacote;
- `twine check`;
- auditoria de dependências com `pip-audit`;
- CI em múltiplas versões de Python.

## Critérios de Aceitação

Uma funcionalidade só deve ser considerada pronta quando tiver:

- contrato público definido ou documentado;
- teste automatizado;
- comportamento de erro previsível;
- documentação ou exemplo;
- limite conhecido declarado;
- respeito a LGPD, termos das fontes e uso responsável.

## Roadmap de Maturidade

Prioridades para evolução pública:

- publicar no PyPI com Trusted Publishing;
- elevar cobertura para 90%+;
- habilitar GitHub Pages quando o plano/configuração permitir;
- habilitar upload CodeQL para Code Scanning quando a feature estiver disponível;
- ampliar fixtures reais sanitizadas;
- criar exportadores CSV/pandas opcionais;
- publicar matriz de compatibilidade por fonte/tribunal.
