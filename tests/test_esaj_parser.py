from pathlib import Path

from bs4 import BeautifulSoup

from esaj_datajud import esaj

FIXTURE = Path(__file__).parent / "fixtures" / "esaj_processo_basico.html"


def _soup() -> BeautifulSoup:
    return BeautifulSoup(FIXTURE.read_text(encoding="utf-8"), "html.parser")


def test_montar_url_busca_valida_numero_cnj():
    url = esaj.montar_url_busca("1076539-20.2019.8.26.0100")

    assert "numeroDigitoAnoUnificado=1076539-20.2019" in url
    assert "foroNumeroUnificado=0100" in url


def test_montar_url_busca_rejeita_numero_invalido():
    try:
        esaj.montar_url_busca("numero-invalido")
    except ValueError as exc:
        assert "CNJ" in str(exc)
    else:
        raise AssertionError("Número CNJ inválido deveria gerar ValueError")


def test_extrair_dados_basicos_da_fixture():
    dados = esaj.extrair_dados_basicos(_soup(), "https://example.test/processo")

    assert dados["numero"] == "1076539-20.2019.8.26.0100"
    assert dados["classe"] == "Ação Civil Pública"
    assert dados["campos_rotulados"]["assunto"] == "Meio Ambiente"
    assert dados["campos_rotulados"]["foro"] == "Foro Central Cível"


def test_extrair_partes_classifica_polos():
    partes = esaj.extrair_partes(_soup())

    assert partes["polo_ativo"][0]["nomes"] == ["Empresa Autora S/A"]
    assert partes["polo_passivo"][0]["nomes"] == ["Empresa Ré Ltda"]
    assert "OAB/SP 123456" in partes["polo_ativo"][0]["advogados"][0]


def test_extrair_movimentacoes_preserva_ordem_e_texto():
    movimentacoes = esaj.extrair_movimentacoes(_soup())

    assert len(movimentacoes) == 2
    assert movimentacoes[0]["ordem"] == 1
    assert movimentacoes[0]["data"] == "29/07/2026"
    assert movimentacoes[0]["titulo"] == "Publicação de intimação"
    assert movimentacoes[1]["texto"] == "Conclusos para decisão"
