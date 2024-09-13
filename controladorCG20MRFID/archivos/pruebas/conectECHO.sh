#!/bin/bash

#mac="F8:1F:32:B6:CF:A0"
#mac="48:F1:7F:3A:D2:9C"
mac="$1"

dispositivo="B8:27:EB:14:1F:4C"

{	echo "power on"
	sleep 1
	echo "remove $mac"
	sleep 1
} | bluetoothctl

{	echo "power off"
	sleep 5
	echo "power on"
	sleep 1
	echo "agent on"
	sleep 1
	echo "agent off"
	sleep 1
	echo "agent NoInputNoOutput"
	sleep 1
	echo "power on"
	sleep 1
	echo "discoverable on"
	sleep 1
	echo "pairable on"
	sleep 1
	echo "list"
	sleep 1
	echo "select $dispositivo"
	sleep 1
#echo "agent off"
#sleep 1
#echo "agent NoInputNoOutput"
#sleep 1
	echo "scan on"
	sleep 30
	echo "pair $mac"
	sleep 15
	echo "connect $mac"
	sleep 15
} | bluetoothctl
