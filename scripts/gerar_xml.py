import os

#mudar parametros do bat e mudar o nome do XML que será gerado
def gerarXml(parametro,quantidade_memoria_usada):
    path = os.path.dirname(__file__)
    os.chdir(path)
    os.system(parametro.sysOpComando.gerar_classificador_xml_arquivo + " " + parametro.args_classificador()  + ' ' + quantidade_memoria_usada)