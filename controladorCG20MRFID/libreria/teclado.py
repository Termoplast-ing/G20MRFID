import RPi.GPIO as GPIO
import time
import datetime

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
GPIO.setup(29, GPIO.IN)
GPIO.setup(31, GPIO.IN)
GPIO.setup(33, GPIO.IN)
GPIO.setup(37, GPIO.IN)


def Teclado(key,count):
    
    if key =="Up":
        aux=1
    elif key =="Down":
        aux=2
    elif key =="Left":
        aux=3
    elif key =="Right":
        aux=4
    elif key =="Enter":
        aux=5
    elif key =="Menu":
        aux=6
    else:
        aux=0
        
    if (GPIO.input(7) and not GPIO.input(29) and not GPIO.input(31) and not GPIO.input(33) and not GPIO.input(37)):
        time.sleep(0.01)
        if (GPIO.input(7) and not GPIO.input(29) and not GPIO.input(31) and not GPIO.input(33) and not GPIO.input(37)):
            aux=1
            
    elif (not GPIO.input(7) and GPIO.input(29) and not GPIO.input(31) and not GPIO.input(33) and not GPIO.input(37)):
        time.sleep(0.1)
        if (not GPIO.input(7) and GPIO.input(29) and not GPIO.input(31) and not GPIO.input(33) and not GPIO.input(37)):
            aux=2
            
    elif (not GPIO.input(7) and not GPIO.input(29) and GPIO.input(31) and not GPIO.input(33) and not GPIO.input(37)):
        time.sleep(0.1)
        if (not GPIO.input(7) and not GPIO.input(29) and GPIO.input(31) and not GPIO.input(33) and not GPIO.input(37)):
            aux=3
            
    elif (not GPIO.input(7) and not GPIO.input(29) and not GPIO.input(31) and GPIO.input(33) and not GPIO.input(37)):
        time.sleep(0.1)
        if (not GPIO.input(7) and not GPIO.input(29) and not GPIO.input(31) and GPIO.input(33) and not GPIO.input(37)):
            aux=4
            
    elif (not GPIO.input(7) and not GPIO.input(29) and not GPIO.input(31) and not GPIO.input(33) and GPIO.input(37)):
        time.sleep(0.1)
        while (not GPIO.input(7) and not GPIO.input(29) and not GPIO.input(31) and not GPIO.input(33) and GPIO.input(37)):
            if count > 50:
                aux=6
            else:
                aux=5
                
        
   # if not(GPIO.input(7) or GPIO.input(29) or GPIO.input(31) or GPIO.input(33) or GPIO.input(37)):
    if aux == 1:
        key="Up"
    elif aux == 2:
        key="Down"
    elif aux == 3:
        key="Left"
    elif aux == 4:
        key="Right"
    elif aux == 5:
        key="Enter"
    elif aux == 6:
        key="Menu"
    else:
        key=""
    
    
    return key