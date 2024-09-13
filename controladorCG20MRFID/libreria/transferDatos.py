import RPi.GPIO as GPIO
import time
import datetime
import os
import subprocess
from libreria import teclado
from libreria import LCD_LIB_16x2 as LCD
from libreria import transferDatos



def TransferirDatos(dirMac):
    
    flagDisp=0
    key=""
    count=0
    envRec=False
    envRecAUX=False
    conExito= False
    
    
    
    while(not envRecAUX):
        
        if (flagDisp>20):
            flagDisp=1
        else:
            flagDisp=flagDisp+1
        if(key==""):     
            key=teclado.Teclado(key,count)
            #print(key)
        
        if((key=="Up")or(key=="Down")):
            if(envRec):
                envRec=False
            else:
                envRec=True
            key=""
        elif((key=="Right")or(key=="Left")):
            key=""
        elif(key=="Enter"):
            envRecAUX=True
            key=""
        else:
            key=""
        
        if(flagDisp<10):
            LCD.lcd_string("     ENVIAR     ",LCD.LINE_1)
            LCD.lcd_string("    RECIBIR    ",LCD.LINE_2)
        else:
            if(envRec):
                LCD.lcd_string(" ",LCD.LINE_1)
                LCD.lcd_string("    RECIBIR    ",LCD.LINE_2)
            else:
                LCD.lcd_string("     ENVIAR     ",LCD.LINE_1)
                LCD.lcd_string(" ",LCD.LINE_2)
    
    while(envRecAUX):
        while(not conExito):
            if(envRec):
                print("hola")
            else:
                print("chauchis")
            
        
    return


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
    
def YaEmparejado(dirMAC):

    #dirMAC="F8:1F:32:B6:CF:A0"
    dirMAC="48:F1:7F:3A:D2:9C"
    conectado=False
    auxConectado=0
    key=""
    count=0
    parejar=False
    auxParejar=0

    dispositivo = subprocess.run(["bluetoothctl","paired-devices"],capture_output=True, text=True, check=True)
    print(dispositivo.stdout)

    if(dirMAC in dispositivo.stdout):
        dispositivos = subprocess.run(["bluetoothctl","trust",dirMAC],capture_output=True, text=True)
        print(dispositivos.stdout)
        while(not conectado):
            auxConectado=auxConectado+1
            if(auxConectado>20):
                auxConectado=0
            if(auxConectado>10):
                LCD.lcd_string("conecte su disp.",LCD.LINE_1)
                LCD.lcd_string("CG20MRFID  Salir",LCD.LINE_2)
            else:
                LCD.lcd_string("conecte su disp.",LCD.LINE_1)
                LCD.lcd_string("CG20MRFID ",LCD.LINE_2)
            if(key==""):
                key=teclado.Teclado(key,count)
            else:
                if(key=="Enter"):
                    return False
                else:
                    key==""
            dispositivos = subprocess.run(["bluetoothctl","info",dirMAC],capture_output=True, text=True)
            print(dispositivos.stdout)
            if("Connected: yes" in dispositivos.stdout):
                return True
            else:
                conectado=False
    else:
        dispositivos = subprocess.Popen(["sh","/home/Termoplast/Desktop/proyectos/CG20MRFID/controlador/software/controladorCG20MRFID/archivos/pruebas/conectECHO.sh",dirMAC], text=True, stdout=subprocess.PIPE)
        LCD.lcd_string("Acepte sincro en",LCD.LINE_1)
        while(not parejar):
            if(auxParejar>20):
                auxParejar=0
            else:
                auxParejar=auxParejar+1
            if(auxParejar>10):
                LCD.lcd_string("*su dispositivo*",LCD.LINE_2)
            else:
                LCD.lcd_string(" su dispositivo ",LCD.LINE_2)
            #stdout,stderr=dispositivos.communicate()
            #print(stderr)
            dispositivo = subprocess.run(["bluetoothctl","info",dirMAC],capture_output=True, text=True)
            print(dispositivo.stdout)
            if(("Connected: yes" in dispositivo.stdout) and ("Paired: yes" in dispositivo.stdout)):
                LCD.lcd_string("Conexion Exitosa",LCD.LINE_1)
                LCD.lcd_string("",LCD.LINE_2)
                time.sleep(3)
                return True
            else:
                LCD.lcd_string("Conexion Fallida",LCD.LINE_1)
                LCD.lcd_string("vuelva intentar ",LCD.LINE_2)
                time.sleep(3)
                return False
