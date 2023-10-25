from pytube import YouTube
from os import system as cmd
from pytube import Playlist
import os
resolucao = []
opcoes = {
    "1": "Baixar video",
    "2": "Fazer Download do audio",
    "3": "Baixar playlist",
}

def baixar_video():
    while True:
        cmd('cls')
        url = input("Cole aqui a URL do vídeo desejado: ")
        yt = YouTube(url)
        print(f"Título do vídeo: {yt.title}")
        confirmacao = input("Deseja mesmo baixar esse vídeo? Digite '1' para sim e '2' para sair: ")
        
        if confirmacao == "1":
            resolution = input("Digite a resolução desejada (ex: 720p): ")
            video = yt.streams.filter(resolution=resolution).first()
            
            if video is not None:
                video.download('./midias')
                print("Download concluído!")
                break
            else:
                print(f"Nenhuma resolução disponível para '{resolution}'.")
    
def baixar_audio():
    while True:
        cmd('cls')
        url = input("Cole aqui a URL do vídeo desejado: ")
        yt = YouTube(url)
        print(f"Título do vídeo: {yt.title}")
        confirmacao = input("Deseja baixar esse áudio? Digite '1' para sim e '2' para não: ")
        if confirmacao == "1":
            yt.streams.get_audio_only().download("./midias", yt.title + ".mp3")
            print("Download do áudio concluído!")
            break
        else:
            print("Nenhum áudio disponível para download.")

def baixar_playlist():
    while True:
            cmd('cls')
            url = input("Cole aqui a URL do vídeo desejado: ")
            playlist = Playlist(url)
            print(f"Playlist: {playlist.title}")
            confirmacao = input("Deseja baixar esse vídeo? Digite '1' para sim e '2' para não: ")
                
            if confirmacao == "1":
                for video in playlist.videos:
                    video.streams.first().download("./midias")
                print("Baixado")
            break

    
while True:
        print("SnapTube2 Baixador de Video e de audio")
        for key, value in opcoes.items():
            print(f"{key}: {value}")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            baixar_video()
        elif escolha == "2":
            baixar_audio()
        elif escolha =="3":
            baixar_playlist()


        
        