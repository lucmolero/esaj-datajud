# Fontes

`esaj-datajud` separa as fontes de extração por responsabilidade.

## eSAJ/TJSP

Fonte de páginas públicas processuais do Tribunal de Justiça de São Paulo.

Extrações suportadas:

- dados básicos;
- partes;
- advogados e OAB quando presentes na página;
- movimentações;
- documentos vinculados;
- audiências;
- petições;
- incidentes, apensos e processos relacionados;
- HTML bruto opcional para auditoria.

## DataJud/CNJ

Fonte de dados processuais estruturados pela API pública do DataJud.

Extrações suportadas:

- número CNJ;
- índice DataJud inferido pelo CNJ;
- tribunal;
- grau;
- classe;
- órgão julgador;
- assuntos;
- movimentos;
- partes quando disponíveis;
- payload bruto opcional.

O DataJud exige API key. A biblioteca lê `ESAJ_DATAJUD_DATAJUD_API_KEY`, `DATAJUD_API_KEY` ou `CNJ_DATAJUD_API_KEY`, ou aceita `api_key` explicitamente.

## DJEN

Fonte de comunicações, publicações e intimações do Diário de Justiça Eletrônico Nacional.

Extrações suportadas:

- id da comunicação;
- data de disponibilização;
- tribunal;
- órgão;
- classe;
- tipo de comunicação;
- destinatários;
- texto integral;
- link.

## Escopo

O projeto não calcula risco, não estima fase processual, não atribui relevância jurídica e não gera parecer. A camada nova é estritamente de extração, normalização técnica, preservação de fonte e exportação.
