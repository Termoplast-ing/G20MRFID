import RPi.GPIO as GPIO
import time
import datetime
import os
from libreria import teclado
from libreria import LCD_LIB_16x2 as LCD
from libreria import dienteAzul
from libreria import lib_dienteAzul

def DienteAzul():
    
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
    seleccion=True
    flagDisp=1
    conocido=1
    direccion=""
    
    
    while(seleccion):
        
        if (flagDisp>20):
            flagDisp=1
        else:
            flagDisp=flagDisp+1
        if(key==""):     
            key=teclado.Teclado(key,count)
            #print(key)
        
        if((key=="Up")or(key=="Down")):
            if(conocido==1):
                conocido=2
            else:
                conocido=1
            key=""
        elif((key=="Right")or(key=="Left")):
            key=""
            if((conocido<1)or(conocido>2)):
                conocido=1
        elif(key=="Enter"):
            seleccion=False
            key=""
        else:
            key=""
        
        if(flagDisp<10):
            LCD.lcd_string("Cone Disp Existe",LCD.LINE_1)
            LCD.lcd_string("Confi Disp Nuevo",LCD.LINE_2)
        else:
            if(conocido==1):
                LCD.lcd_string(" ",LCD.LINE_1)
                LCD.lcd_string("Confi Disp Nuevo",LCD.LINE_2)
            elif(conocido==2):
                LCD.lcd_string("Cone Disp Existe",LCD.LINE_1)
                LCD.lcd_string(" ",LCD.LINE_2)
            else:
                conocido=1
    
    while ((not seleccion) and ((conocido==1) or (conocido==2))):
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
            
            
    if(conocido==1):
        direccion = str(digText[0])+str(digText[1])+":"+str(digText[2])+str(digText[3])+":"+str(digText[4])+str(digText[5])+":"+str(digText[6])+str(digText[7])+":"+str(digText[8])+str(digText[9])+":"+str(digText[10])+str(digText[11])
        lib_dienteAzul.dienteazul(direccion)
        time.sleep(20)
    elif(conocido==2):
        LCD.lcd_string("chau",LCD.LINE_1)
        LCD.lcd_string(mac,LCD.LINE_2)
    else:
        seleccion=True
    if(key=="Enter"):
        seleccion=True
    else:
        key=""
            
    
    return
