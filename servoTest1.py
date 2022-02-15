"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Autor: Juan Elier Rosales Rosas
Fecha: 11/02/22
Descripción: Programa para mover un servomotor simulando la apertura de una puerta
	
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
###################################
#Declaración de modulos
###################################
import RPi.GPIO as GPIO
import time 

###################################
#Configuración de GPIO
###################################
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT) #Se configura el pin 12 como salida
servo = GPIO.PWM(11, 50) # 12 es el pin y 50 el pulso en Hz

#Declaración de variables
servo.start(0)
abierto = int(input("Esperando: "))

###################################
#Condicionante para abrir puerta
###################################
if (abierto == 1):

    print("Puerta abierta")
    servo.ChangeDutyCycle(7)
    time.sleep(2)
    
elif(abierto == 0):
    print("Puerta cerrada")
    servo.ChangeDutyCycle(2)
    time.sleep(0.5)
    servo.ChangeDutyCycle(0)

servo.stop()
GPIO.cleanup()
