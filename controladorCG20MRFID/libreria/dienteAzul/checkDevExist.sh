#!/bin/bash

read mac

dispositivo="B8:27:EB:14:1F:4C"
emparejado=""
equipoExistente=""
auxConectado=""
conectado=0

bluetoothctl power on
bluetoothctl list
bluetoothctl select "$dispositivo"
bluetoothctl trust "$mac"

auxEmparejado=$(bluetoothctl paired-devices)

echo "$auxEmparejado"




#if [[ $auxEmparejado == *$mac* ]]; then
#	echo "conecte el dispositivo cuando este listo presione enter"
#	read
#	auxConectado=$(bluetoothctl info)
#	echo "$auxConectado"
#	if [[ $auxConectado == *$mac* ]]; then
#		echo "conexion exitosa"
#		conectado=1
#	else
#		echo "conexion fallida...debe reemparejar el dispositivo esta de acuerdo s/n"
#		read equipoExistente
#		if [ $equipoExistente == "s" ]; then
#			bluetoothctl pairable on
#			bluetoothctl discoverable on
#			bluetoothctl scan on&
#			sleep 20
#			bluetoothctl trust "$mac"
#			bluetoothctl pair "$mac"
#			bluetoothctl scan off&
#			sleep 30
#			bluetoothctl trust "$mac"
#			bluetoothctl connect "$mac"
#		else
#			echo "conexion fallida...finalizado"
#		fi
#	fi
#else
#	echo "mac no reconocida"
