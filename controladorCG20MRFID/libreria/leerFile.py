class DatosAnimal:
    def __init__(self, number: str,dayStart: str,dayDiet: str,load: str,horary: str,eat: str,dispensed: str):
        self.number = number
        self.dayStart = dayStart
        self.dayDiet = dayDiet
        self.load = load
        self.horary = horary
        self.eat = eat
        self.dispensed = dispensed
   
   
def LeerDatoAnimal():
    
    nutricion=[]
    texto=open("/home/avila-brian/Desktop/pegasus1/archivos/datoAnimal.txt", "r")

    for line in texto.readlines():
    
        caravana=line[0:15]
        diaInicio=line[15:28]
        diaDieta=line[28:31]
        peso=line[31:35]
        hora=line[35:37]
        comido=line[37:38]
        dispensado=line[38:51]
    
        nutricion.append(DatosAnimal(caravana,diaInicio,diaDieta,peso,hora,comido,dispensado))
    
    texto.close()

    return nutricion