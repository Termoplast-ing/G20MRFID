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


def Alarmas():

    alarmas=[]
    bucleMostrar=True
    i=0
    key=""
    count=0
    auxLINE2=0
    hora=""
    horaAUX=""
    borrar=False
    
    alarmas=datosBD.LeerAlarmas()

    if(len(alarmas)==0):
        while(bucleMostrar):
            LCD.lcd_string(" No hay alarmas ",LCD.LINE_1)
            LCD.lcd_string("     Volver     ",LCD.LINE_2)
            
    else:
        while(len(alarmas)>i):
            if(auxLINE2>100):
                auxLINE2=1
            else:
                auxLINE2=auxLINE2+1
            LCD.lcd_string(alarmas[i].number,LCD.LINE_1)
            if(auxLINE2>50):
                if(alarmas[i].type=="1"):
                    LCD.lcd_string(" sincronizacion ",LCD.LINE_2)
                if(alarmas[i].type=="2"):
                    LCD.lcd_string("Nro. desconocido",LCD.LINE_2)
                if(alarmas[i].type=="3"):
                    LCD.lcd_string("Dieta incompleta",LCD.LINE_2)
                if(alarmas[i].type=="4"):
                    LCD.lcd_string("MAX. CAP. animal",LCD.LINE_2)
            else:
                hora=int(alarmas[i].hour)
                hora=(datetime.datetime.fromtimestamp(hora/1000))
                horaAUX=hora.strftime('%d/%m/%2Y %H:%M')
                LCD.lcd_string(horaAUX,LCD.LINE_2)
            
            if(key==""):   
                key=teclado.Teclado(key,count)
            if(key=="Up"):
                if(len(alarmas)==0):
                    key=""
                else:
                    if(i==0):
                        i=(len(alarmas))-1
                    else:
                        i=i-1
                key=""
            else:
                if(key=="Down"):
                    if(len(alarmas)==0):
                        key=""
                    else:
                        if(i==(len(alarmas)-1)):
                            i=0
                        else:
                            i=i+1
                    key=""
                else:
                    if(key=="Left"):
                        if(len(alarmas)==0):
                            key=""
                        else:
                            i=(len(alarmas)+1)
                            borrar=False
                        key=""
                    else:
                        if(key=="Enter"):
                            if(len(alarmas)==0):
                                bucleMostrar=False
                            else:
                                i=(len(alarmas)+1)
                                borrar=True
                                alarmas.clear()
                            key=""
                        else:
                            if(key=="Right"):
                                if(len(alarmas)==0):
                                    key=""
                                else:
                                    borrar=True
                                    del alarmas[i]
                                key=""
                            else:
                                key=""
            if(borrar):
                alarmas=datosBD.GuardarAlarmas(alarmas)
                    
    return