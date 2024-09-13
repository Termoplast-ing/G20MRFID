import subprocess
import os
import time
import datetime

mac="F8:1F:32:B6:CF:A0"
fallaConexion=False
print("1")
#enciende en bluetooth
aux = subprocess.run(["bluetoothctl power on"], shell=True, capture_output=True, text=True, check=True)
if(aux.stderr!=""):
    fallaConexion=True
print("2")
#se setea como visible
aux = subprocess.run(["bluetoothctl discoverable on"], shell=True, capture_output=True, text=True, check=True)
if(aux.stderr!=""):
    fallaConexion=True
print("3")
#se setea como emparejable
aux = subprocess.run(["bluetoothctl pairable on"], shell=True, capture_output=True, text=True, check=True)
if(aux.stderr!=""):
    fallaConexion=True
print("4")
print(fallaConexion)
#si hasta aca no hubo fallas sigue con el proceso de borrar la mac de los equipos ya conectados 
#anteriormente....sino se trata la falla
if(not fallaConexion):
    print("5")
    #revisa si la mac esta en los dipoditivos conectados anteriormente lo borra para volverlo a conectar
    #esto es necesario porque hay que iniciarlo como desconocido para que levante el canal FTP
    paired= subprocess.run(["bluetoothctl paired-devices"], shell=True, capture_output=True, text=True, check=True)
    if(paired.stderr!=""):
        fallaConexion=True
    print("6")
    if mac in paired.stdout:
        borrar=subprocess.run(["bluetoothctl remove " + mac], shell=True, capture_output=True, text=True, check=True)
        if(borrar.stderr!=""):
            fallaConexion=True
    print("7")
    print(fallaConexion)
os.system("bluetoothctl scan on &")
time.sleep(5)
cone=subprocess.Popen(['bluetoothctl', 'agent off'],stdout=subprocess.PIPE,encoding='utf-8')
time.sleep(5)
print(cone.stdout)
subprocess.Popen(['bluetoothctl', 'agent NoInputNoOutput'],stdout=subprocess.PIPE,encoding='utf-8')
time.sleep(5)
#time.sleep(1)
#if(not fallaConexion):
   # print("8")
    #apaga el agente por defecto
#subprocess.run(["bluetoothctl agent off"], shell=True, capture_output=True, text=True, check=True)
#time.sleep(1)
   # if(conexion.stderr!=""):
     #   fallaConexion=True
    #print("9")
    #vuelve a iniciar el agente pero del tipo NoInputNoOutput para que no pida pin de sincro
#subprocess.run(["bluetoothctl agent NoInputNoOutput"], shell=True, capture_output=True, text=True, check=True)
time.sleep(5)
os.system("bluetoothctl trust " + mac)
   # if(conexion.stderr!=""):
    #    fallaConexion=True
    #print("10")

#conexion=subprocess.run(["bluetoothctl scan on &"], shell=True, capture_output=True, text=True, check=True)
#if(conexion.stderr!=""):
#    fallaConexion=True
#print("11")
#print(conexion.stdout)
#print(conexion.stderr)
#while((not fallaConexion)and(not(mac in conexion.stdout))):

#    time.sleep(1)
print("2")
#conexion=subprocess.run(["bluetoothctl scan off"], shell=True, capture_output=True, text=True, check=True)
#if(conexion.stderr!="0"):
#    fallaConexion=True

#conexion=subprocess.run(["bluetoothctl trust" + mac], shell=True, capture_output=True, text=True, check=True)
#if(conexion.stderr!="0"):
#    fallaConexion=True
    
conexion=subprocess.run(["bluetoothctl pair " + mac], shell=True, capture_output=True, text=True, check=True)
if(conexion.stderr!="0"):
    fallaConexion=True

conexion=subprocess.run(["bluetoothctl scan on &"], shell=True, capture_output=True, text=True, check=True)
if(conexion.stderr!="0"):
    fallaConexion=True
    


    #result = subprocess.run(["bluetoothctl help"], shell=True, capture_output=True, text=True)

    #print(result.stdout)