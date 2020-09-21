from scripts.model.Comando import Comando
from scripts.model.To_Process import To_Process
from scripts.NoProcessException import NoProcessException
from pathlib import Path
from runner import executar
import sys
import os.path

try:
    try:
        quantidade_memoria_total = sys.argv[1]
        quantidade_memoria_usada = int(quantidade_memoria_total)/2
    except Exception:
        print('Nao especificado quantidade de memoria para uso')
        raise NoProcessException('Nao especificado quantidade de memoria para uso')

    try:
        sistemaOperacional = sys.argv[2]
        if(sistemaOperacional == 'WIN'):
            sistemaOperacional = Comando.WINDOWS
        elif(sistemaOperacional == 'LIN'):
            sistemaOperacional = Comando.LINUX
        else:
            raise Exception()
    except Exception:
        print('Nao especificado Sistema Operacional')
        raise NoProcessException('Nao especificado Sistema Operacional')

    contadorDeExecucoes = 0
    print('Executando Watch')
    while not os.path.exists('stop'):
        contadorDeExecucoes = contadorDeExecucoes +1
        print('Iniciando watch numero: '+ str(contadorDeExecucoes))
        executar(quantidade_memoria_total,sistemaOperacional)
    else:
        print('Arquivo STOP criado.')
        
except Exception as e:
    print(e)
    print("Algo de errado ocorreu --> WATCH")