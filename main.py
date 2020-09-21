from scripts.model.Comando import Comando
from scripts.model.To_Process import To_Process
from scripts.NoProcessException import NoProcessException
from pathlib import Path
from runner import executar
import sys

try:
    quantidade_memoria_total = sys.argv[1]
except Exception:
    print('Nao especificado quantidade de memoria para uso')
    raise NoProcessException('Nao especificado quantidade de memoria para uso')
    sys.exit(0)

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
    sys.exit(0)

try:
    executar(quantidade_memoria_total,sistemaOperacional)
except Exception as e:
    print(e)
    print("Algo de errado ocorreu --> MAIN")