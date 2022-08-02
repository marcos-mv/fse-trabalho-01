from gpiozero import LED, Button
from time import sleep

from cruzamento import Cruzamento
# import portasGPIO

# SEMAFORO_1_VERMELHO = LED(21),
# SEMAFORO_1_AMARELO = LED(26),
# SEMAFORO_1_VERDE = LED(1),

SEMAFORO_1_VERMELHO = 21,
SEMAFORO_1_AMARELO = 26,
SEMAFORO_1_VERDE = 1,

SEMAFORO_2_VERMELHO = 12,
SEMAFORO_2_AMARELO = 16,
SEMAFORO_2_VERDE = 20

BOTAO_PEDESTRE_1 = 8,
BOTAO_PEDESTRE_2 = 7,

SENSOR_PASSAGEM_1 = 14,
SENSOR_PASSAGEM_2 = 15,

SENSOR_VELOCIDADE_1_A = 18,
SENSOR_VELOCIDADE_1_B = 23,

SENSOR_VELOCIDADE_2_A = 24,
SENSOR_VELOCIDADE_2_B = 25

print(Cruzamento.BOTAO_PEDESTRE_1)




    # class Semaforos(cruzamento.Cruzamento):

    #     def __init__(self, cruzamento.Cruzamento):




    #     def inicia(self):
    #         self.SEMAFORO_1_VERMELHO.off()
    #         self.SEMAFORO_1_AMARELO.off()
    #         self.SEMAFORO_1_VERDE.off()

    #     def modoEmergencia(self, active):
    #         self.active = True
    #         print("Modo Emergencial Ativado.")
    #         while self.active == True:
    #             self.SEMAFORO_1_VERMELHO.off()
    #             self.SEMAFORO_1_AMARELO.off()
    #             self.SEMAFORO_1_VERDE.on()

    #     def modoNoturno(self):
    #         while True:
    #             self.SEMAFORO_1_VERMELHO.off()
    #             self.SEMAFORO_1_AMARELO.blink()
    #             self.SEMAFORO_1_VERDE.off()

    #     def modoPare(self):
    #         self.SEMAFORO_1_VERMELHO.on()
    #         self.SEMAFORO_1_AMARELO.off()
    #         self.SEMAFORO_1_VERDE.off()

    #     def modoAtencao(self, active):
    #         self.active = False
    #         while active == True:
    #             SEMAFORO_1_VERMELHO.off()
    #             SEMAFORO_1_AMARELO.blink()
    #             SEMAFORO_1_VERDE.off()
    #             sleep(1)
    #             print("Modo Atenção Ativado!")

    #     def modoLibera(self):
    #         SEMAFORO_1_VERMELHO.off()
    #         SEMAFORO_1_AMARELO.off()
    #         SEMAFORO_1_VERDE.on()


    # semaforo1 = Semaforos(LED(21), LED(26), LED(1), LED(12), LED(16), LED(20), 1)


    # print(semaforo1.numeroCruzamento)
    # # print(semaforo1.SEMAFORO_1_VERDE)
    # # print(semaforo1.SEMAFORO_1_VERMELHO)
    # # print(semaforo1.SEMAFORO_1_AMARELO)

    # # while True:
    # #     Semaforos.SEMAFORO_1_VERMELHO.on()
    # #     Semaforos.SEMAFORO_1_AMARELO.on()
    # #     Semaforos.SEMAFORO_1_VERDE.on()
    # #     print('ligado')
    # #     sleep(1)
    # #     Semaforos.SEMAFORO_1_VERMELHO.off()
    # #     Semaforos.SEMAFORO_1_AMARELO.off()
    # #     Semaforos.SEMAFORO_1_VERDE.off()
    # #     print('desligado')
    # #     sleep(1)

    # # def ligarSemaforo(self):
    # #     while True:
    # #         Semaforos.on()
    # #         led2.on()
    # #         led3.on()
    # #         sleep(1)
    # #         led.off()
    # #         led2.off()
    # #         led3.off()
    # #         sleep(1)


    # # cruzamento = Semaforos(1, 2, 3, 4, 5, 6, 7)

    # # print(cruzamento.numeroCruzamento)


    # class Botoes:
    #     def __init__(self, BOTAO_PEDESTRE_1, BOTAO_PEDESTRE_2, numeroCruzamentoB):

    #         self.BOTAO_PEDESTRE_1 = BOTAO_PEDESTRE_1,
    #         self.BOTAO_PEDESTRE_2 = BOTAO_PEDESTRE_2,

    #         self.numeroCruzamentoB = numeroCruzamentoB


    # class Sensores:
    #     def __init__(self, SENSOR_PASSAGEM_1, SENSOR_VELOCIDADE_1_A,
    #                 SENSOR_VELOCIDADE_1_B, SENSOR_PASSAGEM_2,
    #                 SENSOR_VELOCIDADE_2_A,
    #                 SENSOR_VELOCIDADE_2_B, numeroCruzamentoS):

    #         self.SENSOR_PASSAGEM_1 = SENSOR_PASSAGEM_1,
    #         self.SENSOR_PASSAGEM_2 = SENSOR_PASSAGEM_2,

    #         self.SENSOR_VELOCIDADE_1_A = SENSOR_VELOCIDADE_1_A,
    #         self.SENSOR_VELOCIDADE_1_B = SENSOR_VELOCIDADE_1_B,

    #         self.SENSOR_VELOCIDADE_2_A = SENSOR_VELOCIDADE_2_A,
    #         self.SENSOR_VELOCIDADE_2_B = SENSOR_VELOCIDADE_2_B,
    #         self.numeroCruzamentoS = numeroCruzamentoS
