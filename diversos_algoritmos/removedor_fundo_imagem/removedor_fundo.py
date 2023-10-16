# Algoritmo simples para remover fundo da imagem.

# Instalar a biblioteca pelo terminal: pip install rembg

# Importando a biblioteca rembg e o módulo Image.
from PIL import Image
import rembg

# Caminho até o arquivo nas barras deve conter barras duplas (\\) semparando os diretórios.
img = Image.open('Color aqui o caminho até o arquivo.')
img.show() # Mostra a imagem armazenada.

# Remove o dundo da imagem.
img_fundo_removido = rembg.remove(img)
img_fundo_removido.show() # Retorna a imagem, sem fundo.

# Define o caminho para salvar a imagem sem fundo.
img_sem_fundo_path = 'C:\\caminho\\até\\o\\arquivo_sem_fundo.png'

# Salva a imagem sem fundo.
img_fundo_removido.save(img_sem_fundo_path)