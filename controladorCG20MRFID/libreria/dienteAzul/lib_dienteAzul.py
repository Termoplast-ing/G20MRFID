import subprocess
from libreria import lib_dienteAzul

def dienteBlue(direccion):
    
    devPair=False
    devConnectAux=False

    MAC=direccion
    #F8:1F:32:B6:CF:A0
    MACaux=bytes(MAC,'UTF-8')

    devExist=subprocess.run(['bash','/home/avila-brian/Desktop/pruebaEjecBashPython/checkDevExist.sh','import sys','sys.stdin.read()'], input=MACaux, stdout=subprocess.PIPE)

    outConect=str(devExist.stdout, encoding='utf-8')

    print(outConect)

    if(not(MAC + " not available" in outConect)):
        print("si esta")
        devPair=True
    else:
        print("nop")
        devPair=False
        
    checkConnect=subprocess.run(['bluetoothctl','info'], stdout=subprocess.PIPE)
    connectOK=(str(checkConnect.stdout, encoding='utf-8'))

    if((devPair) and (not(MAC in connectOK))):
        reconnection=0
        print("2")
        while((reconnection<3) and (not devConnectAux)):
            print("3")
            if(reconnection > 0):
                print("por favor vueltalo a intentar")
            else:
                print("conecte el dispositivo cuando este listo presione enter")
            
            input()
            
            devConnect=subprocess.run(['bash','/home/avila-brian/Desktop/pruebaEjecBashPython/checkConnection.sh','import sys','sys.stdin.read()'], input=MACaux, stdout=subprocess.PIPE)
        
            connectOK=str(devConnect.stdout, encoding='utf-8')
            
            print(connectOK)
            
            MACdev="Device "+ MAC
        
            if(MACdev in connectOK) and ("Connected: yes" in connectOK):
                print("conexion extablecida")
                devConnectAux=True
            else:
                print("conexion fallida")
                devConnectAux=False
                reconnection=reconnection+1
                
        if((not devConnectAux) and (reconnection>=3)):    
            reconnection=0
            print("conexion fallidas")
            print("es necesario volver a emparejar dispositivo")
            
            devConnect=subprocess.run(['bash','/home/avila-brian/Desktop/pruebaEjecBashPython/reConnection.sh','import sys','sys.stdin.read()'], input=MACaux, stdout=subprocess.PIPE)
        
            reconnectOK=str(devConnect.stdout, encoding='utf-8')
            
            if(MAC in reconnectOK):
                print("conexion extablecida")
                devConnectAux=True
            else:
                print("conexion fallida")
                devConnectAux=False
                
    elif(not devPair):
        
        devConnect=subprocess.run(['bash','/home/avila-brian/Desktop/pruebaEjecBashPython/reConnection.sh','import sys','sys.stdin.read()'], input=MACaux, stdout=subprocess.PIPE)
        
        connectOk=str(devConnect.stdout, encoding='utf-8')
        
        if(MAC in reconnectOK):
            print("conexion extablecida")
            devConnectAux=True
        else:
            print("conexion fallida")
            devConnectAux=False
                
    else:
        print("conectado")
        
    return
    
        