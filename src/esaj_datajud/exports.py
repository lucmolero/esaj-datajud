"""Exportadores tecnicos para dados extraidos."""

from __future__ import annotations

import csv
import json
import sqlite3
from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import Any


def to_json(data: Any) -> str:
    """Serializa dados em JSON UTF-8 amigavel."""
    return json.dumps(data, ensure_ascii=False, indent=2, default=str)


def write_json(data: Any, path: str | Path) -> Path:
    """Grava dados em arquivo JSON."""
    destino = Path(path)
    destino.write_text(to_json(data), encoding="utf-8")
    return destino


def to_jsonl(records: Iterable[Mapping[str, Any]]) -> str:
    """Serializa registros em JSON Lines."""
    return "\n".join(json.dumps(record, ensure_ascii=False, default=str) for record in records)


def write_jsonl(records: Iterable[Mapping[str, Any]], path: str | Path) -> Path:
    """Grava registros em JSON Lines."""
    destino = Path(path)
    conteudo = to_jsonl(records)
    destino.write_text(conteudo + ("\n" if conteudo else ""), encoding="utf-8")
    return destino


def write_csv(records: Iterable[Mapping[str, Any]], path: str | Path) -> Path:
    """Grava registros achatados em CSV."""
    rows = [dict(record) for record in records]
    destino = Path(path)
    fieldnames = sorted({key for row in rows for key in row})
    with destino.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: _csv_value(row.get(key, "")) for key in fieldnames})
    return destino


def write_sqlite(
    records: Iterable[Mapping[str, Any]],
    path: str | Path,
    *,
    table: str = "records",
) -> Path:
    """Grava registros em SQLite usando colunas TEXT para portabilidade."""
    rows = [dict(record) for record in records]
    destino = Path(path)
    fieldnames = sorted({key for row in rows for key in row}) or ["empty"]
    columns = ", ".join(f'"{name}" TEXT' for name in fieldnames)
    placeholders = ", ".join("?" for _ in fieldnames)
    with sqlite3.connect(destino) as conn:
        conn.execute(f'DROP TABLE IF EXISTS "{table}"')
        conn.execute(f'CREATE TABLE "{table}" ({columns})')
        for row in rows:
            conn.execute(
                f'INSERT INTO "{table}" VALUES ({placeholders})',
                [_csv_value(row.get(key, "")) for key in fieldnames],
            )
    return destino


def _csv_value(value: Any) -> str:
    if isinstance(value, str):
        return value
    if value is None:
        return ""
    if isinstance(value, int | float | bool):
        return str(value)
    return json.dumps(value, ensure_ascii=False, default=str)
