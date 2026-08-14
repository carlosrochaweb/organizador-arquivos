import os
import shutil

caminho_alvo = r"C:\\Users\\seu-user\\Downloads"

categorias = {
    "Documentos": [".pdf", ".doc", ".docx",".txt", ".xls", ".xlsx", ".psd", ".rtf", ".ppt", ".pptx", ".odt", ".ods", ".odp"],
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".bmp", ".tiff", ".avif", ".webp", ".heic"],
    "Vídeos": [".mp4", ".avi", ".mov","mkv","wmv", ".flv", ".webm", ".ogg"],
    "executaveis": [".exe", ".msi", ".bat", ".sh"],
    "Arquivos compactados": [".zip", ".rar", ".7z", ".001", ".tar", ".gz"],
    "Áudio": [".mp3", ".wav", ".flac"],
    "HTML": [".html", ".htm"],
    "CSS": [".css"],
    "Torrents": [".torrent"],
    "Imagem de Disco": [".iso"],
}

for arquivo in os.listdir(caminho_alvo):
    caminho_arquivo = os.path.join(caminho_alvo, arquivo)

    if os.path.isdir(caminho_arquivo):
        continue

    _, extensao = os.path.splitext(arquivo)

    movido = False
    
    for pasta, extensoes in categorias.items():
        if extensao.lower() in extensoes:
            pasta_destino = os.path.join(caminho_alvo, pasta)
            os.makedirs(pasta_destino, exist_ok=True)
            shutil.move(caminho_arquivo, os.path.join(pasta_destino, arquivo))
            movido = True
            break
