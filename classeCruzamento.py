from msilib.schema import Class
from gpiozero import LED, Button
from time import sleep

Class Cruzamento:

    def __init__(self, vermelho1, amarelo1, verde1, vermelho2, amarelo2, verde2,
        botaoPedestre1, botaoPedreste2, presenca1, presenca2, numeroCruzamento):
    
        self.SEMAFORO_1_VERMELHO = SEMAFORO_1_VERMELHO,
        self.SEMAFORO_1_AMARELO = SEMAFORO_1_AMARELO,
        self.SEMAFORO_1_VERMELHO = SEMAFORO_1_VERDE,

        self.SEMAFORO_2_VERMELHO = SEMAFORO_2_VERMELHO,
        self.SEMAFORO_2_AMARELO = SEMAFORO_2_AMARELO,
        self.SEMAFORO_2_VERDE = SEMAFORO_2_VERDE,

        self.BOTAO_PEDESTRE_1 = BOTAO_PEDESTRE_1,
        self.BOTAO_PEDESTRE_2 = BOTAO_PEDESTRE_2 ,

        self.SENSOR_PASSAGEM_1 = SENSOR_PASSAGEM_1,
        self.SENSOR_PASSAGEM_2 = SENSOR_PASSAGEM_2,

        self.SENSOR_VELOCIDADE_1_A = SENSOR_VELOCIDADE_1_A,
        self.SENSOR_VELOCIDADE_1_B = SENSOR_VELOCIDADE_1_B,

        self.SENSOR_VELOCIDADE_2_A = SENSOR_VELOCIDADE_2_A,
        self.SENSOR_VELOCIDADE_2_B = SENSOR_VELOCIDADE_2_B
    )

cruzamento = Cruzamento(1,2,3,4,5,6,7,8,9,10,11)

print(cruzamento.numeroCruzamento)
