import os

def apagarPastasVetoresEPositivas():
    path = os.path.dirname(__file__)
    os.chdir(path)
    os.system("apagar-pastas-vetores-positivos.bat")