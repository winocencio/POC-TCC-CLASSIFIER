from negativas_pre.negativas import moveNegativasComFiltro
from objetos_pre.converte_objetos import moveObjetosComFiltro
from scripts.criar_positivas import criarPositivas ,  gerarVetorFinal
from scripts.gerar_xml import gerarXml
from scripts.model.To_Process import To_Process
from scripts.pastas import apagarPastas, criarPastas
from scripts.NoProcessException import NoProcessException
from scripts.upload_arquivos_s3 import uploadFiles
from scripts.model.Comando import Comando
import cv2
import sys
import os

def executar(quantidade_memoria_total,sistemaOperacional):
    try:
        print('Quantidade de memoria: ' + quantidade_memoria_total)
        print('Rodando no sistema: ' + sistemaOperacional.descricao)

        a_process = To_Process.getNext()
        a_process.setComando(sistemaOperacional)
        a_process.numero_total_mb_usado = quantidade_memoria_total
        print(dict(a_process))
        a_process.saveProcessando()

        criarPastas()

        #Move Negativas da pasta com filtros para pasta Negativas
        moveNegativasComFiltro(a_process)
        
        #Move Objeto da pasta com filtros para pasta objetos
        moveObjetosComFiltro(a_process)
        #Criando Positivas
        criarPositivas(a_process)
        gerarVetorFinal(a_process)

        #Iniciando o treinamento
        gerarXml(a_process)

        uploadFiles(a_process)
        
        #Limpando remanecentes
        #apagaObjetosPng()
        apagarPastas()
        a_process.saveFinalizado()

        print("Finalizado versao: " + a_process.versao_cascade_resumida())
    except NoProcessException:
        print("Sem argumentos disponiveis para processar")
        os.system('type nul > stop')
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