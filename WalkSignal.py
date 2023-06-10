from Displays import *
from Lights import *
from time import sleep

class WalkSignal:
    #constructor
    def __init__(self):
        self.display = OLEDDisplay(sda=4, scl=5, i2cid=0, width=128, height=64)
        self.walkLight = Light(2, "walklight")
        self.dontLight = Light(16, "dontlight")
    
    def walk(self):
        #set light to walk and display "WALK"
        self.dontLight.off()
        self.walkLight.on()
        self.display.reset()
        self.display.showText("WALK")

    def warning(self, warnTime=10):
        #blink dontLight and display warning of how many seconds before dont walk
        #warnTime arguement allows to set seconds of warning
        while True:
            warnTime = warnTime - 1
            self.display.reset()
            self.display.showNumber(warnTime)
            sleep(0.5)
            if warnTime == 0:
                self.display.reset()
                self.display.showText("WAIT")
                return True
                break
            
    def stopCount(self, stopTime = 10):
        for i in range(stopTime):
            self.display.reset()
            self.display.showNumber(stopTime)
            sleep(1)
            return True
    
    def dont(self):
        #turns on dontLight and displays "WAIT"
        self.walkLight.off()
        self.dontLight.on()
        self.display.reset()
        self.display.showText("WAIT")



