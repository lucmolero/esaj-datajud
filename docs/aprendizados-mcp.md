# Aprendizados MCP

Esta página registra aprendizados das validações manuais com o MCP local. Ela não representa novas features implementadas; serve como referência para priorizar refinamentos futuros.

## O que as consultas mostraram

O MCP local já consegue sustentar uma jornada real:

1. validar número CNJ;
2. consultar eSAJ/TJSP;
3. consultar DJEN;
4. consultar DataJud/CNJ;
5. gerar timeline agregada;
6. fornecer insumos para briefing responsável.

O ponto forte não é "dar opinião jurídica". O ponto forte é entregar dados públicos estruturados para que advogado, pesquisador ou agente local trabalhem com rastreabilidade.

## Casos avaliados

### Caso empresarial de alto valor

Foi útil para testar profundidade, perícia, publicações e linha do tempo complexa, mas não é adequado como showcase público. Risco: exposição de disputa empresarial identificável e narrativa sensível.

Decisão: não usar em README, exemplos ou página pública.

### Ação Civil Pública institucional muito antiga

Retornou muitos dados e demonstrou robustez, mas era pesada demais para demo fluida.

Métricas observadas:

- mais de 1700 movimentações;
- timeline com mais de 1800 eventos;
- tempo maior para demonstração ao vivo.

Decisão: boa para teste de carga manual, ruim para onboarding.

### Processo público institucional recomendado

Processo:

```text
0015020-23.2010.8.26.0053
```

Motivos:

- rápido no eSAJ;
- tem DJEN;
- tem DataJud/CNJ;
- tem timeline suficiente;
- envolve partes institucionais;
- permite briefing responsável sem exposição excessiva.

## O que advogados perguntam

As interações mostraram que advogados não perguntam apenas "qual é o JSON?". Eles perguntam:

- que tipo de processo é?
- o que aconteceu?
- qual é a fase atual?
- quais são os marcos relevantes?
- há publicação recente?
- existem incidentes?
- quais teses aparecem?
- o que precisa ser conferido nas peças?

O produto deve responder com separação clara entre:

- fato extraído;
- inferência operacional;
- hipótese jurídica;
- ponto que exige leitura humana.

## Refinamentos futuros sugeridos

Sem alterar o escopo de extração, os refinamentos mais valiosos são:

- saída compacta para demo rápida;
- relatório de fontes consultadas;
- deduplicação entre eSAJ e DJEN;
- marcação de marcos processuais por palavras-chave;
- aviso quando DataJud retornar classe de incidente relacionado;
- sanitização opcional de nomes em outputs públicos;
- exemplos de prompts MCP para advogados;
- fixtures documentais baseadas em outputs reduzidos e sanitizados.

## Critérios para escolher demos futuras

Um bom processo de demonstração deve:

- ser público;
- não depender de segredo, senha ou peça restrita;
- ter menos de 500 movimentações no eSAJ;
- ter alguma comunicação DJEN;
- preferencialmente ter DataJud/CNJ;
- ter partes institucionais ou baixa sensibilidade;
- permitir briefing sem expor dados pessoais desnecessários;
- rodar em menos de 20 segundos em consulta completa manual.

## Mensagem de produto

A melhor narrativa observada é:

> Do número CNJ à linha do tempo auditável: extração responsável de dados públicos judiciais para advogados, legal ops, pesquisa e agentes locais de IA.

Essa mensagem é precisa, vendável e respeita os limites técnicos e jurídicos do projeto.
