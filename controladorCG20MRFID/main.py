###importacion de librerias

import RPi.GPIO as GPIO
import time
import datetime
import serial
import threading
from libreria import teclado
from libreria import datosBD
from libreria import menu
from libreria import LCD_LIB_16x2 as LCD
from libreria import habilitacionAnimal
from libreria import datosBD
from libreria import alarmas
from libreria import dietaFaltante
from libreria import pruebaHabi

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

###se declara la variable antena la inicializacion de las GPIO y del display
###la las declaracion de variables
        
antena = serial.Serial('/dev/ttyUSB0', 9600)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
GPIO.setup(29, GPIO.IN)
GPIO.setup(31, GPIO.IN)
GPIO.setup(33, GPIO.IN)
GPIO.setup(37, GPIO.IN)
GPIO.setup(32, GPIO.OUT)
GPIO.output(32,True)

LCD.lcd_init()

caravana=""
cadena=""
countKey=0
fin=1
keyPress=""
main=0
showCaravana=0
addAnimal=False
dosis=1
reader=""
animales={}
foodOK=[False,0]
retardoON=False
listAuxMain=[]
habilitado=True
datoAnimal=[]
datoAnimalAUX=[]
guardarLecturaAUX=[]
guardarLecturaAUX.append(DatosAnimal("000000000000000","0000000000000","000","0000","00","0","0000000000000"))
i=0
alarmaDesconocido=False
mensajeDesconocido=False
desconocido=False
guardarLectura=False
### 1-falla sincronizacion / 2-falla animal desconocido
### 3-falla animal no comio dieta / 4-falla sobrecarga animales
### segundo elemento del arreglo hora de la falla
flagAlarma=[]
flagAlarma.append(DatosAlarmas("0","000000000000000","0000000000000"))
flagAlarmasAUX=False
dia=60
alarma=[]
displayAUX=0

###se toma la fecha y hora se le pasa al display para que muestre

fecha=datetime.datetime.now()
fechAux=fecha.strftime('%d/%m/%Y-%H:%M')


LCD.lcd_string(fechAux,LCD.LINE_1)
LCD.lcd_string("esperando animal",LCD.LINE_2)

###funcion que se ejecuta luego del transcurrido el tiempo seteado en cada 
###caso segun corresponda luego de leer un animal

def Retardo():
    GPIO.output(32,True)
    global foodOK
    foodOK[0]=False
    foodOK[1]=0
    global retardoON
    retardoON=False
    global desconocido
    desconocido=False
    global showCaravana
    showCaravana=0

### va a leer al archivos todos los registros y los guarda en datoAnimal

datoAnimal=datosBD.LeerDatoAnimal()

### genero un vector para guardar solo una vez cada caravana para ver la
### cantidad animales que hay agregados si hay mas de 20 da la alarma de sobrecarga

datoAnimalAUX.append(datoAnimal[0].number)

for i in range(len(datoAnimal)-1):
    if((datoAnimal[i+1].dispensed=="0000000000000") and (datoAnimal[i+1].number!=datoAnimalAUX[-1])):
        datoAnimalAUX.append(datoAnimal[i+1].number)

if(len(datoAnimalAUX)>19):
    flagAlarma[0].type="4"
    flagAlarma[0].number=(str(0)).zfill(15)
    flagAlarma[0].hour=str(int(time.time()*1000))
    datosBD.GuardarLineaAlarmas(flagAlarma[0])

###bucle infinito para que siempre se ejecute el programa y inicio del mismo

while(True):
    #if(displayAUX==10):
    #    LCD.reinicio()
    #    displayAUX=0
    #else:
    #    displayAUX=displayAUX+1   

    alarma=datosBD.LeerAlarmas()
    if(len(alarma)==0):
        flagAlarmasAUX=True
        ###gpio que prende luz alarma
    else:
        flagAlarmasAUX=False
        ###gpio que prende luz alarma

###todo lo que contiene el proximo if es lo que se ejecuta en el main

    if(main==0):

### compara con la variable showcaravana para ver si muestra el mensaje principal(=0)
### o los mensajes de lectura(=1) osea  el mensaje que muestra luego de cada lectura
###segun corresponda en cada caso

        if(showCaravana==1):
###en este caso muestra el numero de caravana y el mensaje despachando
            if(foodOK[0]):
                if(displayAUX==10):
                    LCD.reinicio()
                    displayAUX=0
                else:
                    displayAUX=displayAUX+1 
                LCD.lcd_string(caravana,LCD.LINE_1)
                LCD.lcd_string("  Despachando  ",LCD.LINE_2)
            else:
###sino muestra tambien el numero de caravana y el mensaje animal inahbilitado
### o ID desconocido segun corresponda
                if(displayAUX==10):
                    LCD.reinicio()
                    displayAUX=0
                else:
                    displayAUX=displayAUX+1 
                LCD.lcd_string(str(caravana).zfill(15),LCD.LINE_1)
                LCD.lcd_string(mensaje,LCD.LINE_2)
        else:
            fecha=datetime.datetime.now()    
            fechAux=fecha.strftime('%d/%m/%Y-%H:%M')
            if(displayAUX==10):
                LCD.reinicio()
                displayAUX=0
            else:
                displayAUX=displayAUX+1 
            LCD.lcd_string(fechAux,LCD.LINE_1)
            LCD.lcd_string("esperando animal",LCD.LINE_2)
        
