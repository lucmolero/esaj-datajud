"""esaj_datajud package

Expose main modules:
- `api` : highest-level operations for lawyers and systems
- `esaj` : eSAJ extraction helpers
- `datajud` : DataJud/CNJ structured process data helpers
- `djen` : DJEN communication helpers
- `utils`: helper utilities
"""

from . import (
    api,
    cache,
    client,
    config,
    datajud,
    djen,
    esaj,
    exceptions,
    exports,
    extraction,
    models,
    normalization,
    schemas,
    sources,
    timeline,
    utils,
)
from .client import EsajDatajudClient
from .config import EsajDatajudConfig
from .version import __version__

__all__ = [
    "EsajDatajudClient",
    "EsajDatajudConfig",
    "api",
    "cache",
    "client",
    "config",
    "datajud",
    "djen",
    "esaj",
    "exceptions",
    "extraction",
    "exports",
    "models",
    "normalization",
    "schemas",
    "sources",
    "timeline",
    "utils",
    "__version__",
]
