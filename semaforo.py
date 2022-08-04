from time import sleep
from gpiozero import LED


class Semaforo():

    def __init__(self, SEMAFORO_VERMELHO, SEMAFORO_AMARELO,
                 SEMAFORO_VERDE):

        self.SEMAFORO_VERMELHO = LED(SEMAFORO_VERMELHO)
        self.SEMAFORO_AMARELO = LED(SEMAFORO_AMARELO)
        self.SEMAFORO_VERDE = LED(SEMAFORO_VERDE)

        self.ativado = False

    def inicia(self):
        self.SEMAFORO_VERMELHO.off()
        self.SEMAFORO_AMARELO.off()
        self.SEMAFORO_VERDE.off()
        print("Semaforos Desligados!!!")

    def modoEmergencia(self, ativado):
        self.ativado = ativado
        print("Modo Emergencia Ativado.")
        while self.ativado == True:
            self.SEMAFORO_VERMELHO.off()
            self.SEMAFORO_AMARELO.off()
            self.SEMAFORO_VERDE.on()

    def modoNoturno(self):
        print("Modo Noturno Ativado")
        while True:
            self.SEMAFORO_VERMELHO.off()
            self.SEMAFORO_AMARELO.blink()
            self.SEMAFORO_VERDE.off()

    def modoPare(self):
        self.SEMAFORO_VERMELHO.on()
        self.SEMAFORO_AMARELO.off()
        self.SEMAFORO_VERDE.off()

    def modoAtencao(self, ativado):
        self.ativado = False
        while ativado == True:
            self.SEMAFORO_VERMELHO.off()
            self.SEMAFORO_AMARELO.blink()
            self.SEMAFORO_VERDE.off()
            sleep(1)
            print("Modo Atenção Ativado!")

    def modoSiga(self):
        self.SEMAFORO_VERMELHO.off()
        self.SEMAFORO_AMARELO.off()
        self.SEMAFORO_VERDE.on()

print('Digite algo para ativar o modo de atenção:  ')
