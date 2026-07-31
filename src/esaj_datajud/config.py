"""Configuração de clientes esaj-datajud."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class EsajDatajudConfig:
    """Configuração operacional para uso corporativo e automações recorrentes."""

    timeout: float = 30.0
    rate_limit_interval: float = 0.0
    cache_enabled: bool = False
    cache_dir: Path = Path(".esaj_datajud_cache")
    cache_ttl_seconds: int = 24 * 60 * 60
    salvar_html: bool = False
    user_agent: str = (
        "Mozilla/5.0 "
        "(compatible; esaj-datajud/{version}; +https://github.com/lucmolero/esaj-datajud)"
    )

    def resolved_user_agent(self, version: str) -> str:
        return self.user_agent.format(version=version)
