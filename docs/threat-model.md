# Modelo de Ameaças

Este modelo descreve riscos práticos para uso da biblioteca em ambiente jurídico.

## Ativos protegidos

- Dados pessoais em extratos, peças, logs e cache.
- Credenciais e tokens de ambientes que integrem a biblioteca.
- Integridade dos dados extraídos.
- Disponibilidade das fontes públicas consultadas.
- Reputação profissional de usuários e mantenedores.

## Riscos

| Risco | Impacto | Mitigação |
| --- | --- | --- |
| Vazamento de extratos ou peças | Exposição de dados pessoais e estratégia jurídica | `.gitignore`, sanitização, controle de acesso e revisão antes de publicar |
| Coleta excessiva | Bloqueio, dano reputacional ou violação de regras | rate limit, cache, finalidade definida e volume proporcional |
| Mudança de HTML da fonte | Dados incompletos ou parsing incorreto | fixtures, testes, erros explícitos e versionamento |
| Logs com dados sensíveis | Exposição operacional | logging moderado e política de retenção |
| Uso fora do escopo público | Risco jurídico e ético | não burlar autenticação, captcha, segredo de justiça ou restrições |

## Fora de escopo

O projeto não fornece automação para login, quebra de captcha, extração de processos sigilosos ou contorno de medidas técnicas de proteção.
