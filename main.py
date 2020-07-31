from negativas_pre.negativas import transformaNegativas
from objetos_pre.converte_objetos import converteObjetos, apagaObjetosPng
from scripts.criar_positivas import criarPositivas ,  gerarVetorFinal
from scripts.gerar_xml import gerarXml
from scripts.model.To_Process import To_Process
from scripts.apagar_pastas import apagarPastasVetoresEPositivas,apagarPastasObjetosENegativos
import cv2

a_process = To_Process.getNext()
print(dict(a_process))

#Transforma negativas e coloca na nova pasta
transformaNegativas(cv2.COLOR_BGR2GRAY) # trocar para receber parametro

#transforma objetos e coloca na nova pasta
converteObjetos(a_process)

#Criando Positivas
criarPositivas(a_process)
gerarVetorFinal()

#Iniciando o treinamento
gerarXml(a_process)

#Limpando remanecentes
apagarPastasVetoresEPositivas()
apagarPastasObjetosENegativos()
#apagaObjetosPng()
#Finalização -> Enviando resultado para o S3 e registrando
#ENVIAR RESULTADO PARA O S3

a_process.saveFinalizado()