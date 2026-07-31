# MCP Local

`esaj-datajud` pode ser usado como servidor MCP local por `stdio`.

Essa camada foi desenhada para clientes MCP que rodam na maquina do usuario. Ela nao hospeda endpoint publico, nao abre porta HTTP e nao muda o contrato principal da biblioteca Python.

## Instalacao

Instale a biblioteca com o extra opcional `mcp`:

```bash
python -m pip install -e ".[mcp]"
```

Para desenvolvimento completo:

```bash
python -m pip install -e ".[dev,mcp]"
```

## Executar

```bash
esaj-datajud-mcp
```

Tambem e possivel executar pelo modulo:

```bash
python -m esaj_datajud.mcp_server
```

O transporte padrao e `stdio`.

## Configuracao em cliente MCP local

Use o Python do ambiente onde o pacote esta instalado.

Exemplo generico:

```json
{
  "mcpServers": {
    "esaj-datajud": {
      "command": "python",
      "args": ["-m", "esaj_datajud.mcp_server"],
      "env": {
        "DATAJUD_API_KEY": "APIKey ..."
      }
    }
  }
}
```

Em ambiente virtual local, use o caminho absoluto do Python da `.venv`.

No Windows:

```json
{
  "mcpServers": {
    "esaj-datajud": {
      "command": "C:\\Users\\luciano.finozzi\\Desktop\\Lib Python - Esaj - Datajud\\.venv\\Scripts\\python.exe",
      "args": ["-m", "esaj_datajud.mcp_server"],
      "env": {
        "DATAJUD_API_KEY": "APIKey ..."
      }
    }
  }
}
```

## Ferramentas

- `server_info`: retorna metadados do servidor MCP local.
- `validar_cnj`: valida e normaliza numero CNJ.
- `extrair_numeros_cnj_de_texto`: extrai numeros CNJ encontrados em texto livre.
- `consultar_esaj`: consulta extrato publico do eSAJ/TJSP.
- `consultar_datajud`: consulta dados processuais estruturados no DataJud/CNJ.
- `consultar_djen`: consulta comunicacoes do DJEN e retorna `count` e `comunicacoes`.
- `extrair_processo`: retorna envelope versionado por fonte.
- `gerar_timeline`: retorna timeline cronologica sem interpretacao juridica.

## Escopo de Seguranca

O servidor MCP local e somente de extracao e normalizacao.

Ele nao:

- baixa pecas automaticamente;
- escreve arquivos;
- publica dados;
- burla autenticacao, captcha, senha ou segredo de justica;
- emite aconselhamento juridico;
- classifica risco, fase ou relevancia juridica.

## DataJud

A API publica do DataJud/CNJ usa chave publica documentada na Wiki oficial do DataJud/CNJ.

A biblioteca inclui a chave publica vigente como fallback. Caso o CNJ rotacione a chave, envie a chave atualizada por argumento da ferramenta ou por variavel de ambiente:

- `ESAJ_DATAJUD_DATAJUD_API_KEY`
- `DATAJUD_API_KEY`
- `CNJ_DATAJUD_API_KEY`

## Arquitetura

O MCP local e uma camada fina sobre a API publica da biblioteca:

```text
cliente MCP local
  -> stdio
  -> esaj_datajud.mcp_server
  -> esaj_datajud.api
  -> eSAJ / DataJud / DJEN
```

Essa separacao mantem o nucleo da biblioteca independente do MCP. Quem usa apenas Python ou CLI nao precisa instalar o SDK MCP.
