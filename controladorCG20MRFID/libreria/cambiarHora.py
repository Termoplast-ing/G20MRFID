###importacion de librerias

import RPi.GPIO as GPIO
import time
import datetime
import os
from libreria import teclado
from libreria import LCD_LIB_16x2 as LCD
from libreria import cambiarHora

###declaracion de la libreria del manejo del menu

def CambiarHora():

###toma la hora y le asigna los valores a las variables que van a calibrar
###y  el resto de variables que va a usar la libreria

    LCD.lcd_string("calibrar fecha",LCD.LINE_1)
    fecha=datetime.datetime.now()    
    day=int(fecha.strftime("%d"))
    month=int(fecha.strftime("%m"))
    year=int(fecha.strftime("%Y"))-2000
    hour=int(fecha.strftime("%H"))
    minute=int(fecha.strftime("%M"))
    
    cursor=1
    ok=True
    key=""
    count=0
    flagDisp=0
    calHora=False
    confirmar=False
    guardar=True
    
###while para que quede en bucle hasta que termine de calibrar la hora
    
    while(ok):
###primer if para hacer el parpadeo de del termino a cambiar,el segundo para
###llamar la funcion de teclado
        if(flagDisp > 20):
            flagDisp=0
        else:
            flagDisp=flagDisp+1
        if(key==""):     
            key=teclado.Teclado(key,count)
            #print(key)
###con up y down sube y baja el valor pero lleva muchos if anidados para poder
###hacer bien el hecho de que los dia depende el mes pueden tener 28,29,30 o 31 
###diasy segun el valor de cursor los que cambia es el valor de dia,mes o año 
        if((not calHora)and(not confirmar)):
            if(key=="Up"):
                if(cursor==1):
                    day=day+1
                    key=""
                    if(month==4 or month==6 or month==9 or month==11):
                        if(day>30):
                            day=1
                    else:
                        if(month==2):
                            if(year%4==0):
                                if(day>29):
                                    day=1
                            else:
                                if(day>28):
                                    day=1
                        else:
                            if(day>31):
                                day=1
                elif(cursor==2):
                    month=month+1
                    key=""
                    if(month>12):
                        month=1
                elif(cursor==3):
                    year=year+1
                    key=""
                    if(year>99):
                        year=00
                else:
                    curso=1
            if(key=="Down"):
                if(cursor==1):
                    day=day-1
                    key=""
                    if(month==4 or month==6 or month==9 or month==11):
                        if(day<1):
                            day=30
                    else:
                        if(month==2):
                            if(year%4==0):
                                if(day<1):
                                    day=29
                            else:
                                if(day<1):
                                    day=28
                        else:
                            if(day<1):
                                day=31
                elif(cursor==2):
                    month=month-1
                    key=""
                    if(month<1):
                        month=12
                elif(cursor==3):
                    year=year-1
                    key=""
                    if(year<1):
                        year=99
                else:
                    curso=1
###con right y left cambio el valor de cursor por lo tanto selecciono que 
###termino voy a cambiar con up y down y con enter guardo los nuevos valores
            if(key=="Right"):
                cursor=cursor+1
                key=""
                if(cursor>3):
                    cursor=1
            if(key=="Left"):
                cursor=cursor-1
                key=""
                if(cursor<1):
                    cursor=3
            if(key=="Enter"):
                cursor=1
                key=""
                calHora=True

            if(flagDisp<10):
                LCD.lcd_string(str(day).zfill(2) + "/" + str(month).zfill(2) + "/" + str(year+2000).zfill(4),LCD.LINE_2)
            else:
                if(cursor==1):
                    LCD.lcd_string("  " + "/" + str(month).zfill(2) + "/" + str(year+2000).zfill(4),LCD.LINE_2)
                elif(cursor==2):
                    LCD.lcd_string(str(day).zfill(2) + "/" + "  " + "/" + str(year+2000).zfill(4),LCD.LINE_2)
                elif(cursor==3):
                    LCD.lcd_string(str(day).zfill(2) + "/" + str(month).zfill(2) + "/" + "    ",LCD.LINE_2)
                else:
                    cursor==1
###en el elif que va a entrar solo cuando aprete enter en la parte de fecha
###analogo que para la fecha es el funcioanmiento para los dias
        elif((calHora) and (not confirmar)):
            if(key=="Up"):
                if(cursor==1):
                    hour=hour+1
                    key=""
                    if(hour>23):
                        hour=0
                elif(cursor==2):
                    minute=minute+1
                    key=""
                    if(minute>59):
                        minute=0
                else:
                    cursor=1
            elif(key=="Down"):
                if(cursor==1):
                    hour=hour-1
                    key=""
                    if(hour<00):
                        hour=23
                elif(cursor==2):
                    minute=minute-1
                    key=""
                    if(minute<0):
                        minute=59
                else:
                    cursor=1
            elif(key=="Right"):
                cursor=cursor+1
                key=""
                if(cursor>2):
                    cursor=1
            elif(key=="Left"):
                cursor=cursor-1
                key=""
                if(cursor<1):
                    cursor=2
            elif(key=="Enter"):
                cursor=1
                key=""
                calHora=False
                confirmar=True
###aca se muestra igual que en la fecha los valores que van cambiando
            else:                
                LCD.lcd_string("calibrar hora",LCD.LINE_1)
            if(flagDisp<10):
                LCD.lcd_string(str(hour).zfill(2) + ":" + str(minute).zfill(2),LCD.LINE_2)
            else:
                if(cursor==1):
                    LCD.lcd_string("  " + ":" + str(minute).zfill(2),LCD.LINE_2)
                elif(cursor==2):
                    LCD.lcd_string(str(hour).zfill(2) + ":" + "  ",LCD.LINE_2)
                else:
                    cursor==1
###en este else nos muestra fecha y hora y le tenemos que dar enter para 
###confirmar el cambio de fecha y hora  
        else:
            if(key=="Up"):
                key=""
            elif(key=="Down"):
                key=""
            elif(key=="Right"):
                if(guardar):
                    guardar=False
                else:
                    guardar=True
                key=""
            elif(key=="Left"):
                if(guardar):
                    guardar=False
                else:
                    guardar=True
                key=""
            elif(key=="Enter"):
                key=""
                calHora=False
                confirmar=True
                ok=False
                if(guardar):
                    LCD.lcd_string("***guardando***",LCD.LINE_2)
                    fechaAUX=str(hour).zfill(2)+":"+str(minute).zfill(2)+":   00"
                    os.system("sudo date +%T -s '" + fechaAUX + "'")
                    os.system("sudo hwclock --systohc")
                    anioAUX=str(year+2000).zfill(4)+str(month).zfill(2)+str(day).zfill(2)
                    os.system("sudo date +%Y%m%d -s '" + anioAUX +"'")
                    os.system("sudo hwclock --systohc")
                else:
                    LCD.lcd_string("***no guardado***",LCD.LINE_2)
                    time.sleep(2)
            else:
                LCD.lcd_string(str(day).zfill(2) + "/" + str(month).zfill(2) + "/" + str(year+2000).zfill(4) + "-" + str(hour).zfill(2) + ":" + str(minute).zfill(2),LCD.LINE_1)
            if(flagDisp<10):
                LCD.lcd_string("guardar    salir",LCD.LINE_2)
            else:
                if(guardar):
                    LCD.lcd_string("           salir",LCD.LINE_2)
                else:
                    LCD.lcd_string("guardar         ",LCD.LINE_2)
                
        

    return
