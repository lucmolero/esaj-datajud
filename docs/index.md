# esaj-datajud

`esaj-datajud` é uma biblioteca Python e CLI para consultar, organizar e exportar informações públicas de processos do eSAJ/TJSP e comunicações do DJEN/DataJud.

O projeto foi desenhado para ficar no encontro entre direito, academia e engenharia corporativa: contratos previsíveis, testes sem rede, documentação clara, cuidado com LGPD e uma API pequena o bastante para ser auditável.

## Para quem é

- Advogados e escritórios que precisam estruturar consultas públicas recorrentes.
- Desenvolvedores de legaltech que querem uma base aberta e extensível.
- Pesquisadores que precisam de metodologia, rastreabilidade e limites declarados.
- Times corporativos que avaliam risco, governança e manutenção antes de integrar uma dependência.

## Diferenciais técnicos

- API de alto nível para resumo, extrato, partes, peças públicas candidatas e DJEN.
- Cliente configurável com timeout, rate limit, cache opcional e logging.
- Validação de número CNJ com dígito verificador.
- Contratos tipados publicados com `py.typed`.
- Fixtures sanitizadas e testes automatizados sem dependência de rede.
- CI com testes, cobertura, lint, formatação, build, auditoria de dependências e checagem de tipos.

## Comece por aqui

Leia o [Quickstart](quickstart.md), depois veja o [Cliente Configurável](client.md) para uso em integrações profissionais.
