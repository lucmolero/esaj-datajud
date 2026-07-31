"""esaj_datajud package

Expose main modules:
- `api` : highest-level operations for lawyers and systems
- `esaj` : eSAJ extraction helpers
- `djen` : DJEN (DataJud) helpers
- `utils`: helper utilities
"""

from . import api, cache, client, config, djen, esaj, exceptions, models, utils
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
    "djen",
    "esaj",
    "exceptions",
    "models",
    "utils",
    "__version__",
]
