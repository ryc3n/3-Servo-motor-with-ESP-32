# Script para mover 3 servo-motores cun un ESP-32 en MicroPython
# Creado por Sergio Saul  

from machine import Pin, PWM
from utime import sleep, sleep_ms

# Aqui se refleja la señal en la que esta conectado el servo-motor junto a la frecuencia.
servo = PWM (Pin(21), freq = 40)
servo1 = PWM (Pin(23), freq = 30)
servo2 = PWM (Pin (22), freq = 20)

# Aqui se refleja el radio y tiempo de respuesta a la que va a funcionar el servo-motor 
while True:

     for i in range(1800, 7000):
        servo.duty_u16(i)
        sleep_ms(1)
        servo1.duty_u16(i)
        sleep_ms(1)
        servo2.duty_u16(i)
        sleep_ms(1)
    
        