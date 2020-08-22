import os, os.path
import glob
import shutil

path = os.path.dirname(__file__)
dest_dir = path + '/../objetos/'

def sortKeyFunc(s):
    return int(os.path.basename(s)[:-4])

def moveObjetosComFiltro(a_process):
    numero_objetos = int(a_process.numero_objetos)
    files = glob.glob("./objetos_pre/"+a_process.filtro+"/*.png")
    print("Iniciando movimento das Imagens de Objetos")
    print("Numero de objetos: " + a_process.numero_objetos)
    count =0
    files.sort(key=sortKeyFunc)
    for file in files:
        count +=1
        if(count > numero_objetos):
            break
        shutil.copy(file,dest_dir)
        print(percentile(count,numero_objetos) + " na movimentação de imagens de objetos", end="\r")
    print("")

def percentile(number1,number2):
    return '{0:.2f}%'.format((number1 / number2 * 100))