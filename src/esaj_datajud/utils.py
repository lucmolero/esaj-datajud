"""Utility helpers for esaj_datajud."""
import re
import unicodedata


def limpar(texto: str) -> str:
    return re.sub(r"\s+", " ", (texto or "")).strip()


def nome_arquivo_seguro(texto: str, fallback: str = "processo") -> str:
    nome = re.sub(r"[^A-Za-z0-9_.-]", "_", limpar(texto))
    nome = re.sub(r"_+", "_", nome).strip("_.")
    return nome or fallback


def normalizar_chave(texto: str) -> str:
    chave = unicodedata.normalize("NFKD", limpar(texto))
    chave = "".join(ch for ch in chave if not unicodedata.combining(ch)).lower()
    return re.sub(r"[^a-z0-9]+", "_", chave).strip("_")

POLOS_ATIVOS = {
    "autor",
    "autora",
    "requerente",
    "reqte",
    "reqnte",
    "exequente",
    "exeqte",
    "credor",
    "credora",
    "embargante",
    "embargte",
    "impetrante",
    "apelante",
    "agravante",
    "reclamante",
    "justica_publica",
    "ministerio_publico",
    "ministerio_publico_do_estado_de_sao_paulo",
}

POLOS_PASSIVOS = {
    "reu",
    "re",
    "requerido",
    "requerida",
    "reqdo",
    "reqda",
    "executado",
    "executada",
    "exectdo",
    "exectda",
    "devedor",
    "devedora",
    "embargado",
    "embargada",
    "embargdo",
    "embargda",
    "averiguado",
    "averiguada",
    "falido",
    "falida",
    "impetrado",
    "impetrada",
    "apelado",
    "apelada",
    "agravado",
    "agravada",
    "reclamado",
    "reclamada",
    "indiciado",
    "indiciada",
    "acusado",
    "acusada",
    "querelado",
    "querelada",
    "denunciado",
    "denunciada",
}


def classificar_polo(tipo: str) -> str | None:
    tipo_normalizado = normalizar_chave(tipo)
    if tipo_normalizado in POLOS_ATIVOS:
        return "ativo"
    if tipo_normalizado in POLOS_PASSIVOS:
        return "passivo"
    return None


def adicionar_unico(lista: list, valor: str) -> None:
    if valor and valor not in lista:
        lista.append(valor)
