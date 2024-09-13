
cadena=[]

class LeerBD:
    def __init__(self, number: str,dayStart: str,dayDiet: str,load: str,horary: str):
        self.number = number
        self.dayStart = dayStart
        self.dayDiet = dayDiet
        self.load = load
        self.horary = horary
        
texto=open("/home/avila-brian/Desktop/pruebaLeerBD.txt", "r")

i=0

for line in texto.readlines():
    
    caravana=line[0:15]
    diaInicio=line[15:28]
    diaDieta=line[28:31]
    peso=line[31:35]
    hora=line[35:37]
    
    cadena.append(LeerBD(caravana,diaInicio,diaDieta,peso,hora))
    
    i=i+1
    #print(line)
    #if("112233010445566" in line):
    #    cadena.append(line)

#for cadenas in cadena:
    #caravana=cadenas[0:15]
    #num=LeerBD(caravana)    
    

for cadenas in cadena:
    print("el numero de caravana es:")
    print(cadenas.number)
    print("el dia de inicio de ciclo es:")
    print(cadenas.dayStart)
    print("el dia de inicio de dieta es:")
    print(cadenas.dayDiet)
    print("el peso:")
    print(cadenas.load)
    print("y la hora")
    print(cadena[0].horary)

texto.close()