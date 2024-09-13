#!/bin/bash



dispositivo="B8:27:EB:14:1F:4C"
mac=""
yes="yes"
emparejado=""
equipoExistente=""
auxConectado=""
conectado=0

bluetoothctl power on
bluetoothctl list
bluetoothctl select "$dispositivo"

auxEmparejado=$(bluetoothctl paired-devices)

echo "$auxEmparejado"


if [[ $auxEmparejado == *$mac* ]]; then
	echo "conecte el dispositivo cuando este listo presione enter"
	read
	auxConectado=$(bluetoothctl info)
	echo "$auxConectado"
	if [[ $auxConectado == *$mac* ]]; then
		echo "conexion exitosa"
		conectado=1
	else
		echo "conexion fallida...debe reemparejar el dispositivo esta de acuerdo s/n"
		read equipoExistente
		if [ $equipoExistente == "s" ]; then
			bluetoothctl pairable on
			bluetoothctl discoverable on
			bluetoothctl scan on&
			sleep 20
			bluetoothctl trust "$mac"
			bluetoothctl pair "$mac"
			bluetoothctl scan off&
			sleep 30
			bluetoothctl trust "$mac"
			bluetoothctl connect "$mac"
		else
			echo "conexion fallida...finalizado"
		fi
	fi
else

	bluetoothctl pairable on
	bluetoothctl discoverable on
	bluetoothctl scan on&
	sleep 20
	bluetoothctl trust "$mac"
	bluetoothctl pair "$mac"
	bluetoothctl scan off&
	sleep 30
	bluetoothctl trust "$mac"
	bluetoothctl connect "$mac"

fi

echo "FINALIZADO"

read



