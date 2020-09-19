import enum

class ComandoEnumMeta(enum.EnumMeta):
    def __new__(mcs, name, bases, attrs):
        obj = super().__new__(mcs, name, bases, attrs)
        obj._value2member_map_ = {}
        for m in obj:
            value, descricao, gerar_lista_negativas , criar_positiva, gerar_vetor_positivo , gerar_vetor_final , gerar_classificador_xml_arquivo = m.value
            m._value_ = value
            m.descricao = descricao
            m.gerar_lista_negativas = gerar_lista_negativas
            m.criar_positiva = criar_positiva
            m.gerar_vetor_positivo = gerar_vetor_positivo
            m.gerar_vetor_final = gerar_vetor_final
            m.gerar_classificador_xml_arquivo = gerar_classificador_xml_arquivo
            obj._value2member_map_[value] = m

        return obj

class Comando(enum.Enum, metaclass=ComandoEnumMeta):
    WINDOWS = 1,'WINDOWS','dir /b "../negativas/*.jpg" > "../negativas/bg.txt"' , 'start /wait ./openCV/opencv_createsamples -img ../objetos/{0}.png -bg ../negativas/bg.txt -info ../positivas/positivas{0}/positivas{0}.lst -maxidev 20 -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num {1} -bgcolor 255' , 'start /wait ./openCV/opencv_createsamples -info ../positivas/positivas{0}/positivas{0}.lst -num {1} -w {2} -h {2} -vec ../vetores/positivas{0}.vec' , 'python ./openCV/mergevec.py -v ../vetores -o ../vetores/vetor_final.vec' , 'gerar-classificador-xml.bat'
    LINUX = 2,'LINUX','ls -l "../negativas/*.jpg" > "../negativas/bg.txt"','opencv_createsamples -img ../objetos/{0}.png -bg ../negativas/bg.txt -info ../positivas/positivas{0}/positivas{0}.lst -maxidev 20 -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num {1} -bgcolor 255' ,'wait opencv_createsamples -info ../positivas/positivas{0}/positivas{0}.lst -num {1} -w {2} -h {2} -vec ../vetores/positivas{0}.vec' ,'python ./openCV/mergevec.py -v ../vetores -o ../vetores/vetor_final.vec' ,'bash gerar-classificador-xml.sh'
