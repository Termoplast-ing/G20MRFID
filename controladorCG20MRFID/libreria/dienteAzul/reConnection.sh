#!/bin/bash

read mac

dispositivo="B8:27:EB:14:1F:4C"

bluetoothctl power on
bluetoothctl list
bluetoothctl select "$dispositivo"
bluetoothctl remove "$mac"

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
bluetoothctl info
