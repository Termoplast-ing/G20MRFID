###definicion de la clase

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

class PesoHora:
    def __init__(self, dia:int, hora:int, peso:int):
        self.dia = dia
        self.hora = hora
        self.peso= peso

###importacion de librerias

import RPi.GPIO as GPIO
import time
import datetime
import os
from libreria import datosBD

animal=[]

#animal=datosBD.LeerDatoAnimal()

###inicio de la libreria

def HabilitacionAnima(animalLeido,animal):

    ###declaracion de variables

    nutricion=[]
    nutricionAUX=[]
    diaDietaActual=0
    food=[]
    nro=""
    diaInicio=""
    diaDieta=""
    peso=""
    hora=""
    comido=""
    horaDispensado=""
    horaReal=""
    i=0
    retorno=[9999,False]
    animalInhabilitado=[]
    diaReal=0
    pesoHora=[]
    guardarFood=[]
    guardarFood.append(DatosAnimal("000000000000000","0000000000000","000","0000","00","0","0000000000000"))
    diaFood=0
    alarmaSincro=False
    alarmaAUX=[]
    alarmaAUX.append(DatosAlarmas("0","000000000000000","0000000000000"))
    dieta=[]
    dispensado=[]
    diaSigDieta=0
    auxIndex=0
    

###for para crear un nuevo array con todos los elementos que
###contengan el numero de caravana leido  
  
    for i in range(len(animal)):
    
        if ((animal[i].number==animalLeido)and((animal[i].dispensed=="0000000000000")or(animal[i].eat=="1"))):
            nro=animal[i].number
            diaInicio=animal[i].dayStart
            diaDieta=animal[i].dayDiet
            peso=animal[i].load
            hora=animal[i].horary
            comido=animal[i].eat
            horaDispensado=animal[i].dispensed

            nutricion.append(DatosAnimal(nro,diaInicio,diaDieta,peso,hora,comido,horaDispensado))

###segun el dia de inicio de dieta se calcula que dia que va de ciclo
    
    diaDietaActual=int((int(time.time()*1000)-(int(nutricion[0].dayStart)))/86400000)

    auxDay=int(nutricion[0].dayDiet)
    
    for i in range(len(nutricion)):
        if(((int(nutricion[i].dayDiet))<=diaDietaActual)and(nutricion[i].dispensed=="0000000000000")):
            if(auxDay==int(nutricion[i].dayDiet)):
                dieta.append(PesoHora(int(nutricion[i].dayDiet),int(nutricion[i].horary),int(nutricion[i].load)))
            else:
                if(int(nutricion[i].dayDiet)>int(dieta[0].dia)):
                    dieta.clear()
                    auxDay=int(nutricion[i].dayDiet)
                    dieta.append(PesoHora(int(nutricion[i].dayDiet),int(nutricion[i].horary),int(nutricion[i].load)))
    
    for i in range(len(nutricion)):
        if((int(nutricion[i].dayDiet)==diaDietaActual)and(nutricion[i].eat=="1")):
            dispensado.append(PesoHora(int(nutricion[i].dayDiet),int(nutricion[i].horary),int(nutricion[i].load)))
            auxIndex=i

    horaReal=int(time.time()*1000)
    diaReal=int(((horaReal)-(int(nutricion[0].dayStart)))/86400000)
    horaReal=datetime.datetime.now()
    horaReal=int(horaReal.strftime('%H'))

    diaFood=int(nutricion[0].dayDiet)

    if(diaFood<=diaReal):
        if(len(dispensado)==0):
            guardarFood[0].number=nutricion[0].number
            guardarFood[0].dayStart=nutricion[0].dayStart
            guardarFood[0].dayDiet=str(diaDietaActual).zfill(3)
            guardarFood[0].load=str(dieta[0].peso).zfill(4)
            guardarFood[0].horary=str(dieta[0].hora).zfill(2)
            guardarFood[0].eat="1"
            guardarFood[0].dispensed=str(int(time.time()*1000))
            for j in range(len(animal)):
                indices=(len(animal)-(j+1))
                if ((animal[indices].number== guardarFood[0].number) and (animal[indices].dayStart == guardarFood[0].dayStart) and (animal[indices].dayDiet == (str(dieta[0].dia)).zfill(3))and (animal[indices].eat == "0")):
                    animal.insert((indices+1),guardarFood[0])
                    break
            animal=datosBD.GuardarDatoReal(animal)
            retorno[1]=int(dieta[0].peso)
            retorno[0]=True
            deshabilitado=False
            #aca hacer cuando el la primer toma del dia
        else:
            if((len(dieta))>(len(dispensado))):
                if((dieta[len(dispensado)].hora)<=(horaReal)):
                    guardarFood[0].number=nutricion[0].number
                    guardarFood[0].dayStart=nutricion[0].dayStart
                    guardarFood[0].dayDiet=str(diaDietaActual).zfill(3)
                    guardarFood[0].load=str(dieta[len(dispensado)].peso).zfill(4)
                    guardarFood[0].horary=str(dieta[len(dispensado)].hora).zfill(2)
                    guardarFood[0].eat="1"
                    guardarFood[0].dispensed=str(int(time.time()*1000))
                    for j in range(len(animal)):
                        indices=(len(animal)-(j+1))
                        if ((animal[indices].number== guardarFood[0].number) and (animal[indices].dayStart == guardarFood[0].dayStart) and (animal[indices].dayDiet == guardarFood[0].dayDiet)and (animal[indices].eat == guardarFood[0].eat)):
                            animal.insert((indices+1),guardarFood[0])
                            break
                    animal=datosBD.GuardarDatoReal(animal)
                    retorno[1]=int(guardarFood[0].load)
                    retorno[0]=True
                    deshabilitado=False
                else:
                    deshabilitado=True
            else:
                deshabilitado=True
            if(deshabilitado):
                guardarFood[0].number=nutricion[0].number
                guardarFood[0].dayStart=nutricion[0].dayStart
                guardarFood[0].dayDiet=str(diaDietaActual).zfill(3)
                guardarFood[0].load="0000"
                guardarFood[0].horary="00"
                guardarFood[0].eat="0"
                guardarFood[0].dispensed=str(int(time.time()*1000))
                animal.append(DatosAnimal(guardarFood[0].number,guardarFood[0].dayStart,guardarFood[0].dayDiet,guardarFood[0].load,guardarFood[0].horary,guardarFood[0].eat,guardarFood[0].dispensed))
                animal=datosBD.GuardarDatoReal(animal)
                retorno[1]=0
                retorno[0]=False
            #aca desarrollar el desahabilitadoi
    else:
        alarmaAUX[0].type="1"
        alarmaAUX[0].number=(str(animalLeido)).zfill(15)
        alarmaAUX[0].hour=str(int(time.time()*1000))
        datosBD.GuardarAlarmas(alarmaAUX[0])

    return retorno,animal

