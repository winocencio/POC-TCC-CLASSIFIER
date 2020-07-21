import os, os.path
import cv2

# from '../objetos_pre/converte_objetos.py' import converte_objetos
#1-pegar imagens negativas_pre e adicionar o filtro correto nelas
#2-mover imagens com o filtro de negativas_pre > negativas


#3-pegar objetos_pre e transformar em fundo branco jpg (TESTAR MELHOR FORMA)
# converte_objetos.execute()

#4-mover objetos_jpg para objetos
os.system("../batch/mover_objetos_jpg.bat")

#5-criar positivas_pre com "objetos" e "negativas_pre"
#6-pegar imagens positivas_pre e adicionar o filtro correto nelas
#7-mover imagens com o filtro de positiva_pre > positivas