# Arquitetura

`esaj-datajud` é organizado em camadas pequenas para separar experiência pública, parsing, clientes HTTP e utilidades de domínio jurídico.

## Camadas

- `esaj_datajud.api`: fachada pública para scripts, notebooks, CLIs e integrações.
- `esaj_datajud.esaj`: cliente e parser do eSAJ/TJSP.
- `esaj_datajud.djen`: cliente do DJEN/DataJud.
- `esaj_datajud.models`: contratos tipados dos retornos.
- `esaj_datajud.exceptions`: exceções públicas e previsíveis.
- `esaj_datajud.utils`: normalização de texto, CNJ e classificação auxiliar.
- `esaj_datajud.cli`: interface de linha de comando.

## Princípios

- Testes não devem depender de rede.
- Fixtures devem ser sanitizadas.
- Erros previsíveis devem usar exceções próprias.
- A API pública deve preservar contratos estáveis.
- Funcionalidades sensíveis, como download de peças, devem respeitar restrições técnicas e jurídicas.

## Fluxo eSAJ

1. Valida e normaliza CNJ.
2. Monta URL pública de busca.
3. Abre sessão HTTP com cabeçalhos conservadores.
4. Segue lista de resultados quando necessário.
5. Detecta captcha, senha, restrição ou processo não encontrado.
6. Extrai dados básicos, partes, movimentações, documentos e tabelas complementares.
7. Retorna dicionário estruturado com `status`, `mensagem`, `origem` e dados do processo.

## Fluxo DJEN

1. Consulta endpoint público do DJEN/DataJud por número CNJ.
2. Pagina resultados até `max_pages`.
3. Aplica retry/backoff para falhas transitórias e HTTP 429.
4. Deduplica comunicações por `id`.
5. Normaliza datas e campos de saída.
