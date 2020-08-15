from negativas_pre.negativas import moveNegativasComFiltro
from objetos_pre.converte_objetos import moveObjetosComFiltro
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

    #Move Negativas da pasta com filtros para pasta Negativas
    moveNegativasComFiltro(a_process)
    
    #Move Objeto da pasta com filtros para pasta objetos
    moveObjetosComFiltro(a_process)
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
    apagarPastas()
    a_process.saveErro()
except KeyboardInterrupt:
    print("")
    print("Script Interrompido")
    apagarPastas()
    a_process.saveAguardando()
    sys.exit(0)