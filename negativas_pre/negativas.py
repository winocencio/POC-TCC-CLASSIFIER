import os
import cv2
import glob
import shutil

path = os.path.dirname(__file__)
dest_dir = path + "/../negativas/"

def moveNegativasComFiltro(a_process):
    numero_negativos_copiar = int(a_process.numero_negativos_treino)
    files = glob.glob("./negativas_pre/"+a_process.filtro+"/*.jpg")
    print("Iniciando transformação Imagens Negativas")
    print("Numero de negativas no total: " + str(len(files)))
    print("Numero de negativas para treino: " + a_process.numero_negativos_treino)
    count =0
    for file in files:
        count +=1
        if(count >= numero_negativos_copiar):
            break
        shutil.copy(file,dest_dir)
        print(percentile(count,int(a_process.numero_negativos_treino)) + " na transformação de imagens negativas", end="\r")
    print("")

def percentile(number1,number2):
    return '{0:.2f}%'.format((number1 / number2 * 100))