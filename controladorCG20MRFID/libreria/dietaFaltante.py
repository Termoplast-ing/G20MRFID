###importacion de librerias

import RPi.GPIO as GPIO
import time
import datetime
import serial
import threading
import time
import datetime
from libreria import teclado
from libreria import datosBD
from libreria import menu
from libreria import LCD_LIB_16x2 as LCD
from libreria import habilitacionAnimal
from libreria import datosBD
from libreria import dietaFaltante

###declaracion de la clase 

class DatosAnimal:
    def __init__(self, number: str,dayStart: str,dayDiet: str,load: str,horary: str,eat: str,dispensed: str):
        self.number = number
        self.dayStart = dayStart
        self.dayDiet = dayDiet
        self.load = load
        self.horary = horary
        self.eat= eat
        self.dispensed = dispensed

class DatosAlarmas:
    def __init__(self, type: str, number:str, hour:str):
        self.type = type
        self.number = number
        self.hour = hour

def DietaFaltante(day):

    animal=[]
    animalAUX=[]
    dietas=[]
    dietasAUX=[]
    auxiliar=0
    comido=[]
    comidas=[]
    alarma=[]
    alarma.append(DatosAlarmas("0","000000000000000","0000000000000"))

    animal=datosBD.LeerDatoAnimal()

###    for i in range(len(animal)):
###        if((animal[i].dispensed=="0000000000000")and(int(animal[i].dayDiet)<=day)):
###            nroCaravanaAUX.append(DatosAnimal(animal[i].number,animal[i].dayStart,animal[i].dayDiet,animal[i].load,animal[i].horary,animal[i].eat,animal[i].dispensed))

###    auxiliar=nroCaravanaAUX[0].number
###    ###auxiliar.append(DatosAnimal(nroCaravanaAUX[0].number,nroCaravanaAUX[0].dayStart,nroCaravanaAUX[0].dayDiet,nroCaravanaAUX[0].load,nroCaravanaAUX[0].horary,nroCaravanaAUX[0].eat,nroCaravanaAUX[0].dispensed))
    
###    for i in range(len(nroCaravanaAUX)-1): 
###        if(auxiliar!=nroCaravanaAUX[i+1].number):
###            nroCaravana.append(DatosAnimal(nroCaravanaAUX[i].number,nroCaravanaAUX[i].dayStart,nroCaravanaAUX[i].dayDiet,nroCaravanaAUX[i].load,nroCaravanaAUX[i].horary,nroCaravanaAUX[i].eat,nroCaravanaAUX[i].dispensed))
###            auxiliar=nroCaravanaAUX[i+1].number

###    for i in range(len(nroCaravana)):
###        print(nroCaravana[i])

###    auxiliar=animal[0].number

###    for i in range(len(animal)-1):
###        if((animal[i].dispensed=="0000000000000") and (animal[i+1].number==auxiliar)and(int(animal[i].dayDiet)<=day)):
###            nroCaravanaAUX.append(animal[i])
###       else:
###            auxiliar=animal[i+1].number
        
###    for j in range(len(nroCaravanaAUX)):
###        if(nroCaravanaAUX[j].dayDiet == dietaAUX):
###            nroCaravana.append(nroCaravanaAUX[j]) 
    animalAUX.append(animal[0].number)      

    for i in range(len(animal)-1):
        if((animal[i+1].dispensed=="0000000000000") and (animal[i+1].number!=animalAUX[-1])):
            animalAUX.append(animal[i+1].number)

    for i in range(len(animalAUX)):
        dietas.clear()

        for j in range(len(animal)):
            if((animal[j].dispensed=="0000000000000") and(animal[j].number==animalAUX[i]) and (int(animal[j].dayDiet)<=day)):
                dietas.append(animal[j])

        auxiliar=int(dietas[-1].dayDiet)

        for j in range(len(dietas)):
            if((int(dietas[j].dayDiet))==auxiliar):
                dietasAUX.append(dietas[j])

    for i in range(len(animalAUX)):
        for j in range(len(animal)):
            comido.clear()
            comidas.clear()
            compararDaym=(int(animal[j].dayStart))+(86400000*day)
            compararDayM=compararDaym+86400000
            if((str(animal[j].number)==str(animalAUX[j])) and (animal[i].eat=="1") and (compararDaym<(int(animal[i].dispensed))) and (compararDayM>(int(animal[i].dispensed)))):
                comido.append(animal[j])
        
        for j in range(len(dietasAUX)):
            if(animalAUX[i].number==dietasAUX[j].number):
                comidas.append(dietasAUX[j])

        if(len(comidas)>len(comido)):
            alarma[0].type="3"
            alarma[0].number=(str(animalAUX[i])).zfill(15)
            alarma[0].hour=str(int(time.time()*1000))
            datosBD.GuardarLineaAlarmas(alarma[0])


    return