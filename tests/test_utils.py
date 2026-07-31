from esaj_datajud.utils import classificar_polo, limpar, nome_arquivo_seguro, normalizar_chave


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
