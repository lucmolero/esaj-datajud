"""Identificacao padronizada das fontes de extracao."""

from __future__ import annotations

from typing import Literal

SourceName = Literal["esaj", "datajud", "djen"]

ESAJ: SourceName = "esaj"
DATAJUD: SourceName = "datajud"
DJEN: SourceName = "djen"

ALL_SOURCES: tuple[SourceName, ...] = (ESAJ, DATAJUD, DJEN)

SOURCE_DESCRIPTIONS: dict[SourceName, str] = {
    ESAJ: "eSAJ/TJSP: paginas publicas processuais do Tribunal de Justica de Sao Paulo.",
    DATAJUD: "DataJud/CNJ: API publica de dados processuais estruturados.",
    DJEN: "DJEN: Diario de Justica Eletronico Nacional para comunicacoes e publicacoes.",
}


def normalizar_fonte(fonte: str) -> SourceName:
    """Normaliza e valida uma fonte conhecida pela biblioteca."""
    valor = fonte.strip().lower()
    if valor not in ALL_SOURCES:
        permitidas = ", ".join(ALL_SOURCES)
        raise ValueError(f"Fonte desconhecida: {fonte!r}. Use uma de: {permitidas}.")
    return valor  # type: ignore[return-value]
