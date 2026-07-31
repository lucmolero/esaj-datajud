# Changelog

Todas as mudanças relevantes deste projeto serão documentadas aqui.

O formato segue a ideia de manter versões legíveis para usuários jurídicos e desenvolvedores.

## [0.2.0] - Em desenvolvimento

### Adicionado

- Exceções públicas para erros previstos: CNJ inválido, URL inválida, acesso restrito, consulta indisponível, processo não encontrado e download indisponível.
- Contratos tipados em `esaj_datajud.models` com `TypedDict`.
- Validação de CNJ com normalização e conferência de dígito verificador.
- Parser eSAJ ampliado para dados básicos, partes, movimentações, documentos vinculados, metadados de publicação, audiências, petições, incidentes e apensos.
- Cliente DJEN com sessão injetável, retry configurável, backoff e testes sem rede.
- CLI com comando `baixar`, flags `--inspecionar-pecas`, `--salvar-html` e erros em JSON.
- Documentação de arquitetura, contratos e erros.

### Alterado

- `resumo_rapido` passa a consultar o extrato uma única vez.
- `baixar_pecas` passa a usar o fluxo real de documentos públicos candidatos quando disponível.

## [0.1.1] - 2026-07-31

### Corrigido

- Corrige metadados PEP 621 do `pyproject.toml`, removendo `url` de `project.authors`.
- Atualiza declaração de licença para SPDX (`MIT`) e inclui `license-files`.
- Adiciona dependências dev necessárias para validação local de lint e build.
- Formata o código com Ruff e corrige problemas de lint.

### Adicionado

- CI passa a executar testes, lint e build do pacote.
- Testes de parsing com fixture HTML sanitizada.
- Documentação e arquivos de governança para GitHub.

## [0.1.0] - 2026-07-31

### Adicionado

- Estrutura inicial do pacote `esaj_datajud`.
- API pública com funções para resumo, extrato, partes e DJEN.
- CLI `esaj` com comandos iniciais.
- Especificação de produto em `SPECS.md`.
- Documentação inicial de uso, contribuição, segurança e roadmap.

### Conhecido

- Download de peças ainda não está implementado de ponta a ponta.
- Parser do eSAJ ainda precisa de fixtures reais sanitizadas e cobertura maior.
- Tratamento de erros será refinado nas próximas versões.
