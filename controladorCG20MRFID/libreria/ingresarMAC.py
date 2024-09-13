import RPi.GPIO as GPIO
import time
import datetime
import os
from libreria import teclado
from libreria import LCD_LIB_16x2 as LCD
from libreria import ingresarMAC
from libreria import lib_dienteAzul

def IngresarMAC():
    
    intToHex= {
        10:"A",
        11:"B",
        12:"C",
        13:"D",
        14:"E",
        15:"F",
    }
    digText=["0","0","0","0","0","0","0","0","0","0","0","0"]
    digito=[0,0,0,0,0,0,0,0,0,0,0,0]
    dig=0
    mac=""
    key=""
    count=0
    seleccion=False
    flagDisp=1
    conocido=1
    direccion=""
    
    while (not seleccion):
        if (flagDisp>20):
            flagDisp=1
        else:
            flagDisp=flagDisp+1
        if(key==""):     
            key=teclado.Teclado(key,count)
            #print(key)
            LCD.lcd_string(" Ingrese La MAC ",LCD.LINE_1)
            
        if(key=="Up"):
            digito[dig]=digito[dig]+1
            if(digito[dig]>15):
                digito[dig]=1
            elif(digito[dig]<0):
                digito[dig]=15
            if(digito[dig]<10):
                digText[dig]=str(digito[dig])
            else:
                digText[dig]=intToHex[digito[dig]]
            key=""
                
        elif(key=="Down"):
            digito[dig]=digito[dig]-1
            if(digito[dig]>15):
                digito[dig]=1
            elif(digito[dig]<0):
                digito[dig]=15
            if(digito[dig]<10):
                digText[dig]=str(digito[dig])
            else:
                digText[dig]=intToHex[digito[dig]]
            key=""
                
        elif(key=="Left"):
            dig=dig+1
            if(dig>11):
                dig=0
            elif(dig<0):
                dig=11
            key=""
            
        elif(key=="Right"):
            dig=dig-1
            if(dig>11):
                dig=0
            elif(dig<0):
                dig=11
            key=""
                
        elif(key=="Enter"):
            seleccion=True
        
        if(flagDisp<10):
            LCD.lcd_string("**"+str(digText[0])+str(digText[1])+str(digText[2])+str(digText[3])+
                           str(digText[4])+str(digText[5])+str(digText[6])+str(digText[7])+
                           str(digText[8])+str(digText[9])+str(digText[10])+str(digText[11])+"**",LCD.LINE_2)
        else:
            if(dig==0):
                LCD.lcd_string("**"+" "+str(digText[1])+str(digText[2])+str(digText[3])+str(digText[4])+str(digText[5])+str(digText[6])+str(digText[7])+str(digText[8])+str(digText[9])+str(digText[10])+str(digText[11])+"**",LCD.LINE_2)   
            elif(dig==1):
                LCD.lcd_string("**"+str(digText[0])+" "+str(digText[2])+str(digText[3])+str(digText[4])+str(digText[5])+str(digText[6])+str(digText[7])+str(digText[8])+str(digText[9])+str(digText[10])+str(digText[11])+"**",LCD.LINE_2) 
            elif(dig==2):
                LCD.lcd_string("**"+str(digText[0])+str(digText[1])+" "+str(digText[3])+str(digText[4])+str(digText[5])+str(digText[6])+str(digText[7])+str(digText[8])+str(digText[9])+str(digText[10])+str(digText[11])+"**",LCD.LINE_2)
            elif(dig==3):
                LCD.lcd_string("**"+str(digText[0])+str(digText[1])+str(digText[2])+" "+str(digText[4])+str(digText[5])+str(digText[6])+str(digText[7])+str(digText[8])+str(digText[9])+str(digText[10])+str(digText[11])+"**",LCD.LINE_2)
            elif(dig==4):
                LCD.lcd_string("**"+str(digText[0])+str(digText[1])+str(digText[2])+str(digText[3])+" "+str(digText[5])+str(digText[6])+str(digText[7])+str(digText[8])+str(digText[9])+str(digText[10])+str(digText[11])+"**",LCD.LINE_2)
            elif(dig==5):
                LCD.lcd_string("**"+str(digText[0])+str(digText[1])+str(digText[2])+str(digText[3])+str(digText[4])+" "+str(digText[6])+str(digText[7])+str(digText[8])+str(digText[9])+str(digText[10])+str(digText[11])+"**",LCD.LINE_2)
            elif(dig==6):
                LCD.lcd_string("**"+str(digText[0])+str(digText[1])+str(digText[2])+str(digText[3])+str(digText[4])+str(digText[5])+" "+str(digText[7])+str(digText[8])+str(digText[9])+str(digText[10])+str(digText[11])+"**",LCD.LINE_2)
            elif(dig==7):
                LCD.lcd_string("**"+str(digText[0])+str(digText[1])+str(digText[2])+str(digText[3])+str(digText[4])+str(digText[5])+str(digText[6])+" "+str(digText[8])+str(digText[9])+str(digText[10])+str(digText[11])+"**",LCD.LINE_2)
            elif(dig==8):
                LCD.lcd_string("**"+str(digText[0])+str(digText[1])+str(digText[2])+str(digText[3])+str(digText[4])+str(digText[5])+str(digText[6])+str(digText[7])+" "+str(digText[9])+str(digText[10])+str(digText[11])+"**",LCD.LINE_2) 
            elif(dig==9):
                LCD.lcd_string("**"+str(digText[0])+str(digText[1])+str(digText[2])+str(digText[3])+str(digText[4])+str(digText[5])+str(digText[6])+str(digText[7])+str(digText[8])+" "+str(digText[10])+str(digText[11])+"**",LCD.LINE_2)
            elif(dig==10):
                LCD.lcd_string("**"+str(digText[0])+str(digText[1])+str(digText[2])+str(digText[3])+str(digText[4])+str(digText[5])+str(digText[6])+str(digText[7])+str(digText[8])+str(digText[9])+" "+str(digText[11])+"**",LCD.LINE_2)
            elif(dig==11):
                LCD.lcd_string("**"+str(digText[0])+str(digText[1])+str(digText[2])+str(digText[3])+str(digText[4])+str(digText[5])+str(digText[6])+str(digText[7])+str(digText[8])+str(digText[9])+str(digText[10])+" "+"**",LCD.LINE_2) 
            
            
    if(seleccion):
        direccion = str(digText[0])+str(digText[1])+":"+str(digText[2])+str(digText[3])+":"+str(digText[4])+str(digText[5])+":"+str(digText[6])+str(digText[7])+":"+str(digText[8])+str(digText[9])+":"+str(digText[10])+str(digText[11])
#        lib_dienteAzul.dienteazul(direccion)
        
            
    
    return direccion
    
