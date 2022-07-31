from msilib.schema import Class
from gpiozero import LED, Button
from gpiozero import LED
from time import sleep

led = LED(1)
led2 = LED(26)
led3 = LED(21)

Class Cruzamento1:


def __init__(self):

    cruzamento1=(
    SEMAFORO_1_VERMELHO = LED(21),
    SEMAFORO_1_AMARELO = LED(26),
    SEMAFORO_1_VERDE = LED(1),

    SEMAFORO_2_VERMELHO = LED(12),
    SEMAFORO_2_AMARELO = LED(16),
    SEMAFORO_2_VERDE = LED(20),

    BOTAO_PEDESTRE_1 = Button(8),
    BOTAO_PEDESTRE_2 = Button(7),

    SENSOR_PASSAGEM_1 = Button(14),
    SENSOR_PASSAGEM_2 = Button(15),

    SENSOR_VELOCIDADE_1_A = Button(18),
    SENSOR_VELOCIDADE_1_B = Button(23),

    SENSOR_VELOCIDADE_2_A = Button(24),
    SENSOR_VELOCIDADE_2_B = Button(25))


# Class Cruzamento2:

#     def __init__(self):


#         SEMAFORO_1_VERMELHO = LED(11)
#         SEMAFORO_1_AMARELO = LED(3)
#         SEMAFORO_1_VERDE = LED(2)

#         SEMAFORO_2_VERMELHO = LED(6)
#         SEMAFORO_2_AMARELO = LED(5)
#         SEMAFORO_2_VERDE = LED(0)

#         BOTAO_PEDESTRE_1 = Button(10)
#         BOTAO_PEDESTRE_2 = Button(9)

#         SENSOR_PASSAGEM_1 = Button(4)
#         SENSOR_PASSAGEM_2 = Button(17)

#         SENSOR_VELOCIDADE_1_A = Button(27)
#         SENSOR_VELOCIDADE_1_B = Button(22)

#         SENSOR_VELOCIDADE_2_A = Button(13)
#         SENSOR_VELOCIDADE_2_B = Button(19)


while True:
    led.on()
    led2.on()
    led3.on()
    sleep(1)
    led.off()
    led2.off()
    led3.off()
    sleep(1)
