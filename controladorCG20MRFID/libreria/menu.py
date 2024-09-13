###importacion de librerias

import RPi.GPIO as GPIO
import time
import datetime
from libreria import teclado
from libreria import LCD_LIB_16x2 as LCD
from libreria import cambiarHora
from libreria import dienteAzul
from libreria import ingresarMAC
from libreria import transferDatos
from libreria import agregarAnimal
from libreria import apagarCtrl
from libreria import alarmas

###declaracion de la libreria del manejo del menu

def Menu(menu,tecla,habil,timeDosis):
##########   para manejar la paginacion del menu se usa, a falta   ##########
##########     del buen switch, se usa varios if-else anidados     ##########
##########          1 - calibrar fecha y hora                      ##########
##########          2 - transferir datos del dispositivos          ##########
##########          3 - agregar animales nuevos                    ##########
##########          4 - alarmas                                    ##########
##########          5 - calibrar dosis                             ##########
##########          6 - apagar controlador                         ##########
##########          7 - salir del menu                             ##########
    nuevoAnimal=False
    emparejar=False
    
    
### muestra el mensaje de la primer pagina del menu(->)-proxima pag.(<-)-vuelve
### a la pag anterior(enter)-entra al menu posicionado
    
    if(menu==1):
        LCD.lcd_string("    Calibrar    ",LCD.LINE_1)
        LCD.lcd_string("  Fecha y Hora  ",LCD.LINE_2)
        if(tecla == "Right"):
            menu=2
            habil=False
        elif(tecla == "Left"):
            menu=7
            habil=False
        elif(tecla == "Enter"):
###cuando vuelve de la funcion de calibrar el reloj actualiza la hora en el 
###programa y display
            cambiarHora.CambiarHora()
            LCD.lcd_string("Cal.fecha/hora",LCD.LINE_1)
            fecha=datetime.datetime.now()    
            fechAux=fecha.strftime('%d/%m/%Y-%H:%M')
            LCD.lcd_string(fechAux,LCD.LINE_2)
            habil=False
        tecla=""

### muestra el mensaje de la primer pagina del menu(->)-proxima pag.(<-)-vuelve
### a la pag anterior(enter)-entra al menu posicionado
    
    elif (menu==2):
        LCD.lcd_string("Transferir Datos",LCD.LINE_1)
        LCD.lcd_string("Del Dispositivo",LCD.LINE_2)
        if(tecla == "Right"):
            menu=3
            habil=False
        elif(tecla == "Left"):
            menu=1
            habil=False
        elif(tecla == "Enter"):
            #################RESOLVER##########################
            dienteAzul.dienteazul()
            #print("ok")
            #dirMAC=transferDatos.IngresarMAC()
            #emparejar=transferDatos.YaEmparejado(dirMAC)
            #if(emparejar):
            #    transferDatos.TransferirDatos(dirMAC)
            habil=False
        tecla=""

### muestra el mensaje de la primer pagina del menu(->)-proxima pag.(<-)-vuelve
### a la pag anterior(enter)-entra al menu posicionado

    elif (menu==3):
        LCD.lcd_string(" Agregar Animal ",LCD.LINE_1)
        LCD.lcd_string("     Nuevo      ",LCD.LINE_2)
        if(tecla == "Right"):
            menu=4
            habil=False
        elif(tecla == "Left"):
            menu=2
            habil=False
        elif(tecla == "Enter"):
            nuevoAnimal=agregarAnimal.AgregarAnimal()
            habil=False
        tecla=""

### muestra el mensaje de la primer pagina del menu(->)-proxima pag.(<-)-vuelve
### a la pag anterior(enter)-entra al menu posicionado

    elif (menu==4):
        LCD.lcd_string("*** ALARMAS ***",LCD.LINE_1)
        LCD.lcd_string("  ",LCD.LINE_2)
        if(tecla == "Right"):
            menu=5
            habil=False
        elif(tecla == "Left"):
            menu=3
            habil=False
        elif(tecla == "Enter"):
            alarmas.Alarmas()
            habil=False
        tecla=""

### muestra el mensaje de la primer pagina del menu(->)-proxima pag.(<-)-vuelve
### a la pag anterior(enter)-entra al menu posicionado

    elif (menu==5):
        LCD.lcd_string("Calibrar Dosis",LCD.LINE_1)
        msjDosis=str(timeDosis)
        msjDosis=msjDosis + " segundos 100g"
        LCD.lcd_string(msjDosis,LCD.LINE_2)
        if(tecla == "Right"):
            menu=6
            habil=False
        elif(tecla == "Left"):
            menu=5
            habil=False
        elif(tecla == "Up"):
            timeDosis=timeDosis+1
            if timeDosis>15:
                timeDosis=15
            habil=False
        elif(tecla == "Down"):
            timeDosis=timeDosis-1
            if timeDosis<1:
                timeDosis=1
            habil=False
        elif(tecla == "Enter"):
            GPIO.output(32,False)
            time.sleep(timeDosis)
            GPIO.output(32,True)
            habil=False
        tecla=""

### muestra el mensaje de la primer pagina del menu(->)-proxima pag.(<-)-vuelve
### a la pag anterior(enter)-entra al menu posicionado

    elif (menu==6):
        LCD.lcd_string("     Apagar     ",LCD.LINE_1)
        LCD.lcd_string("   Controlador  ",LCD.LINE_2)
        if(tecla == "Right"):
            menu=7
            habil=False
        elif(tecla == "Left"):
            menu=5
            habil=False
        elif(tecla == "Enter"):
            apagarCtrl.ApagarCtrl()
            habil=False
        tecla=""

### muestra el mensaje de la primer pagina del menu(->)-proxima pag.(<-)-vuelve
### a la pag anterior(enter)-entra al menu posicionado
        
    elif (menu==7):
        LCD.lcd_string("   Salir del    ",LCD.LINE_1)
        LCD.lcd_string("      Menu      ",LCD.LINE_2)
        if(tecla == "Right"):
            menu=1
            habil=False
        elif(tecla == "Left"):
            menu=6
            habil=False
        elif(tecla == "Enter"):
            menu=0
            habil=False
        tecla=""
    else:
       menu=0
       
    listAux=[tecla,menu,habil,timeDosis,nuevoAnimal]
    
    return listAux
    
