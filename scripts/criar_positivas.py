import os
import os.path

path = os.path.dirname(__file__)

COMANDO_GERAR_LISTA_NEGATIVAS = 'dir /b "../negativas/*.jpg" > "../negativas/bg.txt"'
COMANDO_CRIAR_POSITIVA = 'start /wait ./openCV/opencv_createsamples -img ../objetos/{0}.png -bg ../negativas/bg.txt -info ../positivas/positivas{0}/positivas{0}.lst -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num {1} -bgcolor 255'
COMANDO_GERAR_VETOR_POSITIVO = 'start /wait ./openCV/opencv_createsamples -info ../positivas/positivas{0}/positivas{0}.lst -num {1} -w {2} -h {2} -vec ../vetores/positivas{0}.vec'
COMANDO_GERAR_VETOR_FINAL = 'python ./openCV/mergevec.py -v ../vetores -o ../vetores/vetor_final.vec'

def criarPositivas(parametro):
    os.chdir(path)
    os.system(COMANDO_GERAR_LISTA_NEGATIVAS)
    for i in range(1,int(parametro.numero_objetos)+1):
        print("Criando positivas:" + str(i) + " de " + parametro.numero_objetos)
        os.system(COMANDO_CRIAR_POSITIVA.format(i,parametro.numero_positivos_cada_objetos()))
        os.system(COMANDO_GERAR_VETOR_POSITIVO.format(i,parametro.numero_positivos_cada_objetos(),parametro.wh))



def gerarVetorFinal():
    print("Criando Vetor Final")
    os.chdir(path)
    os.system(COMANDO_GERAR_VETOR_FINAL)
