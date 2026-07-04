import hashlib
import os


def calcular_sha256(caminho_pdf):
    sha256 = hashlib.sha256()

    with open(caminho_pdf, "rb") as arquivo:
        while True:
            bloco = arquivo.read(4096)

            if not bloco:
                break

            sha256.update(bloco)

    return sha256.hexdigest()


def obter_tamanho_mb(caminho_pdf):
    tamanho_bytes = os.path.getsize(caminho_pdf)
    return round(tamanho_bytes / (1024 * 1024), 2)


def analisar_pdf(caminho_pdf):
    tamanho = obter_tamanho_mb(caminho_pdf)
    sha256 = calcular_sha256(caminho_pdf)

    aprovado = True
    motivo = "Arquivo aprovado."

    if tamanho > 20:
        aprovado = False
        motivo = "Arquivo maior que 20 MB."

    return {
        "approved": aprovado,
        "reason": motivo,
        "size_mb": tamanho,
        "sha256": sha256,
    }