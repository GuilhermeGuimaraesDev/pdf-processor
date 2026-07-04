import hashlib
import os
import fitz


# ==========================
# Configurações
# ==========================

MAX_FILE_SIZE_MB = 20


# ==========================
# Funções auxiliares
# ==========================

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


# ==========================
# Análise de Segurança
# ==========================

def analisar_pdf(caminho_pdf):
    tamanho = obter_tamanho_mb(caminho_pdf)
    sha256 = calcular_sha256(caminho_pdf)

    documento = fitz.open(caminho_pdf)

    page_count = documento.page_count
    encrypted = documento.is_encrypted
    metadata = documento.metadata

    documento.close()

    checks = {
        "sha256": sha256,
        "size_mb": tamanho,
        "page_count": page_count,
        "encrypted": encrypted,
        "metadata": metadata,
    }

    # ======================
    # SCORE
    # ======================
    score = 100
    aprovado = True
    reason = "Arquivo aprovado."

    # criptografia
    if encrypted:
        score -= 40
        aprovado = False
        reason = "PDF criptografado detectado."

    # páginas excessivas
    if page_count > 150:
        score -= 10
        score -= 40
        aprovado = False
        reason = "Documento muito grande (possível risco)."

    elif page_count > 50:
         score -= 25

    elif page_count > 10:
        score -= 10

    # metadados básicos ausentes
    if not metadata.get("author") or not metadata.get("creator"):
        score -= 10

    # segurança final
    if score < 60:
        aprovado = False
        reason = "Arquivo considerado suspeito pelo sistema."

    return {
        "approved": aprovado,
        "score": score,
        "reason": reason,
        "checks": checks
    }