from cruzamento import Cruzamento
from time import sleep


class Semaforo(Cruzamento):

    def __init__(self, SEMAFORO_1_VERMELHO, SEMAFORO_1_AMARELO,
                 SEMAFORO_1_VERDE, SEMAFORO_2_VERMELHO,
                 SEMAFORO_2_AMARELO, SEMAFORO_2_VERDE,
                 ):

        self.SEMAFORO_1_VERMELHO = SEMAFORO_1_VERMELHO
        self.SEMAFORO_1_AMARELO = SEMAFORO_1_AMARELO
        self.SEMAFORO_1_VERDE = SEMAFORO_1_VERDE

        self.SEMAFORO_2_VERMELHO = SEMAFORO_2_VERMELHO
        self.SEMAFORO_2_AMARELO = SEMAFORO_2_AMARELO
        self.SEMAFORO_2_VERDE = SEMAFORO_2_VERDE

        self.active = False

    def inicia(self):
        self.SEMAFORO_1_VERMELHO.off()
        self.SEMAFORO_1_AMARELO.off()
        self.SEMAFORO_1_VERDE.off()

    def modoEmergencia(self, active):
        self.active = active
        print("Modo Emergencial Ativado.")
        while self.active == True:
            self.SEMAFORO_1_VERMELHO.off()
            self.SEMAFORO_1_AMARELO.off()
            self.SEMAFORO_1_VERDE.on()

    def modoNoturno(self):
        while True:
            self.SEMAFORO_1_VERMELHO.off()
            self.SEMAFORO_1_AMARELO.blink()
            self.SEMAFORO_1_VERDE.off()

    def modoPare(self):
        self.SEMAFORO_1_VERMELHO.on()
        self.SEMAFORO_1_AMARELO.off()
        self.SEMAFORO_1_VERDE.off()

    def modoAtencao(self, active):
        self.active = False
        while active == True:
            self.SEMAFORO_1_VERMELHO.off()
            self.SEMAFORO_1_AMARELO.blink()
            self.SEMAFORO_1_VERDE.off()
            sleep(1)
            print("Modo Atenção Ativado!")

    def modoLibera(self):
        SEMAFORO_1_VERMELHO.off()
        SEMAFORO_1_AMARELO.off()
        SEMAFORO_1_VERDE.on()
