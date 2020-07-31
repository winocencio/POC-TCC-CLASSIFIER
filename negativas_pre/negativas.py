import os, os.path
import cv2


numero_imagens = len(os.listdir('./negativas_pre/1'))
print("Numero de negativas no total: ",numero_imagens)
path = os.path.dirname(__file__)

def transformaNegativas(filtro):
    print("Iniciando transformação Imagens Negativas")
    for numero_atual in range(1,numero_imagens):
        #adicionar um try catch aqui
        nome_img = "neg("+str(numero_atual) + ").jpg"
        img = getImagem(nome_img)
        img = cv2.cvtColor(img,filtro)
        gravaImagem(img,nome_img)

def getImagem(nome):
    return cv2.imread(path + '/1/' + nome)

def gravaImagem(img,nome):
    cv2.imwrite(path + "/../negativas/" + nome, img)