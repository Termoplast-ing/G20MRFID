import RPi.GPIO as GPIO
import time
import datetime
import os
import subprocess
from libreria import teclado
from libreria import LCD_LIB_16x2 as LCD
from libreria import apagarCtrl

def ApagarCtrl():
    
    flagDisp=0
    key=""
    count=0
    apagar=True
    apagarAUX=True
    auxiliar=True
    
    while(apagarAUX):
    
        if(flagDisp > 20):
            flagDisp=0
        else:
            flagDisp=flagDisp+1
        if(key==""):     
            key=teclado.Teclado(key,count)
            #print(key)
        
        if(key=="Up" or key=="Down"):
            if(apagar):
                apagar=False
            else:
                apagar=True
            key=""
        elif(key=="Enter"):
            apagarAUX=False
            auxiliar=True
            key=""
        else:
            key=""
        
        if(flagDisp<10):
            LCD.lcd_string(" Quiere Apagar? ",LCD.LINE_1)
            LCD.lcd_string("Apagar     Salir",LCD.LINE_2)
        else:
            if(apagar):
                LCD.lcd_string("           Salir",LCD.LINE_2)
            else:
                LCD.lcd_string("Apagar          ",LCD.LINE_2)
    
    while(auxiliar):
        if(apagar):
            LCD.lcd_string("****Apagando****",LCD.LINE_1)
            LCD.lcd_string("**Hasta Luego***",LCD.LINE_2)
            subprocess.run(["shutdown", "-h", "now"])
        else:
            auxiliar=False
    
    return
