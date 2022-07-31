from gpiozero import Button, LED, TrafficLights, Buzzer
from time import sleep

button = Button(8)

SEMAFORO_1_VERMELHO = LED(21)
SEMAFORO_1_AMARELO = LED(26)
SEMAFORO_1_VERDE = LED(1)

while True:
    button.wait_for_press()
    SEMAFORO_1_VERMELHO.on()
    SEMAFORO_1_VERDE.on()
    SEMAFORO_1_AMARELO.on()
    button.wait_for_release()
    SEMAFORO_1_VERMELHO.off()
    SEMAFORO_1_VERDE.off()
    SEMAFORO_1_AMARELO.off()