###tratamiento de la lectura de la antena y lo guarda en la variable reader y caravana
    
        transmition=antena.inWaiting()
        if transmition:
            caravanaAux = antena.read()
            caravanaAux1=caravanaAux.decode()
            if(caravanaAux1 == '$'):
                reader=""
                cadena=""
            else:
                cadena=cadena + caravanaAux.decode()
            if(caravanaAux1 == '#'):
                reader=cadena[8:23:]
                caravana=reader
                
        #if(not retardoON):
            #print("numero")        
            #reader=input()
        #reader="112233020445566"
        
###compara si reader leyo el numero entra al if sino no hace nada
        print(reader)
        if((reader!="") and (not retardoON)):       

###for que recorre todo el registro de animales y compara con el leido si lo
###encuentra llama a la libreria habilitacionAnimal() para su tratamiento sino
### lo marca como no leido para que se trate por otro lado y se da la alarma

            for i in range(len(datoAnimal)):
                if((datoAnimal[i].number == reader)and(datoAnimal[i].dayStart!="1111111111111")):
                    #foodOK,datoAnimal=habilitacionAnimal.HabilitacionAnimal(reader,datoAnimal)
                    foodOK,datoAnimal=pruebaHabi.HabilitacionAnima(reader,datoAnimal)
                    desconocido=False
                    guardarLectura=False
                    break    
                else:
                    desconocido=True
                    guardarLectura=True
        
###si el numero leido fue marcado como desconocido se guarda en el registro 
###en la ultima linea se guarda el ID,el diadiet con el dia de ciclo y la hora
###en diastart se guarda con todos 1,load 0, horary 99, eat 0 para identificarlo

        if(guardarLectura):
            guardarLecturaAUX[0].number=(str(reader).zfill(15))
            guardarLecturaAUX[0].dayStart="1111111111111"
            guardarLecturaAUX[0].dayDiet=(str(int((int(time.time()*1000)-(int(datoAnimal[0].dayStart)))/86400000)).zfill(3))
            guardarLecturaAUX[0].load="0000"
            guardarLecturaAUX[0].horary="99"
            guardarLecturaAUX[0].eat="0"
            guardarLecturaAUX[0].dispensed=str(int(time.time()*1000)).zfill(13)
            datoAnimal.append(DatosAnimal(guardarLecturaAUX[0].number,guardarLecturaAUX[0].dayStart,guardarLecturaAUX[0].dayDiet,guardarLecturaAUX[0].load,guardarLecturaAUX[0].horary,guardarLecturaAUX[0].eat,guardarLecturaAUX[0].dispensed))
            datoAnimal=datosBD.GuardarDatoReal(datoAnimal)
            flagAlarma[0].type="2"
            flagAlarma[0].number=(str(reader)).zfill(15)
            flagAlarma[0].hour=str(int(time.time()*1000))
            datosBD.GuardarLineaAlarmas(flagAlarma[0])
            guardarLectura=False

### tratamiento de la devolucion del tratamiento de la lectura,va a habilitar
### el despacho o no,acomodar los mensajes y dar el retardor para controlar 
### el tiempo de despacho


        if((not retardoON) and (reader!="")):    
            if (foodOK[0]):
                GPIO.output(32,False)
                retardoON=True
                showCaravana=1
                
                t=threading.Timer(((foodOK[1]/100)*(dosis)),Retardo) #dosis variable de calibracion que tiene que ser el tiempo de marcha del motor para que tiere un gramo de alimento
                t.start()
            else:
                showCaravana=1
                GPIO.output(32,True)
                retardoON=True
                caravana=reader
                t=threading.Timer(10,Retardo) #retardo para mostrar mensaje y deshabilitar antena
                t.start()
                if(desconocido):
                    mensaje=" ID desconocido "                  
                else:
                    mensaje="Animal Inhabili."

###reinicia variable reader

        reader=""

############################## fin menu ##############################   

###si no hay tecla presionada entra a libreria que maneja el teclado
        
    if(keyPress==""):     
        keyPress=teclado.Teclado(keyPress,countKey)
        #print(keyPress)
        if(keyPress==""):
            habilitado=True

###si es diferente de "Rigth" limpia la variable para que vuelva a leer la tecla
###ya que las demas teclas no tienen funcion en el main
    
    if(main==0 and keyPress!="Right"):
        keyPress=""
        
###si esta en el menu principal y se apreto la tecla "Right" se ingrasa al
###menu de opciones

    if(main==0 and keyPress=="Right"):
        keyPress=""
        main=1

### llamado y tratamiento del menu
       
    if(habilitado):
        listAuxMain=menu.Menu(main,keyPress,habilitado,dosis)
    keyPress=listAuxMain[0]
    main=listAuxMain[1]
    habilitado=listAuxMain[2]
    dosis=listAuxMain[3]

### si vuelve del menu con la flag de que se agrego un animal borra la lista
### y la vuelve a leer del archivo

    if(listAuxMain[4]):
        datoAnimal.clear()
        datoAnimal=datosBD.LeerDatoAnimal()

    if((int(time.time()*1000))<(int(datoAnimal[0].dayStart))):
        
        flagAlarma[0].type="1"
        flagAlarma[0].number=(str(0)).zfill(15)
        flagAlarma[0].hour=str(int(time.time()*1000))
        datosBD.GuardarLineaAlarmas(flagAlarma[0])

### tratamiento de la falla por no respetar la dieta
    if((dia)!=(int(fecha.strftime('%d')))):
        #dietaFaltante.DietaFaltante(dia)
        dia=int(fecha.strftime('%d'))
        


###fin del programa limpia el gpio antes de apagarse
        

GPIO.cleanup()
 
