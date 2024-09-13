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

###importacion de librerias

import RPi.GPIO as GPIO
import time
import datetime
import os
from libreria import datosBD

animal=[]

#animal=datosBD.LeerDatoAnimal()

###inicio de la libreria

def HabilitacionAnimal(animalLeido,animal):

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
    dispensado=""
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
    diaSigDieta=0
    

###for para crear un nuevo array con todos los elementos que
###contengan el numero de caravana leido  
  
    for i in range(len(animal)):
    
        if ((animal[i].number==animalLeido)and((animal[i].dispensed=="0000000000000")or(animal[i].eat))):
            nro=animal[i].number
            diaInicio=animal[i].dayStart
            diaDieta=animal[i].dayDiet
            peso=animal[i].load
            hora=animal[i].horary
            comido=animal[i].eat
            dispensado=animal[i].dispensed

            nutricion.append(DatosAnimal(nro,diaInicio,diaDieta,peso,hora,comido,dispensado))

###segun el dia de inicio de dieta se calcula que dia que va de ciclo
    
    diaDietaActual=int((int(time.time()*1000)-(int(nutricion[0].dayStart)))/86400000)

###for para crear un nuevo array donde solo quedan los elementos
###que el dia de dieta son menor que el dia dieta actual
    
    for i in range(len(nutricion)):
        if(diaDietaActual>=int(nutricion[i].dayDiet)):
            nutricionAUX.append(DatosAnimal(nutricion[i].number,nutricion[i].dayStart,nutricion[i].dayDiet,nutricion[i].load,nutricion[i].horary,nutricion[i].eat,nutricion[i].dispensed))
        else:
            diaSigDieta=int(nutricion[i].dayDiet)
            break

###ya que los dia de dieta estan ordenados en forma ascendente asigno
### el valor de diadieta del ultimo elemento del vector que este va a 
### contener la dieta mas proxima por lo tanto la que corresponde dar 
              
    diaDietaAnimal=nutricionAUX[-1].dayDiet
    i=0

###for para crear el arreglo que contiene la dieta a dispensar

    for i in range(len(nutricionAUX)):
        if(((int(nutricionAUX[i].dayDiet)==diaReal) and (nutricionAUX[i].eat=="1")) or ((nutricionAUX[i].dayDiet==diaDietaAnimal) and (nutricionAUX[i].dispensed=="0000000000000"))):
            food.append(DatosAnimal(nutricionAUX[i].number,nutricionAUX[i].dayStart,nutricionAUX[i].dayDiet,nutricionAUX[i].load,nutricionAUX[i].horary,nutricionAUX[i].eat,nutricionAUX[i].dispensed))
    
###se le asigna los valores de la hora real del dia y el dia que va de  
###ciclo para poder comparar
    horaReal=int(time.time()*1000)
    diaReal=int(((horaReal)-(int(food[0].dayStart)))/86400000)
    horaReal=datetime.datetime.now()
    horaReal=int(horaReal.strftime('%H'))

###for para hacer una matriz con todos los valores de peso y hora correspondiente

    for i in range(len(food)):
        if(food[i].dispensed=="0000000000000"):
            pesoHora.append([food[i].horary,food[i].load])

###compara el dia de dieta con el dia de ciclo para ver se le corresponde
### dispensar ese dia
    
    diaFood=int(food[-1].dayDiet)
    #print(len(food))
    if (diaFood<=diaReal):

###si corresponde por el dia despachar comida va a comparar el ultimo elemento 
###del arreglo si este en dispensed tiene todos cero significa es todavia no 
###hay historia y toma el los valores de peso y hora del primer elemento para 
###comparar OR si horario del ultimo elemento es mayor que la hora real ya que 
###esto significa que tiene que cargar el horario del dia nuevo
        
        if((food[-1].dispensed=="0000000000000") or (int(food[-1].horary)>horaReal)):
            horaFood=pesoHora[0][0]
            loadAUX=pesoHora[0][1]

###si no se cumple lo anterios  hacemos un for para recorrer la matriz de 
###peso y hora y lo comparamos con el ultimo elemento que va a ser el ultimo
###registro de despacho para ese animal, tambien se atiende las posibilidades
###de que hay una falla en los datos pero igual se asignan valores asi no se 
###cuelga el comedero

        else:
            for i in range(len(pesoHora)):
                if((food[-1].horary)==pesoHora[i][0]):
                    if(len(pesoHora)>(i+1)):
                        horaFood=pesoHora[i+1][0]
                        loadAUX=pesoHora[i+1][1]
                        break
                    else:
                        horaFood=24
                        loadAUX=0
                        break
                else:
                    horaFood=0
                    if((i>=len(pesoHora)-1)):
                        horaFood=24
                        loadAUX=0
                        break

###se compara no solo que la hora real sea mayor que la de la dieta sino que 
###tambienque el horario de dieta del ultimo elementos sea menor que el del 
### actual para que entre horarios solo dispense una sola vez

        if((int(horaReal) >= int(horaFood)) and (int(food[-1].horary)<int(horaFood)) or (food[-1].dispensed=="0000000000000")):
            
###si entra aca inserta el registro del animal despachado al final de los datos
###de ese animal o luego del ultimo registro que haya de ese animal y antes de 
###que empiezen los datos del siguiente numero de caravana
            
            guardarFood[0].number=food[-1].number
            guardarFood[0].dayStart=food[-1].dayStart
            guardarFood[0].dayDiet=str(diaDietaActual).zfill(3)
            guardarFood[0].load=str(loadAUX)
            guardarFood[0].horary=str(horaFood)
            guardarFood[0].eat="1"
            guardarFood[0].dispensed=str(int(time.time()*1000))
            for j in range(len(animal)):
                indices=(len(animal)-(j+1))
                if ((animal[indices].number== guardarFood[0].number) and (animal[indices].dayStart == guardarFood[0].dayStart)):
                    animal.insert((indices+1),guardarFood[0])
                    break  
            animal=datosBD.GuardarDatoReal(animal)
            retorno[1]=int(guardarFood[0].load)
            retorno[0]=True

###si no entral en el anterios esporque al animal leido no le corresponde comida
###por horario o lo que sea, en tal caso, va a este else y guarda el registro que 
###se leyo el animal pero no le despacha comida y lo guarda en la ultima linea del archivo

        else:
            guardarFood[0].number=food[-1].number
            guardarFood[0].dayStart=food[-1].dayStart
            guardarFood[0].dayDiet=food[-1].dayDiet
            guardarFood[0].load="0000"
            if(horaFood==24):
                guardarFood[0].horary=str(pesoHora[-1][0])
            else:
                guardarFood[0].horary=str(horaFood)
            guardarFood[0].eat="0"
            guardarFood[0].dispensed=str(int(time.time()*1000))
            animal.append(DatosAnimal(guardarFood[0].number,guardarFood[0].dayStart,guardarFood[0].dayDiet,guardarFood[0].load,guardarFood[0].horary,guardarFood[0].eat,guardarFood[0].dispensed))
            animal=datosBD.GuardarDatoReal(animal)
            retorno[1]=0
            retorno[0]=False

###a este else solo va entrar si el dia de ciclo es menor que el dia de dieta
###por lo cual significa que hay un error de sincronizacion de reloj ya que 
###esto no tendria que suceder en ningun caso
    else:
        alarmaAUX[0].type="1"
        alarmaAUX[0].number=(str(animalLeido)).zfill(15)
        alarmaAUX[0].hour=str(int(time.time()*1000))
        datosBD.GuardarAlarmas(alarmaAUX[0])
              

    return retorno,animal
