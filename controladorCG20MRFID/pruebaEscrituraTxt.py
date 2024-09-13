        
#def GuardarDatoReal(caravana,peso,hora):

peso=5000
hora=20
caravana=112233080445566
    
texto=open("/home/avila-brian/Desktop/pruebaEscrituraBD.txt", "w")

texto.write(str(caravana)+str(peso)+str(hora)+"\n")


texto.close()