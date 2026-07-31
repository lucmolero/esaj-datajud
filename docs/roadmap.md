# Roadmap

Este roadmap organiza a evolução do projeto em entregas pequenas, verificáveis e úteis para usuários jurídicos.

## Agora

- Melhorar documentação pública do GitHub.
- Criar governança básica de projeto aberto.
- Garantir consistência de metadados do pacote.
- Ampliar testes sem depender de rede.

## Próxima versão

- Criar exceções próprias e mensagens de erro amigáveis.
- Adicionar fixtures HTML sanitizadas do eSAJ.
- Testar parsing de dados básicos, partes e movimentações.
- Mockar respostas do DJEN em testes.
- Melhorar contratos de retorno da API.

## Depois

- Extrair documentos vinculados das movimentações.
- Implementar download responsável de peças públicas quando tecnicamente permitido.
- Adicionar cache opcional.
- Exportar CSV e integração opcional com pandas.
- Criar documentação de referência da API.

## Critério de qualidade

Uma funcionalidade só deve ser apresentada como pronta quando tiver:

- contrato documentado;
- teste automatizado;
- exemplo de uso;
- comportamento de erro compreensível;
- limite conhecido declarado.
