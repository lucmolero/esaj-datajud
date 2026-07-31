import os
import subprocess
import sys
from pathlib import Path

from esaj_datajud import cli

ROOT = Path(__file__).parent.parent
SRC = ROOT / "src"


def test_cli_help():
    env = os.environ.copy()
    env.setdefault("PYTHONPATH", str(SRC))
    result = subprocess.run(
        [sys.executable, "-m", "esaj_datajud.cli", "--help"],
        env=env,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "Ferramenta profissional de linha de comando para eSAJ/TJSP e DJEN." in result.stdout


def test_cli_search_imprime_json(monkeypatch, capsys):
    monkeypatch.setattr(
        cli.api,
        "search_processo",
        lambda numero: {"status": "ok", "numero": numero},
    )

    status = cli.main(["search", "1076539-20.2019.8.26.0100"])

    assert status == 0
    assert '"status": "ok"' in capsys.readouterr().out
