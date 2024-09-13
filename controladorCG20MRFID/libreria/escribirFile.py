class DatosAnimal:
    def __init__(self, number: str,dayStart: str,dayDiet: str,load: str,horary: str,eat: str):
        self.number = number
        self.dayStart = dayStart
        self.dayDiet = dayDiet
        self.load = load
        self.horary = horary
        self.eat= eat

import time
from datetime import datetime, time

def GuardarDatoReal(Caravana):
    
    texto=open("./archivos/datoReal.txt", "w")

    for i in range(len(Caravana)):
        texto.write(str(Caravana[i].number)+str(Caravana[i].dayStart)+str(Caravana[i].dayDiet)+str(Caravana[i].load)+str(Caravana[i].eat)+str(Caravana[i].dispensed)+"\n")
    
    texto.close()
