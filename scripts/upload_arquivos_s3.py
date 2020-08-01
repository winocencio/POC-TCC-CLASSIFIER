import tinys3
import os
from scripts.var import access as ACCESS

def uploadFiles(parametro):
    conn = tinys3.Connection(ACCESS.aws_access_key_id,ACCESS.aws_secret_access_key,tls=True)
    path = os.path.dirname(__file__)
    os.chdir('../classificador/' + parametro.versao_cascade_resumida())

    print("Realizando Upload de arquivos : ")
    print(os.getcwd())

    with open("cascade.xml",'rb') as cascade, open("params.xml",'rb') as params:
        conn.upload(parametro.versao_cascade_resumida()+"/cascade.xml",cascade,ACCESS.bucket_name)
        conn.upload(parametro.versao_cascade_resumida()+"/params.xml",params,ACCESS.bucket_name)
