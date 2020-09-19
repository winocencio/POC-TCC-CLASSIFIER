# POC-TCC-CLASSIFIER
Criação do classificador de ovos de mosquito da dengue

TODO 13/08:

- [X] Merge branch secundaria com o master
- [X] Criar Readme com tasks
- [X] Criar pastas de filtro de objeto  
- [X] Criar script para baixar negativas_pre  
- [X] Criar script para baixar dependencias do projeto  
- [X] Criar script para criar pasta no inicio da execucao
- [X] apagar pastas utilizando o python
- [X] Modificar script para aceitar objetos em pastas de filtros  
- [X] Adicionar objetos GS  
- [X] Adicionar parametro para receber quantidade de memoria no main.py
- [X] Verificar parametro de criação de positivas (angulo)
- [X] Modificar script para que seja possivel rodar em linux 
- [ ] Realizar testes no linux
- [X] adicionar conta da memoria, para o usuario do mainpy nao precisar fazer calculo
- [ ] link do resultado no banco
- [X] nome vindo do access.py para o log do dinamoDB
- [X] gravar memoria usada no banco
- [ ] Adicionar negativas TRUNC  
- [ ] Adicionar objetos TRUNC  
- [ ] Criar script para baixar objetos_pre  
- [ ] Adicionar validacao de proporcao de criacao de positivas  
- [ ] Remover arquivos .jpg e .png do projeto com gitignore  
- [ ] Mudar print para logging para debugar no linux
- [ ] Adicionar Thread nos parametros
- [ ] Adicionar argumentos de cl por variaveis e nao por sequencia

ARGUMENTO para o MAIN.py

python main.py {quantidadeDeMemoria} {sistemaOperacional}

quantidadeDeMemoria:
    Obrigatorio
    quantidade de memoria total que será usado para o buffer do haarcascade
    valor recomendado: 2048 (2Gb alocado para o treinamento)

sistemaOperacional:
    Obrigatorio
    opcoes:
        WIN -> para sistema operacional windows
        LIN -> para sistema operacional linux

threads: TODO
    IMPLEMENTAR, hoje é usado o numero é especificado pelo OpenCv no treinamento do haarcascade
