Código de python:

 

import serial

ser = serial.Serial('COM3', 9600)

while True:

    entrada = input("Introduce el angulo: ")

    ser.write(str(entrada).encode())