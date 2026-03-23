import yt_dlp
import subprocess
import os


def baixar_youtube(url, pasta_destino="downloads"):
    """
    o yt-dlp para extrair o melhor áudio disponível e converter para WAV usando FFmpeg.
    """
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    print(f"\n[*] Iniciando o download do áudio...\nURL: {url}")

    opcoes_ydl = {
        'format': 'bestaudio/best',
        'outtmpl': f'{pasta_destino}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'quiet': False,
        'noplaylist': True
    }

    try:
        with yt_dlp.YoutubeDL(opcoes_ydl) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            nome_arquivo = ydl.prepare_filename(info_dict)
            caminho_wav = nome_arquivo.rsplit('.', 1)[0] + '.wav'

        print(f"\n[+] Download concluído: {caminho_wav}")
        return caminho_wav
    except Exception as e:
        print(f"\n[-] Erro durante o download: {e}")
        return None


def separar_instrumentos(caminho_audio, pasta_saida="backing_tracks"):
    """
    usa IA do Demucs para separar o áudio em stems.
    """
    print(f"\n[*] Iniciando a separação de áudio com Demucs...")
    print("[!] A barra de progresso vai aparecer abaixo. Deixe a magia acontecer!\n")

    comando = [
        "demucs",
        "--out", pasta_saida,
        caminho_audio
    ]

    resultado = subprocess.run(comando)

    if resultado.returncode == 0:
        print("\n[+] Separação concluída com sucesso!")
        print(f"[*] Suas faixas separadas (Voz, Bateria, Baixo, Outros) estão na pasta:\n -> {pasta_saida}")
    else:
        print("\n[-] Erro ao separar o áudio com o Demucs.")


# ======================
# Fluxo Principal
# ======================
if __name__ == "__main__":
    print("=== GERADOR DE BACKING TRACKS COM IA ===")
    url_musica = input("Cole o link do YouTube da música: ")

    if "youtube.com" in url_musica or "youtu.be" in url_musica:
        arquivo_baixado = baixar_youtube(url_musica)

        # Se o download deu certo, manda para a IA
        if arquivo_baixado and os.path.exists(arquivo_baixado):
            separar_instrumentos(arquivo_baixado)
    else:
        print("\n[-] Link não reconhecido. Por favor, cole um link válido do YouTube.")