from Sensors import *
from time import sleep


#LDR will be replaced with Hall Effect sensor in actual implementation

class CarDetect:

    def __init__(self):
        #constructor
        self.detectCar = DigitalSensor(14, lowactive = True)
        
    def carHall(self):
        if self.detectCar.tripped():
            return True
        return False
