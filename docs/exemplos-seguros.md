# Exemplos Seguros

Este projeto evita usar estudos de caso empresariais identificáveis como vitrine pública. A documentação deve ensinar a ferramenta sem expor disputas sensíveis, dados pessoais desnecessários ou narrativas que possam gerar risco reputacional.

## Política de exemplos

Prefira:

- números CNJ demonstrativos em tutoriais;
- fixtures sanitizadas;
- processos escolhidos pelo próprio usuário;
- casos institucionais de baixa sensibilidade;
- outputs reduzidos e sem dados pessoais excessivos.

Evite:

- disputas comerciais de alto valor como showcase;
- nomes de partes privadas em material promocional;
- e-mails, CPF, endereços ou dados de contato;
- prints de páginas com dados sensíveis;
- peças processuais reais;
- conclusões jurídicas sem leitura integral dos autos.

## Processo público recomendado

Os exemplos do projeto usam um processo público institucional previamente testado:

```text
0015020-23.2010.8.26.0053
```

Ele foi escolhido por ter bom equilíbrio entre completude e velocidade: eSAJ, DJEN, DataJud/CNJ e timeline agregada funcionam sem depender de uma disputa empresarial sensível.

Veja a página [Demonstração Pública](demonstracao-publica.md) para contexto, métricas e ressalvas.

## Como fazer uma demonstração pública

Use este roteiro:

1. Explique que o número é público, institucional e usado apenas para demonstração técnica.
2. Mostre o comando.
3. Mostre apenas campos estruturais do resultado.
4. Remova dados pessoais e trechos longos.
5. Informe a fonte consultada.
6. Informe os limites da consulta.

Exemplo:

```bash
nanojud timeline <NUMERO_CNJ_PUBLICO> --source esaj --source djen --out timeline.json
```

Resultado demonstrativo:

```json
{
  "numero_cnj": "<NUMERO_CNJ_PUBLICO>",
  "sources": ["esaj", "djen"],
  "timeline_count": 42,
  "status": "ok",
  "observacao": "Dados públicos extraídos e normalizados; validar atos sensíveis na fonte oficial."
}
```

## Para artigos, posts e vídeos

Ao divulgar o projeto, destaque o método:

- extração responsável;
- fonte pública;
- timeline auditável;
- MCP local;
- limites éticos;
- uso profissional com revisão humana.

Evite vender a ideia de que a ferramenta "entende o processo sozinha". A proposta correta é: ela organiza dados públicos para acelerar a análise humana e a automação responsável.
