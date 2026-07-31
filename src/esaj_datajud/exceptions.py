"""Exceções públicas do esaj-datajud."""


class EsajDatajudError(Exception):
    """Classe base para erros previstos da biblioteca."""


class FormatoCNJInvalido(EsajDatajudError, ValueError):
    """Número CNJ ausente, mal formatado ou com dígito verificador inválido."""


class URLInvalida(EsajDatajudError, ValueError):
    """URL fora do domínio e caminho esperados pelo cliente."""


class ConsultaIndisponivel(EsajDatajudError):
    """Fonte remota indisponível, resposta inválida ou falha de comunicação."""


class ProcessoNaoEncontrado(EsajDatajudError):
    """A fonte consultada não retornou uma página de processo válida."""


class AcessoRestrito(EsajDatajudError):
    """A fonte indicou bloqueio, captcha, autenticação, senha ou restrição de acesso."""


class CredencialAusente(EsajDatajudError):
    """Credencial necessária para uma fonte pública não foi informada."""


class DownloadIndisponivel(EsajDatajudError):
    """Não foi possível baixar a peça pública solicitada."""
