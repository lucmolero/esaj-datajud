# Instalação Com IA

Este guia foi escrito para quem quer instalar e usar `nanojud` com ajuda de um agente de IA local, como Claude Code, Codex, Gemini CLI ou outro cliente compatível com MCP.

O objetivo é simples: o advogado descreve o resultado esperado, e o agente executa a instalação, valida o ambiente e configura o MCP local sem expor dados em endpoint público.

## Quando usar

Use esta jornada quando você quer:

- consultar um número CNJ público;
- gerar JSON, extrato ou timeline;
- conectar a biblioteca a um agente local;
- manter a consulta no computador do usuário;
- preservar rastreabilidade das fontes consultadas.

## Fluxo recomendado para IA e advogados sem programação

Se o usuário não sabe codar, a IA deve assumir o papel operacional. O fluxo ideal é:

1. Baixar o repositório inteiro do GitHub, não parar na primeira página.
2. Se o usuário não tem GitHub nem sabe usar `git clone`, a IA pode baixar o projeto como ZIP e extrair a pasta localmente.
3. Ler o README, este guia e a documentação de uso responsável antes de instalar qualquer coisa.
4. Criar um ambiente virtual local e instalar o pacote com suporte a MCP.
5. Iniciar o servidor MCP local por `stdio` e confirmar que ele ficou pronto para uso.

### Alternativa sem GitHub nem git clone

Se o usuário for advogado ou não tiver familiaridade com Git, o agente pode seguir este roteiro:

1. abrir o repositório no navegador;
2. clicar em "Code" → "Download ZIP";
3. extrair a pasta em um diretório simples, como `C:\nanojud` ou `/Users/usuario/nanojud`;
4. abrir o terminal nessa pasta;
5. seguir os comandos abaixo.

Comandos simples recomendados para a IA:

```bash
git clone https://github.com/lucmolero/nanojud.git
cd nanojud
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# Linux/macOS
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[mcp]"
```

Depois de instalar, a IA pode testar com um comando simples:

```bash
nanojud search 0015020-23.2010.8.26.0053
```

Se quiser validar a instalação completa, pode usar:

```bash
python -m pytest --cov
```

## Prompt inicial para o agente

Cole este prompt no seu agente de IA dentro da pasta do projeto:

```text
Você está em um projeto Python chamado nanojud.
Instale o ambiente local com as dependências de desenvolvimento e MCP.
Depois rode os checks principais e me diga se o projeto está pronto para uso local.

Comandos esperados:
- python -m pip install --upgrade pip
- python -m pip install -e ".[dev,mcp]"
- python -m pytest --cov
- python -m ruff check src tests examples
- python -m mypy src

Não publique dados, não baixe peças restritas e não altere arquivos sem explicar antes.
```

## Instalação manual equivalente

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev,mcp]"
```

Para validar:

```bash
python -m pytest --cov
python -m ruff check src tests examples
python -m mypy src
```

## Configurar MCP local

O MCP local usa `stdio`. Ele não abre uma API pública e não hospeda servidor HTTP.

Configuração genérica:

```json
{
  "mcpServers": {
    "nanojud": {
      "command": "python",
      "args": ["-m", "nanojud.mcp_server"]
    }
  }
}
```

No Windows, prefira o Python absoluto da `.venv`:

```json
{
  "mcpServers": {
    "nanojud": {
      "command": "C:\\caminho\\do\\projeto\\.venv\\Scripts\\python.exe",
      "args": ["-m", "nanojud.mcp_server"]
    }
  }
}
```

## Prompt para consultar um processo

Use um número CNJ público escolhido por você. Para demonstração, o projeto recomenda:

```text
0015020-23.2010.8.26.0053
```

```text
Use o MCP local nanojud.
Valide o número CNJ 0015020-23.2010.8.26.0053.
Depois consulte as fontes públicas disponíveis e me entregue:
- dados básicos;
- partes quando públicas;
- últimas movimentações;
- comunicações DJEN quando houver;
- timeline cronológica;
- limites da consulta.

Separe fatos extraídos de qualquer inferência.
Não dê aconselhamento jurídico.
```

## Prompt para gerar briefing responsável

```text
Com base apenas nos dados públicos extraídos pelo MCP local, gere um briefing processual objetivo.

Estruture em:
- identificação;
- fonte consultada;
- fase observável;
- últimos andamentos;
- marcos relevantes;
- pontos que exigem leitura das peças;
- ressalvas de uso responsável.

Não invente teses. Quando algo for hipótese, rotule como hipótese.
```

## Checklist para o advogado

Antes de usar em rotina profissional:

- confirme que o processo é público;
- evite publicar prints com nomes, CPFs, e-mails ou documentos;
- valide o resultado na fonte oficial quando houver prazo ou ato sensível;
- use rate limit e cache em automações recorrentes;
- leia [Uso Responsável](uso-responsavel.md) e [LGPD](lgpd.md).

## Resultado esperado

Ao final da jornada, o advogado deve conseguir pedir ao agente:

```text
Consulte este CNJ pelo nanojud e me entregue uma timeline auditável.
```

E o agente deve usar a biblioteca local, retornando dados estruturados com fonte, data e limites claros.

Para entender por que esse processo foi escolhido, veja [Demonstração Pública](demonstracao-publica.md).
