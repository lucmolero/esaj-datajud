"""Cliente de alto nível configurável."""

from __future__ import annotations

import logging
import time
from pathlib import Path
from typing import Any, cast

import requests

from . import djen, esaj
from .cache import JsonFileCache
from .config import EsajDatajudConfig
from .models import Extrato, ResumoProcesso
from .version import __version__


class RateLimitedSession(requests.Session):
    """Sessão requests com timeout padrão, rate limit simples e logging."""

    def __init__(
        self,
        *,
        timeout: float,
        rate_limit_interval: float,
        logger: logging.Logger,
        user_agent: str,
    ) -> None:
        super().__init__()
        self.timeout = timeout
        self.rate_limit_interval = rate_limit_interval
        self.logger = logger
        self._last_request_at = 0.0
        self.headers.update(
            {
                "User-Agent": user_agent,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Referer": f"{esaj.ESAJ_BASE}/open.do",
            }
        )

    def request(self, method: str, url: str, **kwargs: Any) -> requests.Response:  # type: ignore[override]
        if "timeout" not in kwargs:
            kwargs["timeout"] = self.timeout
        self._wait_if_needed()
        self.logger.debug("HTTP %s %s", method.upper(), url)
        response = super().request(method, url, **kwargs)
        self._last_request_at = time.monotonic()
        self.logger.debug("HTTP %s %s -> %s", method.upper(), url, response.status_code)
        return response

    def _wait_if_needed(self) -> None:
        if self.rate_limit_interval <= 0 or self._last_request_at <= 0:
            return
        elapsed = time.monotonic() - self._last_request_at
        remaining = self.rate_limit_interval - elapsed
        if remaining > 0:
            self.logger.debug("Rate limit: aguardando %.2fs", remaining)
            time.sleep(remaining)


class EsajDatajudClient:
    """Cliente configurável para uso profissional em integrações."""

    def __init__(
        self,
        config: EsajDatajudConfig | None = None,
        *,
        logger: logging.Logger | None = None,
        session: requests.Session | None = None,
    ) -> None:
        self.config = config or EsajDatajudConfig()
        self.logger = logger or logging.getLogger("esaj_datajud")
        self.session = session or RateLimitedSession(
            timeout=self.config.timeout,
            rate_limit_interval=self.config.rate_limit_interval,
            logger=self.logger,
            user_agent=self.config.resolved_user_agent(__version__),
        )
        self.cache = (
            JsonFileCache(self.config.cache_dir, self.config.cache_ttl_seconds)
            if self.config.cache_enabled
            else None
        )

    def search_processo(self, numero: str) -> ResumoProcesso:
        extrato = self.get_extrato(numero)
        return _resumo_do_extrato(extrato)

    def get_extrato(
        self,
        numero: str,
        baixar_pecas: bool = False,
        limite_pecas: int = 3,
        *,
        inspecionar_pecas: bool = False,
        limite_inspecao_pecas: int = 10,
        salvar_html: bool | None = None,
    ) -> Extrato:
        cache_key = (
            f"{numero}|baixar={baixar_pecas}|limite={limite_pecas}|"
            f"inspecionar={inspecionar_pecas}|limite_inspecao={limite_inspecao_pecas}"
        )
        if self.cache and not baixar_pecas:
            cached = self.cache.get("extrato", cache_key)
            if cached is not None:
                self.logger.debug("Cache hit para extrato %s", numero)
                return cached

        extrato = esaj.montar_extrato(
            numero,
            baixar_pecas=baixar_pecas,
            limite_pecas=limite_pecas,
            inspecionar_pecas=inspecionar_pecas,
            limite_inspecao_pecas=limite_inspecao_pecas,
            salvar_html=self.config.salvar_html if salvar_html is None else salvar_html,
            session=self.session,
            timeout=self.config.timeout,
        )
        if self.cache and not baixar_pecas:
            self.cache.set("extrato", cache_key, extrato)
        return extrato

    def get_partes(self, numero: str) -> dict[str, Any]:
        return cast(
            dict[str, Any],
            self.get_extrato(numero).get(
                "partes",
                {
                    "principais": [],
                    "todas": [],
                    "polo_ativo": [],
                    "polo_passivo": [],
                    "polo_desconhecido": [],
                },
            ),
        )

    def consultar_djen(self, numero: str, data_inicio: str = "") -> list[dict[str, Any]]:
        cache_key = f"{numero}|data_inicio={data_inicio}"
        if self.cache:
            cached = self.cache.get("djen", cache_key)
            if cached is not None:
                self.logger.debug("Cache hit para DJEN %s", numero)
                return cast(list[dict[str, Any]], cached)
        resultado = djen.consultar_processo(numero, data_inicio=data_inicio, session=self.session)
        if self.cache:
            self.cache.set("djen", cache_key, resultado)
        return resultado

    def baixar_pecas(
        self,
        extrato: dict[str, Any],
        destino: Path,
        sobrescrever: bool = False,
        limite: int = 0,
    ) -> list[dict[str, Any]]:
        movimentos = []
        documentos = extrato.get("documentos", {}).get("publicos_candidatos_unicos", [])
        if documentos:
            movimentos = [{"documentos": documentos}]
        else:
            movimentos = extrato.get("movimentacoes", [])
        return esaj.baixar_pecas_publicas(
            self.session,
            movimentos,
            destino,
            limite=limite,
            sobrescrever=sobrescrever,
        )


def _resumo_do_extrato(extrato: Extrato) -> ResumoProcesso:
    basicos = extrato.get("dados_basicos", {})
    movimentos = extrato.get("movimentacoes", [])
    ultima = movimentos[-1] if movimentos else {}
    return {
        "numero": basicos.get("numero", ""),
        "classe": basicos.get("classe", ""),
        "assunto": basicos.get("assunto", ""),
        "foro": basicos.get("foro", ""),
        "vara": basicos.get("vara", ""),
        "juiz": basicos.get("juiz", ""),
        "ultima_movimentacao": ultima.get("titulo") or ultima.get("texto", ""),
        "ultima_data": ultima.get("data", ""),
        "url": extrato.get("origem", {}).get("url_final", ""),
        "status": extrato.get("status", "ok"),
        "mensagem": "Processo consultado com sucesso",
    }
