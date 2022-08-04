from cruzamento import Cruzamento
from gpiozero import Button

class Botoes():
    
    def __init__(self, BOTAO_PEDESTRE_1, BOTAO_PEDESTRE_2):

        self.BOTAO_PEDESTRE_1 = Button(BOTAO_PEDESTRE_1, pull_down=True)
        self.BOTAO_PEDESTRE_2 = Button(BOTAO_PEDESTRE_2, pull_down=True)

        self.pressionado = False
        self.BOTAO_PEDESTRE_1.when_pressed = self.pressionado
        

    def botaoPressionado(self):
        self.botaoPressionado = True
        print("Pedestre quer passar")

    def faixaPedrestreLiberada(self):
        self.pedestreEsperando = False

    def esperando(self):
        return self.pressionado
    