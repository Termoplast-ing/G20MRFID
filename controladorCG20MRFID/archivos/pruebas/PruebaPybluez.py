import bluetooth

encontrado=False
mac="F8:1F:32:B6:CF:A0"
devices = bluetooth.discover_devices()
agente=bluetooth.


while(not encontrado):
    for device in devices:
        print(device)
        if(device==mac):
            print("encontrado")
            encontrado=True

print("holis")

bluetooth.bind()