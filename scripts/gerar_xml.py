import os

#mudar parametros do bat e mudar o nome do XML que será gerado
def gerarXml(parametro):
    path = os.path.dirname(__file__)
    os.chdir(path)
    comando = parametro.sysOpComando.gerar_classificador_xml_arquivo + " " + parametro.args_classificador()
    print("Executando: " + comando)
    os.system(comando)