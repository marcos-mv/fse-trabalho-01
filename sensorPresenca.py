from cruzamento import Cruzamento
from gpiozero import Button

class SensorPresenca():
    def __init__(self, SENSOR_PASSAGEM):

        self.SENSOR_PASSAGEM = Button(SENSOR_PASSAGEM, pull_down=True)
        self.SENSOR_PASSAGEM.wait_for_active()
        print('Sensor Presença ativado.')
                
        self.activate = False