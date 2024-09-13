import RPi.GPIO as GPIO
import time
import datetime
import os
import subprocess
from libreria import teclado
from libreria import LCD_LIB_16x2 as LCD
from libreria import dienteAzul
from libreria import lib_dienteAzul

def dienteazul():

    #dirMAC="F8:1F:32:B6:CF:A0"
    dirMAC="48:F1:7F:3A:D2:9C"
    pasos=0
    flagDisp=0
    count=0
    key=""
    enviar=False
    conectado=False
    MACnueva=True
    reciVARok=False
    

    while(pasos==0):
        if (flagDisp>20):
            flagDisp=1
        else:
            flagDisp=flagDisp+1
        if(key==""):     
            key=teclado.Teclado(key,count)
    
        if((key=="Up")or(key=="Down")):
            if(enviar):
                enviar=False
            else:
                enviar=True
            key=""
        elif((key=="Right")or(key=="Left")):
            key=""
        elif(key=="Enter"):
            pasos=1
            key=""
        else:
            key=""
    
        if(flagDisp<10):
            LCD.lcd_string("     ENVIAR     ",LCD.LINE_1)
            LCD.lcd_string("    RECIBIR    ",LCD.LINE_2)
        else:
            if(enviar):
                LCD.lcd_string(" ",LCD.LINE_1)
                LCD.lcd_string("    RECIBIR    ",LCD.LINE_2)
            else:
                LCD.lcd_string("     ENVIAR     ",LCD.LINE_1)
                LCD.lcd_string(" ",LCD.LINE_2)
    
    dispositivos = subprocess.run(["bluetoothctl","disconnect"], capture_output=True, text=True)

    if(enviar):
        #dispositivos = subprocess.run(["sudo","service","bluetooth","restart"],capture_output=True, text=True)
        canal=subprocess.Popen(["sudo","service","bluetooth","restart"], text=True, stdout=subprocess.PIPE)
        #dispositivos = subprocess.run(["hcitool","scan"],capture_output=True, text=True)
        canal=subprocess.Popen(["hcitool","scan"], text=True, stdout=subprocess.PIPE)
        canal=subprocess.Popen(["sudo","obexpushd","-B12","-o","/bluetooth","-n"], text=True, stdout=subprocess.PIPE)
    else:
        canal = subprocess.Popen(["sudo","obexpushd","-B9","-o","/bluetooth","-n"], text=True, stdout=subprocess.PIPE)
    
    while(not conectado):
        conectado,MACnueva=conectAR(MACnueva,dirMAC)

    if(conectado):
        while(not reciVARok):
            reciVAR(enviar,dirMAC)
        return True
    else:
        return False            

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
            key=""
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
                    LCD.lcd_string("Conexion Fallida",LCD.LINE_1)
                    LCD.lcd_string("vuelva intentar ",LCD.LINE_2)
                    time.sleep(3)
                    key=""
                    return False
                else:
                    key==""
            dispositivos = subprocess.run(["bluetoothctl","info",dirMAC],capture_output=True, text=True)
            print(dispositivos.stdout)
            if("Connected: yes" in dispositivos.stdout):
                LCD.lcd_string("Conexion Exitosa",LCD.LINE_1)
                LCD.lcd_string("",LCD.LINE_2)
                time.sleep(3)
                return True
            #else:
            #    LCD.lcd_string("Conexion Fallida",LCD.LINE_1)
            #    LCD.lcd_string("vuelva intentar ",LCD.LINE_2)
            #    time.sleep(3)
            #    return False
    else:
        dispositivos = subprocess.Popen(["sh","/home/Termoplast/Desktop/proyectos/CG20MRFID/controlador/software/controladorCG20MRFID/archivos/pruebas/conect.sh",dirMAC], text=True, stdout=subprocess.PIPE)
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

def conectAR(MACnueva,dirMAC):
    count=0
    MACaux=True
    conecFallidaAUX=0
    key=""
    again="SI"
    MACnuevaAUX=0
    newMAC="SI"

    if(MACnueva):
        dirMAC=IngresarMAC()

    conected=YaEmparejado(dirMAC)

    if(conected):
        return True,False
    else:
        conecFallida=True
        LCD.lcd_string("Conexion Fallida",LCD.LINE_1)
        while(conecFallida):
            if(conecFallidaAUX>20):
                conecFallidaAUX=0
            else:
                conecFallidaAUX=conecFallidaAUX+1
            if(conecFallidaAUX>10):
                LCD.lcd_string("Reinterntar?  "+again,LCD.LINE_2)
            else:
                LCD.lcd_string("Reinterntar?",LCD.LINE_2)
            if(key==""):     
                key=teclado.Teclado(key,count)
            if((key=="Up")or(key=="Down")):
                if(again=="SI"):
                    again="NO"
                else:
                    again="SI"
                key=""
            elif((key=="Right")or(key=="Left")):
                key=""
            elif(key=="Enter"):
                key=""
                if(again=="SI"):
                    while(MACaux):
                        LCD.lcd_string("Desea  ingresar ",LCD.LINE_1)
                        if(MACnuevaAUX>20):
                            MACnuevaAUX=0
                        else:
                            MACnuevaAUX=MACnuevaAUX+1
                        if(MACnuevaAUX<10):
                            LCD.lcd_string("Nueva MAC?    "+newMAC,LCD.LINE_2)
                        else:
                            LCD.lcd_string("Nueva MAC?",LCD.LINE_2)
                        if(key==""):     
                            key=teclado.Teclado(key,count)
                        if((key=="Up")or(key=="Down")):
                            if(newMAC=="SI"):
                                newMAC="NO"
                            else:
                                newMAC="SI"
                            key=""
                        elif((key=="Right")or(key=="Left")):
                            key=""
                        elif(key=="Enter"):
                            if(newMAC=="SI"):
                                return False,True
                            else:
                                key=""
                                return False,False
                        else:
                            key=""
                else:
                    key=""
                    return True,False
            else:
                key=""

def reciVAR(enviar,dirMAC):

    enviado=False
    recibido=False

    if(enviar):
        enviado=True
        recibido=False
    else:
        enviado=False
        recibido=True

    if(enviar):
        while(enviado):
            canal=subprocess.Popen(["obexftp","--nopath","--noconn","--uuid","none","bluetooth",dirMAC,"--channel","12","-p","/bluetooth/prueba.txt"], text=True, stdout=subprocess.PIPE)
    else:
        canal=subprocess.Popen(["sudo","obexpushd","-B9","-o","/bluetooth","-n"], text=True, stdout=subprocess.PIPE)
        while(recibido):
            recibido=False