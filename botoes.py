from gpiozero import Button

class Botoes():
    
    def __init__(self, BOTAO_PEDESTRE):

        self.BOTAO_PEDESTRE_1 = Button(BOTAO_PEDESTRE, pull_down=True)

        self.pressionado = False
        self.BOTAO_PEDESTRE_1.when_pressed = self.pressionado
        

    def botaoPressionado(self):
        self.botaoPressionado = True
        print("Pedestre quer passar")

    def faixaPedrestreLiberada(self):
        self.pedestreEsperando = False
        print("Pedestre passando")

    def esperando(self):
        return self.pressionado
    