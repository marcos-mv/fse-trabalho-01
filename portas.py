from cruzamento import Cruzamento
from semaforo import Semaforo
from sensorPresenca import SensorPresenca
from sensorVelocidade import SensorVelocidade
from botoes import Botoes

cruzamento1 = Cruzamento(
    SEMAFORO_1_VERMELHO = 21,
    SEMAFORO_1_AMARELO = 26,
    SEMAFORO_1_VERDE = 1,

    SEMAFORO_2_VERMELHO = 12,
    SEMAFORO_2_AMARELO = 16,
    SEMAFORO_2_VERDE = 20,

    BOTAO_PEDESTRE_1 = 8,
    BOTAO_PEDESTRE_2 = 7,

    SENSOR_PASSAGEM_1 = 14,
    SENSOR_PASSAGEM_2 = 15,

    SENSOR_VELOCIDADE_1_A = 18,
    SENSOR_VELOCIDADE_1_B = 23,

    SENSOR_VELOCIDADE_2_A = 24,
    SENSOR_VELOCIDADE_2_B = 25,

    numeroCruzamento=1
)

cruzamento2 = Cruzamento(

SEMAFORO_1_VERMELHO = 6,
SEMAFORO_1_AMARELO = 5,
SEMAFORO_1_VERDE = 0,

SEMAFORO_2_VERMELHO = 11,
SEMAFORO_2_AMARELO = 3,
SEMAFORO_2_VERDE = 2,

BOTAO_PEDESTRE_1 = 10,
BOTAO_PEDESTRE_2 = 9,

SENSOR_PASSAGEM_1 = 4,
SENSOR_PASSAGEM_2 = 17,

SENSOR_VELOCIDADE_1_A = 27,
SENSOR_VELOCIDADE_1_B = 22,

SENSOR_VELOCIDADE_2_A = 13,
SENSOR_VELOCIDADE_2_B = 19,
numeroCruzamento= 2
)

print(Cruzamento.cruzamento1)




# SEMAFORO_1_VERMELHO = LED(21),
#     SEMAFORO_1_AMARELO = LED(26),
#     SEMAFORO_1_VERDE = LED(1),

#     SEMAFORO_2_VERMELHO = LED(12),
#     SEMAFORO_2_AMARELO = LED(16),
#     SEMAFORO_2_VERDE = LED(20),

#     BOTAO_PEDESTRE_1 = Button(8),
#     BOTAO_PEDESTRE_2 = Button(7),

#     SENSOR_PASSAGEM_1 = Button(14),
#     SENSOR_PASSAGEM_2 = Button(15),

#     SENSOR_VELOCIDADE_1_A = Button(18),
#     SENSOR_VELOCIDADE_1_B = Button(23),

#     SENSOR_VELOCIDADE_2_A = Button(24),
#     SENSOR_VELOCIDADE_2_B = Button(25))