from negativas_pre.negativas import transformaNegativas
from objetos_pre.converte_objetos import converteObjetos, moveObjetos
from scripts.criar_positivas import criarPositivas ,  gerarVetorFinal
from scripts.gerar_xml import gerarXml
from scripts.Parametro import Parametro
from scripts.apagar_pastas import apagarPastasVetoresEPositivas
import cv2

parametro = Parametro(2,2500,2,10,"GS",18,"parametro.json")
parametro.carregar_versao()
# print(parametro.numero_versao)
# print(parametro.path_arquivo_versao)

# QTD_OBJETOS = 2
# QTD_POSITIVO = 1800
# QTD_POSITIVOS_CADA_OBJETOS = QTD_POSITIVO/QTD_OBJETOS
# VERSAO_XML = "V3-02"

#Transforma negativas e coloca na nova pasta
# transformaNegativas(cv2.COLOR_BGR2GRAY) # trocar para receber parametro

#transforma objetos e coloca na nova pasta
#converteObjetos()
#moveObjetos()


criarPositivas(parametro)
gerarVetorFinal()
gerarXml(parametro)
apagarPastasVetoresEPositivas()

parametro.escrever_versao()