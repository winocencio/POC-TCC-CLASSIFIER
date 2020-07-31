import json
import cv2
import os
from datetime import datetime 

path = os.path.dirname(__file__)

class Parametro:
    def __init__(self,numero_objetos,numero_negativos_treino,proporcao_negativos_para_positivos,numero_estagios,filtro,wh,path_arquivo_versao):
        self.numero_objetos = numero_objetos
        self.numero_negativos_treino = numero_negativos_treino
        self.proporcao_negativos_para_positivos = proporcao_negativos_para_positivos
        self.numero_estagios = numero_estagios
        self.filtro = filtro
        self.wh = wh
        self.numero_versao = 0
        self.path_arquivo_versao = path_arquivo_versao
        self.tempo_percorrido = datetime.now()

    def filtro_cv(self):
        if(self.filtro == "GS"):
            return cv2.COLOR_BGR2GRAY
        
        return cv2.COLOR_BGR2RGB
        
    def escrever_versao(self):
        self.tempo_percorrido = str(datetime.now() - self.tempo_percorrido)
        os.chdir(path)
        with open(self.path_arquivo_versao, 'r') as f:
            json_parametro = json.load(f)
            f.close()

        with open(self.path_arquivo_versao, 'w') as f:
            json_parametro.append(self.__dict__)
            f.write(json.dumps(json_parametro, indent=4))
            f.close()

        print('Tempo percorrido: {0}'.format(self.tempo_percorrido))

    def carregar_versao(self):
        os.chdir(path)
        with open(self.path_arquivo_versao, 'r') as f:
            json_parametro = json.load(f)
            self.numero_versao = json_parametro[-1]['numero_versao']+1
            f.close()
            

    def numero_positivos_treino(self):
        return self.numero_negativos_treino * self.proporcao_negativos_para_positivos

    def numero_negativos_total(self):
        return self.numero_negativos_treino

    def numero_positivos_total(self):
        return self.numero_positivos_treino() * 1.125

    def numero_positivos_cada_objetos(self):
        return self.numero_positivos_total()/self.numero_objetos
    
    def versao_cascade_resumida(self):
        return 'cascadeV{0}-{1}-0{2}'.format("0","5",str(self.numero_versao))

    def versao_cascade(self):
        return '{0}-{1}-{2}-{3}-{4}-{5}-{6}'.format(self.versao_cascade_resumida(),self.numero_objetos,self.numero_negativos_treino,self.proporcao_negativos_para_positivos,self.numero_estagios,self.filtro,self.wh)

    def args_classificador(self):
        return '{0} {1} {2} {3} {4}'.format(self.versao_cascade_resumida(),self.numero_positivos_treino(),self.numero_negativos_treino,self.wh,self.numero_estagios)

#parametro = Parametro(1,800,2,10,"GS",18)