# ESPECIFICAÇÕES DO PROJETO `esaj-datajud`

## Visão

Uma biblioteca Python profissional voltada para advogados e escritórios que precisam consultar e extrair dados de processos no eSAJ/TJSP e no DJEN/DataJud.

A biblioteca deve ser:
- simples para uso diário por não-desenvolvedores;
- confiável em operações de scraping e API;
- estruturada para ser extensível, testável e documentada;
- segura em relação a dados sensíveis e comportamento não intrusivo.

## Objetivo do produto

Produzir uma biblioteca local chamada `esaj-datajud` que permita:
- buscar dados de processo no eSAJ/TJSP;
- montar extratos estruturados de andamentos, partes, documentos e apensos;
- consultar comunicações do DJEN (DataJud);
- baixar arquivos públicos vinculados de processos quando desejado;
- operar com CLI simples e API Python clara.

## Público-alvo

Advogados, estagiários e equipes de escritório jurídico.

### Usuários típicos
- advogado que precisa gerar relatório rápido de um processo;
- assistente que extrai partes e andamentos para controle interno;
- analista que automatiza consultas em Python ou via CLI.

## Proposta de valor

Criar a ferramenta mais fácil e confiável para extrair informações do eSAJ/TJSP sem depender diretamente do Apps Script, mantendo o fluxo auditável e previsível.

---

# Arquitetura da biblioteca

## 1. Estrutura do projeto

```
Lib Python - Esaj - Datajud/
├── pyproject.toml
├── README.md
├── SPECS.md
├── requirements.txt
├── src/
│   └── esaj_datajud/
│       ├── __init__.py
│       ├── api.py
│       ├── esaj.py
│       ├── djen.py
│       ├── tjsp.py
│       ├── cli.py
│       └── utils.py
└── tests/
    ├── test_imports.py
    ├── test_esaj.py
    ├── test_djen.py
    └── fixtures/
        ├── esaj_example.html
        └── ...
```

## 2. Camadas e responsabilidades

### 2.1 `esaj_datajud.api`
Responsável pela API orientada a advogados.

Funções públicas principais:
- `search_processo(numero: str) -> dict`
- `get_extrato(numero: str, baixar_pecas: bool = False, limite_pecas: int = 3) -> dict`
- `get_partes(numero: str) -> dict`
- `baixar_pecas(extrato: dict, destino: Path, sobrescrever: bool = False) -> list[dict]`
- `resumo_rapido(numero: str) -> str`

Essa camada deve ser a mais usada por scripts e CLI.

### 2.2 `esaj_datajud.esaj`
Responsável por:
- montar URL de busca
- carregar página
- parse HTML com BeautifulSoup
- extrair campos básicos, partes, movimentações e documentos
- baixar peças públicas

Funções internas organizadas:
- `montar_url_busca`
- `carregar_pagina`
- `extrair_dados_basicos`
- `extrair_partes`
- `extrair_movimentacoes`
- `extrair_documentos_da_movimentacao`
- `extrair_metadados_movimentacao`
- `montar_extrato`
- `baixar_pecas_publicas`

### 2.3 `esaj_datajud.djen`
Responsável por coletar comunicações do DJEN.

Funções:
- `consultar_processo(numero: str, data_inicio: str = "") -> list[dict]`
- `_parse_data(item: dict) -> str`
- `_fetch_page(session: requests.Session, params: dict) -> list[dict]`

### 2.4 `esaj_datajud.tjsp`
Helpers específicos de TJSP/partes/consulta de partes.
Opcional para ciclos de uso mais avançados.

### 2.5 `esaj_datajud.cli`
Camada CLI que transforma a API em comandos de linha de comando.

Comandos propostos:
- `esaj search <numero>`
- `esaj extrato <numero> [--baixar-pecas] [--out <pasta>]`
- `esaj partes <numero>`
- `esaj baixar <extrato.json> --out <pasta>`
- `esaj djen <numero>`

A CLI deve ter ajuda clara e exemplos para advogados.

### 2.6 `esaj_datajud.utils`
Funções de utilidade:
- limpeza de texto
- normalização de nomes de arquivo
- deduplicação
- parsing de datas auxiliares
- validação de número CNJ

---

# Especificação da API para advogados

## 1. `search_processo`

### Assinatura

```python
search_processo(numero: str) -> dict
```

### Retorno esperado

```python
{
  "numero": "1076539-20.2019.8.26.0100",
  "classe": "Ação Civil Pública",
  "assunto": "Meio Ambiente",
  "foro": "Foro Central Cível",
  "vara": "2ª Vara de Registros Públicos",
  "juiz": "Dr. Fulano",
  "ultima_movimentacao": "Publicação de intimação",
  "ultima_data": "2026-07-30",
  "url": "https://esaj.tjsp.jus.br/cpopg/show.do?...",
  "status": "ok",
  "mensagem": "Processo encontrado",
}
```

### Uso recomendado

- para validar se o processo existe;
- para obter um resumo rápido antes de extrair o extrato completo.

## 2. `get_extrato`

### Assinatura

```python
get_extrato(numero: str, baixar_pecas: bool = False, limite_pecas: int = 3) -> dict
```

### Retorno esperado

```python
{
  "origem": { ... },
  "dados_basicos": { ... },
  "partes": { ... },
  "movimentacoes": [ ... ],
  "documentos": {
      "publicos_candidatos": [ ... ],
      "restritos_por_senha": [ ... ]
  },
  "peticoes_diversas": [ ... ],
  "audiencias": [ ... ],
  "relacionados": { ... },
  "mensagem": "Extrato gerado com sucesso",
  "status": "ok",
}
```

