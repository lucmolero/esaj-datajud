from esaj_datajud.exceptions import FormatoCNJInvalido
from esaj_datajud.utils import (
    classificar_polo,
    limpar,
    nome_arquivo_seguro,
    normalizar_chave,
    normalizar_numero_cnj,
    validar_numero_cnj,
)


def test_limpar_normaliza_espacos():
    assert limpar("  texto\n com\t espaços  ") == "texto com espaços"


def test_normalizar_chave_remove_acentos_e_pontuacao():
    assert normalizar_chave("Última movimentação:") == "ultima_movimentacao"


def test_nome_arquivo_seguro_remove_caracteres_perigosos():
    assert nome_arquivo_seguro("Ação / Processo nº 1") == "A_o_Processo_n_1"


def test_classificar_polo():
    assert classificar_polo("Autor") == "ativo"
    assert classificar_polo("Réu") == "passivo"
    assert classificar_polo("Terceiro interessado") is None


def test_normalizar_e_validar_numero_cnj():
    numero = normalizar_numero_cnj("10765392020198260100")

    assert numero == "1076539-20.2019.8.26.0100"
    assert validar_numero_cnj(numero) == numero


def test_validar_numero_cnj_rejeita_digito_invalido():
    try:
        validar_numero_cnj("1076539-21.2019.8.26.0100")
    except FormatoCNJInvalido as exc:
        assert "Dígito" in str(exc)
    else:
        raise AssertionError("Dígito inválido deveria gerar FormatoCNJInvalido")
