# Para Advogados

`esaj-datajud` é uma biblioteca open source para transformar dados públicos judiciais em informação estruturada, auditável e útil para rotinas jurídicas.

Ela não substitui análise jurídica. Ela reduz o trabalho operacional de coletar, organizar e conferir informações públicas.

## O que resolve

Advogados costumam perder tempo em tarefas repetitivas:

- consultar andamento;
- copiar dados básicos;
- conferir partes;
- verificar publicações;
- montar linha do tempo;
- comparar fontes públicas;
- preparar contexto para análise.

O projeto entrega uma camada técnica para automatizar essa coleta de forma local, rastreável e responsável.

## O que já existe

- Consulta pública do eSAJ/TJSP.
- Consulta ao DataJud/CNJ.
- Consulta ao DJEN.
- Normalização de número CNJ.
- Extração de dados básicos, partes, movimentações, audiências, petições, apensos e documentos vinculados quando públicos.
- Timeline cronológica.
- API Python.
- CLI.
- MCP local para agentes de IA.
- Documentação de LGPD, governança, reprodutibilidade e uso responsável.

## Jornada prática

1. Escolha um número CNJ público.
2. Instale o projeto com ajuda de um agente de IA ou pela CLI.
3. Consulte as fontes públicas.
4. Gere JSON ou timeline.
5. Use o resultado como base para conferência, relatório interno ou pesquisa.
6. Valide atos sensíveis diretamente na fonte oficial.

Para testar sem escolher um caso próprio, use a [Demonstração Pública](demonstracao-publica.md).

## Como pedir para um agente

```text
Use o MCP local esaj-datajud para consultar <NUMERO_CNJ_PUBLICO>.
Quero uma linha do tempo objetiva, com fonte, data e resumo de cada evento.
Não invente informações e separe fatos extraídos de hipóteses.
```

Exemplo de CNJ público institucional para demonstração:

```text
0015020-23.2010.8.26.0053
```

## O que não faz

O projeto não:

- acessa processos em segredo de justiça;
- burla senha, captcha ou autenticação;
- baixa peças restritas automaticamente;
- substitui estratégia jurídica;
- garante prazo processual;
- classifica risco jurídico;
- hospeda dados sensíveis em nuvem.

## Melhor uso em escritório

Use `esaj-datajud` como infraestrutura:

- pré-triagem de processos públicos;
- rotina de conferência;
- organização de timelines;
- pesquisa empírica;
- base para automações internas;
- apoio a agentes locais de IA.

## Por que isso importa

A advocacia está entrando em uma fase em que agentes de IA conseguem operar ferramentas locais. Projetos como `esaj-datajud` ajudam a conectar esses agentes a fontes públicas com contratos claros, logs, testes e limites explícitos.

O valor está na combinação:

- dados públicos;
- extração responsável;
- rastreabilidade;
- automação local;
- governança aberta.
