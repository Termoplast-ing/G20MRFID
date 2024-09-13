#!/bin/bash

read mac

dispositivo="B8:27:EB:14:1F:4C"

bluetoothctl power on
bluetoothctl list
bluetoothctl select "$dispositivo"
bluetoothctl trust "$mac"

auxConectado=$(bluetoothctl connect $mac)
sleep 30
echo "$auxConectado"
auxConectado=$(bluetoothctl info)
echo "$auxConectado"
