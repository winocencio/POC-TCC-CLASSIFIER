from negativas_pre.negativas import transformaNegativas
from objetos_pre.converte_objetos import converteObjetos, apagaObjetosPng
from scripts.criar_positivas import criarPositivas ,  gerarVetorFinal
from scripts.gerar_xml import gerarXml
from scripts.model.To_Process import To_Process
from scripts.pastas import apagarPastas, criarPastas
from scripts.NoProcessException import NoProcessException
from scripts.upload_arquivos_s3 import uploadFiles
import cv2
import sys

try:
    a_process = To_Process.getNext()
    print(dict(a_process))

    criarPastas()
    #Transforma negativas e coloca na nova pasta
    transformaNegativas(a_process) # trocar para receber parametro

    #transforma objetos e coloca na nova pasta
    converteObjetos(a_process)

    #Criando Positivas
    criarPositivas(a_process)
    gerarVetorFinal()

    #Iniciando o treinamento
    gerarXml(a_process)

    #Limpando remanecentes
    apagarPastas()
    #apagaObjetosPng()
    
    uploadFiles(a_process)
    a_process.saveFinalizado()

    print("Finalizado versão: " + a_process.versao_cascade_resumida())
except NoProcessException:
    print("Sem argumentos disponiveis para processar")
except Exception as e:
    print(e)
    print("Algo de errado ocorreu")
    a_process.saveErro()
except KeyboardInterrupt:
    print("")
    print("Script Interrompido")
    a_process.saveAguardando()
    sys.exit(0)