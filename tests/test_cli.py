import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
SRC = ROOT / "src"


def test_cli_help():
    env = os.environ.copy()
    env.setdefault("PYTHONPATH", str(SRC))
    result = subprocess.run([sys.executable, "-m", "esaj_datajud.cli", "--help"], env=env, capture_output=True, text=True)
    assert result.returncode == 0
    assert "Ferramenta de linha de comando para eSAJ e DJEN." in result.stdout
