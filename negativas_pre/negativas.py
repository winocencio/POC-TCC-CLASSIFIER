import os, os.path
import cv2


numero_imagens = len(os.listdir('./negativas_pre'))
print(numero_imagens)
path = os.path.dirname(__file__)

def transformaNegativas(filtro):
    for numero_atual in range(1,numero_imagens):
        #adicionar um try catch aqui
        nome_img = "neg("+str(numero_atual) + ").jpg"
        img = getImagem(nome_img)
        img = cv2.cvtColor(img,filtro)
        gravaImagem(img,nome_img)
        print(nome_img + " finalizado.")

def getImagem(nome):
    return cv2.imread(path + '/' + nome)

def gravaImagem(img,nome):
    cv2.imwrite(path + "/../negativas/" + nome, img)