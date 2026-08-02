# Demonstração Pública

Esta página define o processo público recomendado para demonstrações do `nanojud`.

O objetivo é ter uma demo completa, rápida e responsável: suficiente para mostrar extração, normalização, DJEN, DataJud/CNJ, timeline e MCP local, sem usar disputa empresarial sensível como vitrine.

## Processo recomendado

```text
0015020-23.2010.8.26.0053
```

Fonte principal: eSAJ/TJSP.

Perfil do caso:

- Classe: Mandado de Segurança Cível.
- Assunto: Organização Político-administrativa / Administração Pública.
- Foro: Foro Central - Fazenda Pública/Acidentes.
- Vara: 7ª Vara de Fazenda Pública.
- Partes institucionais: sindicato, autoridade fazendária e Fazenda Pública.
- Valor da ação: R$ 510,00.

## Por que usar este processo

Este processo foi escolhido porque:

- é público;
- possui partes predominantemente institucionais;
- evita disputa empresarial sensível;
- retorna rápido no eSAJ;
- possui comunicações no DJEN;
- possui dados estruturados no DataJud/CNJ;
- tem linha do tempo suficiente para demonstração;
- mostra uma jornada real de conhecimento, execução/cumprimento e extinção.

Validação manual por MCP local em 31/07/2026:

| Fonte | Resultado |
|---|---:|
| eSAJ/TJSP | 246 movimentações |
| DataJud/CNJ | 50 movimentos |
| DJEN | 6 comunicações |
| Timeline agregada | 302 eventos |
| Erros da timeline | 0 |

## Comandos de demonstração

Consulta rápida:

```bash
nanojud search 0015020-23.2010.8.26.0053
```

Extrato público:

```bash
nanojud extrato 0015020-23.2010.8.26.0053 --out extrato.json
```

DJEN:

```bash
nanojud djen 0015020-23.2010.8.26.0053 --out djen.json
```

DataJud/CNJ:

```bash
nanojud datajud 0015020-23.2010.8.26.0053 --out datajud.json
```

Timeline:

```bash
nanojud timeline 0015020-23.2010.8.26.0053 --source esaj --source djen --source datajud --out timeline.json
```

## Prompt MCP para demo

```text
Use o MCP local nanojud.
Consulte o processo 0015020-23.2010.8.26.0053.
Entregue dados básicos, fontes consultadas, últimos andamentos, DJEN, DataJud e uma timeline resumida.
Separe fatos extraídos de inferências.
Não dê aconselhamento jurídico.
```

## Briefing demonstrativo

Com base nos dados públicos extraídos pelo MCP local, o caso pode ser apresentado assim:

> Mandado de Segurança Cível proposto por sindicato relacionado à Administração Pública estadual. O processo evoluiu para fase de execução/cumprimento, com incidentes de Requisição de Pequeno Valor. O andamento mais relevante recente indica extinção da execução/cumprimento pela satisfação da obrigação, com fundamento no art. 924, II, do CPC. Para análise de mérito, é necessário consultar as peças e decisões principais.

## Perguntas que a demo responde bem

- Qual é o tipo de processo?
- Quem são as partes públicas/institucionais?
- Qual é a fase observável?
- Qual foi o último ato relevante?
- Há publicações recentes no DJEN?
- Há eventos no DataJud/CNJ?
- Existem incidentes de RPV?
- A timeline agrega eventos de mais de uma fonte?
- Quais dados exigem conferência na fonte oficial?

## O que não afirmar na demo

Evite afirmar:

- tese jurídica material completa;
- resultado estratégico;
- prazo processual em curso sem conferência oficial;
- conclusão sobre direito líquido e certo;
- parecer jurídico sem leitura das peças.

A demonstração mostra extração e organização de dados públicos. A análise jurídica permanece com o profissional.

## Cuidados de exposição

Para vídeos, posts e apresentações:

- mostre dados agregados e trechos curtos;
- oculte nomes de advogados quando não forem necessários;
- não exponha documentos integrais;
- não use dados de terceiros como material promocional sem contexto;
- destaque que o projeto é independente e não oficial.
