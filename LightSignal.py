from Lights import *
import time

class LightSignal:
    
    #constructor
    def __init__(self):
        print("LightSignal: constructor")
        self.redLight = Light(12, "redlight")
        self.yellowLight = Light(0, "yellowlight")
        self.greenLight = Light(15, "greenlight")

    def goGreen(self):
        #set signal to go
        self.greenLight.on()
        self.yellowLight.off()
        self.redLight.off()
        

    def goRed(self, timeYellow =5):
        #sets signal to yellow and then to red to stop
        #set signal parameter allows to set seconds of yellow light warning
        self.greenLight.off()
        self.yellowLight.on()
        self.redLight.off()
        
        time.sleep(timeYellow)
        self.yellowLight.off()
        self.redLight.on()
        








