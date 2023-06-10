from Sensors import *
from time import sleep


#LDR will be replaced with Hall Effect sensor in actual implementation

class CarDetect:

    def __init__(self):
        #constructor
        self.detectCar = DigitalSensor(13, lowactive = True)
        
    def carHall(self):
        if self.detectCar.tripped():
            return True
        return False

class LDRSensor(AnalogSensor):

    def __init__(self, pin, lowactive=True, threshold = 30000):
        super().__init__(pin, lowactive)

    def lightTrip(self):
        return self.tripped()
        print(self.rawValue())