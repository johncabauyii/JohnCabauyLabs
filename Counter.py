from Button import *
from Displays import *
import time

from Displays import *
import ssd1306
from machine import Pin, SoftI2C

'''this is a counter class 
to implement a basic increment-reset counter and 
show count on display'''

class Counter:

# constructor
    def __init__(self):
        print("counter: constructor")
        self._number = 0
        self._display = OLEDDisplay(sda=4, scl=5, i2cid=0, width=128, height=64)
        self._greenButton = Button(0, "increase", buttonhandler =self , lowActive=True)
        self._greenButton = Button(2, "reset", buttonhandler =self , lowActive=True)
    def increment(self):
        print("incrementing")
        self._number = self._number + 1
    
    def reset(self):
        print("resetting")
        self._number = 0

    def buttonPressed(self, name):
        if name == "increase":
            self.increment()
        elif name == "reset":
            self.reset()
    def buttonReleased(self, name):
        pass
    
    def show(self):
        while True:
            self._display.showNumber(self._number)
            time.sleep(0.05)
            self._display.reset()
    
   
            
            

