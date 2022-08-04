from cruzamento import Cruzamento
from gpiozero import Button

class SensorVelocidade():
    def __init__(self, SENSOR_VELOCIDADE_1_A,
                SENSOR_VELOCIDADE_1_B,
                SENSOR_VELOCIDADE_2_A, SENSOR_VELOCIDADE_2_B):

        self.SENSOR_VELOCIDADE_1_A = SENSOR_VELOCIDADE_1_A
        self.SENSOR_VELOCIDADE_1_B = SENSOR_VELOCIDADE_1_B

        self.SENSOR_VELOCIDADE_2_A = SENSOR_VELOCIDADE_2_A
        self.SENSOR_VELOCIDADE_2_B = SENSOR_VELOCIDADE_2_B

        self.sensorA1 = Button(SENSOR_VELOCIDADE_1_A)
        self.sensorA2 = Button(SENSOR_VELOCIDADE_2_A)
        self.sensorB1 = Button(SENSOR_VELOCIDADE_1_B)
        self.sensorB2 = Button(SENSOR_VELOCIDADE_2_B)