class DatosAnimal:
    def __init__(self, number: str,dayStart: str,dayDiet: str,load: str,horary: str):
        self.number = number
        self.dayStart = dayStart
        self.dayDiet = dayDiet
        self.load = load
        self.horary = horary


def LeerRegistroAnimal():
    
    registro=[]
    texto=open("/home/avila-brian/Desktop/pegasus1/archivos/datoReal.txt", "r")

    for line in texto.readlines():
    
        caravana=line[0:15]
        diaInicio=line[15:28]
        diaDieta=line[28:31]
        peso=line[31:35]
        hora=line[35:37]
        comido=0
    
        registro.append(DatosAnimal(caravana,diaInicio,diaDieta,peso,hora,comido))
    
    texto.close()

    return registro