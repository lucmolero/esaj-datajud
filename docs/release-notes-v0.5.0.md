# Release v0.5.0

Esta release adiciona o primeiro servidor MCP local do projeto.

## Destaques

- Servidor MCP local por `stdio` em `nanojud.mcp_server`.
- Entrypoint `nanojud-mcp`.
- Extra opcional `mcp` para instalar o SDK MCP apenas quando necessario.
- Ferramentas MCP somente leitura para extracao, normalizacao e timeline.
- Chave publica vigente do DataJud/CNJ como fallback documentado, com override por variavel de ambiente ou argumento.
- Documentacao de configuracao local para clientes MCP.

## Ferramentas MCP

- `server_info`
- `validar_cnj`
- `extrair_numeros_cnj_de_texto`
- `consultar_esaj`
- `consultar_datajud`
- `consultar_djen`
- `extrair_processo`
- `gerar_timeline`

## Escopo

O MCP desta versao e local. Ele nao implementa hospedagem HTTPS, autenticacao remota, multiusuario ou deploy em nuvem.

A decisao foi manter a primeira entrega MCP simples, auditavel e segura para uso em clientes locais.

## Validacao

Esta release preserva a arquitetura principal da biblioteca e adiciona testes sem rede para garantir registro e delegacao das ferramentas MCP.
