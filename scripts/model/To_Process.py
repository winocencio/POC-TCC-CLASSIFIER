import os
from datetime import datetime
from ..var import access as ACCESS
from ..NoProcessException import NoProcessException
import getpass

from pynamodb.attributes import UnicodeAttribute, BooleanAttribute, UTCDateTimeAttribute
from pynamodb.models import Model

class To_Process(Model):
    class Meta:
        table_name = ACCESS.table_name
        region = ACCESS.region
        host = ACCESS.host
        aws_access_key_id = ACCESS.aws_access_key_id
        aws_secret_access_key = ACCESS.aws_secret_access_key

    id = UnicodeAttribute(hash_key=True, null=False)
    status = UnicodeAttribute(null=False,default="AGUARDANDO")
    numero_objetos = UnicodeAttribute(null=False)
    numero_negativos_treino = UnicodeAttribute(null=False)
    proporcao_negativos_para_positivos = UnicodeAttribute(null=False)
    numero_estagios = UnicodeAttribute(null=False)
    filtro = UnicodeAttribute(null=False)
    wh = UnicodeAttribute(null=False)
    numero_versao = UnicodeAttribute(null=False)
    #TODO colocar novos parametros
    createdAt = UTCDateTimeAttribute(null=False, default=datetime.now())
    createdBy = UnicodeAttribute(null=False, default=ACCESS.CreationUser)
    updatedAt = UTCDateTimeAttribute(null=False)
    updatedBy = UnicodeAttribute(null=False)
    result = UnicodeAttribute(null=False, default="-")
    featureType = UnicodeAttribute(null=False)
    boostType = UnicodeAttribute(null=False)
    mode = UnicodeAttribute(null=False)
    sysOpComando = 0
    sysOp = UnicodeAttribute(null=True)

    def setComando(self,comando):
        self.sysOpComando = comando
        self.sysOp = comando.descricao

    def saveFinalizado(self):
        self.status = "FINALIZADO"
        self.save()

    def saveProcessando(self):
        self.status = "PROCESSANDO"
        self.createdAt = datetime.now()
        self.save()

    def saveErro(self):
        self.status = "ERRO"
        self.save()
    
    def saveAguardando(self):
        self.status = "AGUARDANDO"
        self.save()

    def save(self, conditional_operator=None, **expected_values):
        self.updatedAt = datetime.now()
        self.updatedBy = getpass.getuser()
        super(To_Process, self).save()

    def getNext():
        results = To_Process.scan()
        results = list(filter(lambda result: result.status == "AGUARDANDO", results))
        results.sort(key=n_negativos)
        if len(results) == 0:
            raise NoProcessException("Sem argumentos para processar")

        a_process = results[0]
        a_process.saveProcessando()
        return a_process

    def numero_positivos_treino(self):
        return int(self.numero_negativos_treino) * int(self.proporcao_negativos_para_positivos)

    def numero_negativos_total(self):
        return self.numero_negativos_treino

    def numero_positivos_total(self):
        return self.numero_positivos_treino() * 1.125

    def numero_positivos_cada_objetos(self):
        return self.numero_positivos_total()/int(self.numero_objetos)

    def versao_cascade_resumida(self):
        return 'cascadeV{0}-{1}-0{2}'.format("0","5",str(self.numero_versao))

    def args_classificador(self):
        return '{0} {1} {2} {3} {4} {5} {6} {7}'.format(self.versao_cascade_resumida(),self.numero_positivos_treino(),self.numero_negativos_treino,self.wh,self.numero_estagios,self.featureType,self.mode,self.boostType)

    def filtro_cv(self):
        if(self.filtro == "GS"):
            return cv2.COLOR_BGR2GRAY
        
        return cv2.COLOR_BGR2RGB

    def __iter__(self):
        for name, attr in self._get_attributes().items():
            yield name, attr.serialize(getattr(self, name))

def n_negativos(e):
    return int(e.numero_negativos_treino)