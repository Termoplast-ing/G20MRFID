class DatosAnimal:
    def __init__(self, number: str,dayStart: str,dayDiet: str,load: str,horary: str,eat: str,dispensed: str):
        self.number = number
        self.dayStart = dayStart
        self.dayDiet = dayDiet
        self.load = load
        self.horary = horary
        self.eat = eat
        self.dispensed = dispensed

class DatosAlarmas:
    def __init__(self, type: str, number:str, hour:str):
        self.type = type
        self.number = number
        self.hour = hour

import os

def GuardarDatoReal(Caravana):
    
    texto=open("/home/Termoplast/Desktop/proyectos/CG20MRFID/controlador/software/controladorCG20MRFID/archivos/datoAnimal.txt", "w")

    for i in range(len(Caravana)):

        texto.write(str(Caravana[i].number)+str(Caravana[i].dayStart)+str(Caravana[i].dayDiet)+str(Caravana[i].load)+str(Caravana[i].horary)+str(Caravana[i].eat)+str(Caravana[i].dispensed+"\n"))
    
    texto.close()

    texto=open("/home/Termoplast/Desktop/proyectos/CG20MRFID/controlador/software/controladorCG20MRFID/archivos/datoAnimal.txt", "r")

    nutricion=[]

    for line in texto.readlines():
    
        caravana=line[0:15]
        diaInicio=line[15:28]
        diaDieta=line[28:31]
        peso=line[31:35]
        hora=line[35:37]
        comido=line[37:38]
        dispensado=line[38:51]
        if((dispensado=="\n") or (dispensado=="")):
            dispensado='0000000000000'
    
        nutricion.append(DatosAnimal(caravana,diaInicio,diaDieta,peso,hora,comido,dispensado))
    
    texto.close()

    return nutricion

def LeerDatoAnimal():

    nutricion=[]
    texto=open("/home/Termoplast/Desktop/proyectos/CG20MRFID/controlador/software/controladorCG20MRFID/archivos/datoAnimal.txt", "r")

    for line in texto.readlines():
    
        caravana=line[0:15]
        diaInicio=line[15:28]
        diaDieta=line[28:31]
        peso=line[31:35]
        hora=line[35:37]
        comido=line[37:38]
        dispensado=line[38:51]
        if((dispensado=="\n") or (dispensado=="")):
            dispensado='0000000000000'
    
        nutricion.append(DatosAnimal(caravana,diaInicio,diaDieta,peso,hora,comido,dispensado))
    
    texto.close()

    return nutricion

def GuardarAlarmas(alarmas):
    
    texto=open("/home/Termoplast/Desktop/proyectos/CG20MRFID/controlador/software/controladorCG20MRFID/archivos/Alarmas.txt", "w")

    for i in range(len(alarmas)):

        texto.write(str(alarmas[i].type)+str(alarmas[i].number)+str(alarmas[i].hour+"\n"))
    
    texto.close()

    readAlarmas=[]
    
    texto=open("/home/Termoplast/Desktop/proyectos/CG20MRFID/controlador/software/controladorCG20MRFID/archivos/Alarmas.txt", "r")

    for line in texto.readlines():
    
        tipo=line[0:1]
        numero=line[1:16]
        horario=line[16:29]
        if((horario=="\n") or (horario=="")):
            horario='0000000000000'
    
        readAlarmas.append(DatosAlarmas(tipo,numero,horario))
    
    texto.close()

    #readAlarmas.append(alarmas)

    return readAlarmas

def GuardarLineaAlarmas(alarma):

    texto=open("/home/Termoplast/Desktop/proyectos/CG20MRFID/controlador/software/controladorCG20MRFID/archivos/Alarmas.txt", "a")

    texto.write(str(alarma.type)+str(alarma.number)+str(alarma.hour)+'\n')

    texto.close()



def LeerAlarmas():

    readAlarmas=[]
    texto=open("/home/Termoplast/Desktop/proyectos/CG20MRFID/controlador/software/controladorCG20MRFID/archivos/Alarmas.txt", "r")

    for line in texto.readlines():
    
        tipo=line[0:1]
        numero=line[1:16]
        horario=line[16:29]
        if((horario=="\n") or (horario=="")):
            horario='0000000000000'
    
        readAlarmas.append(DatosAlarmas(tipo,numero,horario))
    
    texto.close()

    return readAlarmas
