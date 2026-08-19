import serial
import time


# coloque a porta do seu Arduino
arduino = serial.Serial("COM3", 9600)

time.sleep(2)


print("Abrindo torneira")

arduino.write(b"ABRIR")

time.sleep(8)


print("Fechando torneira")

arduino.write(b"FECHAR")


arduino.close()