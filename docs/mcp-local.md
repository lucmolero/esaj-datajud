# MCP Local

`esaj-datajud` pode ser usado como servidor MCP local por `stdio`.

Essa camada foi desenhada para clientes MCP que rodam na maquina do usuario. Ela nao hospeda endpoint publico, nao abre porta HTTP e nao muda o contrato principal da biblioteca Python.

Para advogados, a lógica é simples: o agente de IA chama ferramentas locais para consultar fontes públicas, e o resultado volta estruturado com fonte, data e limites. A análise jurídica continua sendo humana.

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

## Jornada com Claude Code, Codex, Gemini ou cliente MCP

1. Instale `esaj-datajud` com o extra `mcp`.
2. Configure o cliente MCP apontando para `python -m esaj_datajud.mcp_server`.
3. Peça ao agente para validar o CNJ antes de consultar.
4. Solicite respostas com separação entre fatos extraídos e hipóteses.
5. Valide atos sensíveis na fonte oficial.

Prompt sugerido:

```text
Use o MCP local esaj-datajud para consultar 0015020-23.2010.8.26.0053.
Primeiro valide o CNJ. Depois consulte as fontes públicas disponíveis.
Entregue dados básicos, últimas movimentações e timeline.
Não invente teses e não dê aconselhamento jurídico.
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

Para uma instalação guiada por agente, veja [Instalação Com IA](instalacao-com-ia.md).
