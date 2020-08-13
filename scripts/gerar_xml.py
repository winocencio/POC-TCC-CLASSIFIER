import os

#mudar parametros do bat e mudar o nome do XML que será gerado
def gerarXml(parametro):
    path = os.path.dirname(__file__)
    os.chdir(path)
    os.system("gerar-classificador-xml.bat " + parametro.args_classificador())