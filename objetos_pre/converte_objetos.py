import os, os.path

COMANDO_CONVERTER = 'magick convert {0}.png -alpha background -background white {0}.jpg'
COMANDO_MOVER = 'copy "../objetos_pre/*.jpg" "../objetos"'

path = os.path.dirname(__file__)
def converteObjetos():
    os.chdir(path)
    for i in range(1,51):
        print("Executando: "+COMANDO_CONVERTER.format(str(i)))
        os.system(COMANDO_CONVERTER.format(str(i)))

def moveObjetos():
    os.chdir(path)
    os.system(COMANDO_MOVER)