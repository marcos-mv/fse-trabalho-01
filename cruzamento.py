from cruzamento import Cruzamento
from semaforo import Semaforo
from sensorPresenca import SensorPresenca
from sensorVelocidade import SensorVelocidade
from botoes import Botoes
from portas import cruzamento1, cruzamento2


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


        #Inicializa Semaforos
        self.semaforoPrincipal = Semaforo(SEMAFORO_VERMELHO=SEMAFORO_1_VERMELHO,SEMAFORO_AMARELO=SEMAFORO_1_AMARELO, SEMAFORO_VERDE=SEMAFORO_1_VERDE)
        self.semaforoSecundario = Semaforo(SEMAFORO_VERMELHO=SEMAFORO_2_VERMELHO,SEMAFORO_AMARELO=SEMAFORO_2_AMARELO, SEMAFORO_VERDE=SEMAFORO_2_VERDE)

        #Inicializa Botoes Pedestes
        self.botaoPrincipal = Botoes(BOTAO_PEDESTRE=BOTAO_PEDESTRE_1)
        self.botaoSecundario = Botoes(BOTAO_PEDESTRE=BOTAO_PEDESTRE_2)

        #Inicializa Sensor de Presenca de Carros
        self.sensorPresenca1 = SensorPresenca(SENSOR_PASSAGEM=SENSOR_PASSAGEM_1)
        self.sensorPresenca2 = SensorPresenca(SENSOR_PASSAGEM=SENSOR_PASSAGEM_2)

        #Inicializa Sensores de velocidade
        self.sensorVelocidadeA1 = SensorVelocidade(SENSOR_VELOCIDADE=SENSOR_VELOCIDADE_1_A)
        self.sensorVelocidadeA2 = SensorVelocidade(SENSOR_VELOCIDADE=SENSOR_VELOCIDADE_1_B)
        self.sensorVelocidadeB1 = SensorVelocidade(SENSOR_VELOCIDADE=SENSOR_VELOCIDADE_2_A)
        self.sensorVelocidadeB2 = SensorVelocidade(SENSOR_VELOCIDADE=SENSOR_VELOCIDADE_2_B)

        self.contadorEstados = 0
        self.tempo = 0



    def cicloCruzamento(self):
        print("inicia o cruzamento")
        if (self.estado == 0):
            print("Estou no estado 0")

            self.estado=1
        elif(self.estado == 1):
            print("Estou no estado 1")
            self.estado=2

        elif(self.estado == 2):
            print("Estou no estado 2")
            self.estado=3

        elif(self.estado == 3):
            print("Estou no estado 3")
            self.estado=4

        elif(self.estado == 4):
            print("Estou no estado 4")
            self.estado=5

        else:
            print("Estou no estado 5")
            self.estado = 1

        if(self.estado == 6):
            self.modoEmergencia()

        if(self.estado ==7):
            self.modoNoturno()


        
print(Cruzamento.semaforoPrincipal)

