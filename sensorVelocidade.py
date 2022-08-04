from cruzamento import Cruzamento
from gpiozero import Button

class SensorVelocidade():
    def __init__(self, SENSOR_VELOCIDADE):

        self.SENSOR_VELOCIDADE_1_A = SENSOR_VELOCIDADE

        self.sensorA1 = Button(SENSOR_VELOCIDADE, pull_up= True)

        self.activate = False