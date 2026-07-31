from esaj_datajud.djen import _parse_data


def test_parse_data_iso():
    assert _parse_data({"data_disponibilizacao": "2026-07-30T10:00:00"}) == "2026-07-30"


def test_parse_data_brasileira():
    assert _parse_data({"datadisponibilizacao": "30/07/2026"}) == "2026-07-30"


def test_parse_data_vazia():
    assert _parse_data({}) == ""
