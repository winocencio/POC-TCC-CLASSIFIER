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

    try:
        quantidade_memoria_usada = sys.argv[1]
    except Exception:
        print('Nao passado quantidade de memoria para o buffer, usado padrao (1024) ')
        quantidade_memoria_usada = '1024'

    criarPastas()

    #Move Negativas da pasta com filtros para pasta Negativas
    moveNegativasComFiltro(a_process)
    
    #Move Objeto da pasta com filtros para pasta objetos
    moveObjetosComFiltro(a_process)
    #Criando Positivas
    criarPositivas(a_process)
    gerarVetorFinal()

    #Iniciando o treinamento
    gerarXml(a_process,quantidade_memoria_usada)

    uploadFiles(a_process)
    
    #Limpando remanecentes
    #apagaObjetosPng()
    apagarPastas()
    a_process.saveFinalizado()

    print("Finalizado versão: " + a_process.versao_cascade_resumida())
except NoProcessException:
    print("Sem argumentos disponiveis para processar")
except Exception as e:
    print(e)
    print("Algo de errado ocorreu")
    try:
        apagarPastas()
    except Exception:
        print('')

    a_process.saveErro()
except KeyboardInterrupt:
    print("")
    print("Script Interrompido")
    apagarPastas()
    a_process.saveAguardando()
    sys.exit(0)