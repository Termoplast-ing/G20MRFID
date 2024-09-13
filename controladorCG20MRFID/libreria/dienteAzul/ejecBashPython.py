import subprocess

popo=input()

popo1=bytes(popo,'UTF-8')

pipi=subprocess.run(['bluetoothctl','info'], stdout=subprocess.PIPE)

print(pipi.stdout)

print(str(pipi.stdout, encoding='utf-8') + "ahora si")
