import os, os.path
import cv2

COMANDO_CONVERTER = 'cd ../objetos & magick convert {0}.png -alpha background -background white {0}.jpg'
COMANDO_MOVER = 'cd 1 & copy "./*.png" "../../objetos""'
COMANDO_APAGAR = 'cd ../objetos & del *.png"'

path = os.path.dirname(__file__)
def converteObjetos(parametro):
    print("Iniciando Conversão de objetos")
    os.chdir(path)
    #adicionafiltroNaImagem(parametro) Esse cara aqui tem que ser avaliado, por enquanto está sendo substituido pelo moveObjetos
    moveObjetos()
    converteParaJpg(int(parametro.numero_objetos))

def adicionafiltroNaImagem(parametro):
    os.chdir(path)
    for i in range(1,int(parametro.numero_objetos)+1):
        nome_img = str(i)+'.png'
        img = getImagem(nome_img)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        gravaImagem(img,nome_img)

def gravaImagem(img,nome):
    cv2.imwrite(path + "/../objetos/" + nome, img)
        
def getImagem(nome):
    return cv2.imread(path + '/1/' + nome)

def converteParaJpg(numero_objetos):
    for i in range(1,numero_objetos+1):
        print("Executando: "+COMANDO_CONVERTER.format(str(i)))
        os.system(COMANDO_CONVERTER.format(str(i)))

def moveObjetos():
    os.chdir(path)
    os.system(COMANDO_MOVER)

def apagaObjetosPng():
    os.chdir(path)
    os.system(COMANDO_APAGAR)