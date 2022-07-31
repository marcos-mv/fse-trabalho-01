from msilib.schema import Class
from gpiozero import LED, Button
from time import sleep


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