import os
import shutil

pastasTemp = ['positivas','negativas','objetos','vetores']
path = os.path.dirname(__file__)
raizProjeto = os.path.dirname(path)

def apagarPastas():
    for pasta in pastasTemp:
        shutil.rmtree(os.path.join(raizProjeto, pasta))

def criarPastas():
    os.chdir(raizProjeto)
    for pasta in pastasTemp:
        os.mkdir(pasta)