### Principais casos de uso
- gerar JSON de processo para arquivo ou integração;
- alimentar um relatório ou painel jurídico;
- inspecionar questões de sigilo e documentos.

## 3. `get_partes`

### Assinatura

```python
get_partes(numero: str) -> dict
```

### Retorno esperado

```python
{
  "ativo": ["Empresa X"],
  "passivo": ["Empresa Y"],
  "desconhecido": [ ... ],
  "status": "ok",
  "mensagem": "Partes extraídas",
}
```

## 4. `baixar_pecas`

### Assinatura

```python
baixar_pecas(extrato: dict, destino: Path, sobrescrever: bool = False) -> list[dict]
```

### Retorno esperado

```python
[
  {"cd_documento": "12345", "arquivo": "saida/peca_12345.pdf", "status": "baixado"},
]
```

### Regras
- nenhum arquivo é sobrescrito por padrão;
- o comportamento `--dry-run` deve simular sem gravar;
- logs devem informar quais documentos não foram liberados.

## 5. `resumo_rapido`

### Assinatura

```python
resumo_rapido(numero: str) -> str
```

### Exemplo de saída

```
TJSP 1ª Instância · 1076539-20.2019.8.26.0100
Classe: Ação Civil Pública | Vara: 2ª Vara de Registros Públicos
Última movimentação: Publicação de intimação em 2026-07-30
Partes principais: Autor Empresa X / Ré Empresa Y
```

---

## Arquitetura técnica

## 1. Diretórios e namespace

- `src/esaj_datajud/` : código fonte principal
- `tests/` : testes unitários e de parse
- `tests/fixtures/` : HTML estático para validar o parser sem rede
- `pyproject.toml` : metadata e dependências
- `requirements.txt` : instalação direta
- `README.md` / `SPECS.md` : documentação do projeto

## 2. Dependências externas

- `requests` — HTTP
- `beautifulsoup4` — parsing HTML
- `pytest` — testes

## 3. Extensibilidade

Devemos manter a biblioteca pronta para:
- suporte a outros tribunais no futuro;
- cache local de consultas;
- integração via `pandas` ou exportação CSV;  
- extração incremental por data.

## 4. Testes planejados

### Mínimos obrigatórios
- `test_imports.py` — valida importação dos módulos
- `test_esaj.py` — valida parsing de HTML de exemplo
- `test_djen.py` — valida parsing e retorno do DJEN
- `test_api.py` — valida contratos da API pública

### Fixtures
- HTML salvo de processo real/estruturado de eSAJ
- respostas JSON simuladas da API DJEN

### Cobertura
- parsing de campos básicos;
- detecção de lista vs página única;
- extração de partes e documentos;
- comportamento quando a página está restrita ou não encontrada;
- retorno de erros amigáveis.

## 5. CLI e experiência do usuário

### Comandos
- `esaj search <numero>`
- `esaj extrato <numero> --out <arquivo.json>`
- `esaj partes <numero>`
- `esaj baixar <arquivo_extrato.json> --out <pasta>`
- `esaj djen <numero> --out <arquivo.json>`

### Mensagens
- `Processo encontrado` / `Processo não encontrado`
- `Consulta concluída` / `Não foi possível acessar o eSAJ`
- `Documento reservado ou restrito por senha`

### Flags úteis
- `--verbose`
- `--dry-run`
- `--yes`
- `--no-cache`

---

# Plano de desenvolvimento

## Fase 0: Preparação
- definir a arquitetura do pacote;
- criar `SPECS.md`;  
- assegurar que a estrutura do projeto reflete a API desejada.

## Fase 1: API pública e módulo core
- implementar `esaj_datajud.api` com os 5 métodos públicos;
- implementar `esaj_datajud.esaj` com parsing organizado;
- implementar `esaj_datajud.djen` com consulta de comunicações;
- criar `esaj_datajud.utils`.

## Fase 2: CLI e UX
- criar `esaj_datajud.cli` com `argparse` ou `typer`;
- adicionar entrypoints no `pyproject.toml`;
- documentar comandos.

## Fase 3: Testes e fixtures
- salvar HTML de exemplo em `tests/fixtures`;
- escrever testes de parser e de API;
- validar importação e execução local.

## Fase 4: Documentação e onboarding
- escrever quickstart no `README.md`;
- incluir exemplos de uso em Python e CLI;
- criar guia de troubleshooting.

## Fase 5: Polimento e distribuição local
- adicionar instruções de instalação editable (`pip install -e .`);
- gerar pacote wheel local;
- criar tag `v0.1` local.

---

# Critérios de aceitação para advogados

1. Um advogado consegue instalar e rodar em até 10 minutos.
2. A CLI entrega resultados compreensíveis sem precisar abrir código.
3. A API pública expõe apenas funções úteis, sem detalhes internos.
4. O README contém 3 casos de uso claros.
5. O parser e o DJEN funcionam mesmo quando o HTML muda um pouco.

---

# Exemplo de Quickstart

## Instalar

```bash
python -m pip install -r requirements.txt
python -m pip install -e .
```

## Buscar processo

```bash
python -m esaj_datajud.cli search 1076539-20.2019.8.26.0100
```

## Gerar extrato JSON

```bash
python -m esaj_datajud.cli extrato 1076539-20.2019.8.26.0100 --out extrato.json
```

## Baixar peças públicas

```bash
python -m esaj_datajud.cli baixar extrato.json --out pecas/
```

---

# Anexo: estilo de biblioteca da comunidade

A arquitetura proposta segue boas práticas de bibliotecas famosas do GitHub:
- API de alto nível concisa;
- módulos internos separados por responsabilidade;
- use de fixtures e testes;
- documentação clara de uso;
- CLI opcional ligada à API.

A implementação deve priorizar: clareza, manutenção e facilidade de uso.
