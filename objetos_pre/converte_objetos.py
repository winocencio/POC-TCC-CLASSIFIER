import os, os.path
import glob

path = os.path.dirname(__file__)
dest_dir = path + '../objetos/'
def moveObjetosComFiltro(a_process):
    numero_objetos = int(a_process.numero_objetos)
    files = glob.glob("./"+a_process.filtro+"/*.jpg")
    print("Iniciando movimento das Imagens de Objetos")
    print("Numero de objetos: " + a_process.numero_objetos)
    count =0
    for file in files:
        count +=1
        if(count >= numero_negativos_copiar):
            break
        shutil.copy(file,dest_dir)
        print(percentile(count,numero_objetos) + " na movimentação de imagens de objetos", end="\r")
    print("")