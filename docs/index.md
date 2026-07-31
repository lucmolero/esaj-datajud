# esaj-datajud

Toolkit Python para consulta responsável, estruturação e auditoria de dados públicos judiciais do eSAJ/TJSP e comunicações do DJEN/DataJud.

O projeto foi desenhado para ficar no encontro entre direito, academia e engenharia corporativa: contratos previsíveis, testes sem rede, documentação clara, cuidado com LGPD e uma API pequena o bastante para ser auditável.

!!! note "Projeto independente"
    `esaj-datajud` não é um produto oficial do TJSP, CNJ, eSAJ ou DataJud. A biblioteca organiza consultas a fontes públicas ou legitimamente acessíveis pelo usuário e não tem como objetivo contornar autenticação, senha, captcha ou segredo de justiça.

## Para quem é

- Advogados e escritórios que precisam estruturar consultas públicas recorrentes.
- Desenvolvedores de legaltech que querem uma base aberta, tipada e extensível.
- Pesquisadores que precisam de metodologia, rastreabilidade e limites declarados.
- Times corporativos que avaliam risco, governança e manutenção antes de integrar uma dependência.

## Por que confiar

- CI em Python 3.10, 3.11 e 3.12.
- Cobertura automatizada acima de 90%.
- CodeQL, `pip-audit`, lint, type check, build e validação de pacote.
- Testes sem rede com fixtures sanitizadas.
- Testes `live` opcionais contra fonte real, fora do CI por estabilidade.
- Documentação de LGPD, uso responsável, modelo de ameaças, governança e reprodutibilidade.
- Releases versionadas com `wheel`, `sdist` e notas públicas.

## Casos suportados

- Dados básicos do processo.
- Partes e advogados.
- Movimentações e metadados de publicação.
- Documentos públicos candidatos e documentos restritos por senha.
- Audiências, petições diversas, incidentes e apensos.
- Consulta a comunicações DJEN/DataJud.
- Páginas públicas do eSAJ que incluem `popupSenha` oculto.

## Comece por aqui

Leia o [Quickstart](quickstart.md), depois veja o [Cliente Configurável](client.md) para uso em integrações profissionais.
