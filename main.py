from negativas_pre.negativas import transformaNegativas
from objetos_pre.converte_objetos import converteObjetos, moveObjetos , apagaObjetosPastaOrigem
from scripts.criar_positivas import criarPositivas ,  gerarVetorFinal
from scripts.gerar_xml import gerarXml
from scripts.Parametro import Parametro
from scripts.apagar_pastas import apagarPastasVetoresEPositivas,apagarPastasObjetosENegativos
import cv2

parametro = Parametro(50,100,2,10,"GS",18,"parametro.json")
parametro.carregar_versao()

#Transforma negativas e coloca na nova pasta
transformaNegativas(cv2.COLOR_BGR2GRAY) # trocar para receber parametro

#transforma objetos e coloca na nova pasta
converteObjetos()
moveObjetos()
apagaObjetosPastaOrigem()

#Criando Positivas
criarPositivas(parametro)
gerarVetorFinal()

#Iniciando o treinamento
gerarXml(parametro)

#Limpando remanecentes
apagarPastasVetoresEPositivas()
apagarPastasObjetosENegativos()

#Finalização -> Enviando resultado para o S3 e registrando
#ENVIAR RESULTADO PARA O S3


parametro.escrever_versao()