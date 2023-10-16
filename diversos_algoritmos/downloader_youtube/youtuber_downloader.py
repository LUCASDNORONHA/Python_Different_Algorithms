# Algoritmo simples para download de vídeos do Youtube.


# Lembre-se de instalar na sua maquina, a bibliblioteca pytube.
# Para instalar, copier e cole no seu terminar: !pip import pytube
from pytube import YouTube
import os

# Obtém informações do vídeo em um objeto do tipo Youtube.
youtube = YouTube(input('Cole o link: '))

# Define o diretório onde os vídeos serão baixados.
# Escreva o caminho do seu diretório dentro das aspas com barra duplass \\.
pasta = "C:\\Users\\lucas\\Downloads"


# Recupera a maior resolução disponível para o video.
video = youtube.streams.get_highest_resolution()

# Realiza o download do vídeo na pasta definida.
video.download(output_path = pasta)


# Fim