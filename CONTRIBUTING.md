# Contribuindo

Obrigado por considerar contribuir com o `esaj-datajud`.

Este projeto busca ser uma biblioteca aberta, profissional e confiável para soluções jurídicas. Contribuições são bem-vindas, especialmente em documentação, testes com fixtures sanitizadas, parsing robusto e experiência de uso por advogados.

## Princípios

- Seja explícito sobre o comportamento esperado.
- Não inclua dados pessoais, documentos sigilosos ou HTML bruto com informações sensíveis.
- Prefira fixtures sanitizadas a chamadas reais de rede em testes.
- Não implemente mecanismos para burlar captcha, senha, segredo de justiça ou restrições de acesso.
- Mantenha mensagens de erro compreensíveis para pessoas não técnicas.

## Ambiente local

```bash
python -m pip install -e ".[dev]"
python -m pytest
```

## Antes de enviar um pull request

```bash
python -m pytest
python -m build
```

## Como contribuir

1. Abra uma issue descrevendo o problema ou melhoria.
2. Crie uma branch curta e objetiva.
3. Adicione testes quando alterar comportamento.
4. Atualize documentação quando alterar API, CLI ou contratos de saída.
5. Abra um pull request explicando o impacto para usuários jurídicos e técnicos.

## Dados de teste

Ao adicionar fixtures:

- remova nomes, CPFs, CNPJs, endereços, e-mails e documentos;
- preserve apenas a estrutura HTML ou JSON necessária ao teste;
- descreva no teste qual cenário a fixture representa.
