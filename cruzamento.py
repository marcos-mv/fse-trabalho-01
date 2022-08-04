from portas import cruzamento1, cruzamento2
from semaforo import Semaforo
from botoes import Botoes
from sensores import Sensores


class Cruzamento():

    def __init__(self, SEMAFORO_1_VERMELHO, SEMAFORO_1_AMARELO,
                 SEMAFORO_1_VERDE, SEMAFORO_2_VERMELHO,
                 SEMAFORO_2_AMARELO, SEMAFORO_2_VERDE,
                 BOTAO_PEDESTRE_1, BOTAO_PEDESTRE_2,
                 SENSOR_PASSAGEM_1, SENSOR_VELOCIDADE_1_A,
                 SENSOR_VELOCIDADE_1_B, SENSOR_PASSAGEM_2,
                 SENSOR_VELOCIDADE_2_A,
                 SENSOR_VELOCIDADE_2_B,
                 numeroCruzamento):

        self.SEMAFORO_1_VERMELHO = SEMAFORO_1_VERMELHO
        self.SEMAFORO_1_AMARELO = SEMAFORO_1_AMARELO
        self.SEMAFORO_1_VERDE = SEMAFORO_1_VERDE

        self.SEMAFORO_2_VERMELHO = SEMAFORO_2_VERMELHO
        self.SEMAFORO_2_AMARELO = SEMAFORO_2_AMARELO
        self.SEMAFORO_2_VERDE = SEMAFORO_2_VERDE

        self.BOTAO_PEDESTRE_1 = BOTAO_PEDESTRE_1
        self.BOTAO_PEDESTRE_2 = BOTAO_PEDESTRE_2

        self.SENSOR_PASSAGEM_1 = SENSOR_PASSAGEM_1
        self.SENSOR_PASSAGEM_2 = SENSOR_PASSAGEM_2

        self.SENSOR_VELOCIDADE_1_A = SENSOR_VELOCIDADE_1_A
        self.SENSOR_VELOCIDADE_1_B = SENSOR_VELOCIDADE_1_B

        self.SENSOR_VELOCIDADE_2_A = SENSOR_VELOCIDADE_2_A
        self.SENSOR_VELOCIDADE_2_B = SENSOR_VELOCIDADE_2_B

        self.estado = 0
        self.segundos = 0

        self.numeroCruzamento = numeroCruzamento

        self.semaforoPrincipal = Semaforo(SEMAFORO_VERMELHO=SEMAFORO_1_VERMELHO,SEMAFORO_AMARELO=SEMAFORO_1_AMARELO, SEMAFORO_VERDE=SEMAFORO_1_VERDE)
        self.semaforoSecundario = Semaforo(SEMAFORO_VERMELHO=SEMAFORO_2_VERMELHO,SEMAFORO_AMARELO=SEMAFORO_2_AMARELO, SEMAFORO_VERDE=SEMAFORO_2_VERDE)


        

        self.contador = 0
        self.tempo = 0

        def cicloCruzamento(self):
            print("inicia o cruzamento")
            if (self.estado == 0):

            
            elif()

            elif()

            elif()

            elif()

            elif()

            elif()

        
print(Cruzamento.semaforoPrincipal)

