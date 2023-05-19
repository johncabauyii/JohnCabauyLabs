<<<<<<< Updated upstream
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
        self._greenButton = Button(13, "reset", buttonhandler =self , lowActive=True)
        self._greenButton = Button(2, "hexa", buttonhandler =self , lowActive=True)
        self.mode = True
    def increment(self):
        print("incrementing")
        self._number = self._number + 1
    def reset(self):
        print("resetting")
        self._display.reset()
        self._display.showText("resetting")
        time.sleep(1)
        self._display.reset()
        self._number = 0
    
    def hexa(self):
        self._display.reset()
        self.mode = not self.mode
    

    def buttonPressed(self, name):
        if name == "increase":
            self._display.reset()
            self.increment()
        elif name == "reset":
            self.reset()
        elif name == "hexa":
            self.hexa()
    def buttonReleased(self, name):
        pass
    
    def show(self):
        while True:
            if self.mode == True:
                self._display.showNumber(self._number)
            else:
                self._display.showNumber(hex(self._number))
                
    
   
            
            

=======
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
        self._greenButton = Button(13, "reset", buttonhandler =self , lowActive=True)
        self._greenButton = Button(2, "hexa", buttonhandler =self , lowActive=True)
        self.mode = True
    def increment(self):
        print("incrementing")
        self._number = self._number + 1
    def reset(self):
        print("resetting")
        self._display.reset()
        self._display.showText("resetting")
        time.sleep(1)
        self._display.reset()
        self._number = 0
    
    def hexa(self):
        self._display.reset()
        self.mode = not self.mode
    

    def buttonPressed(self, name):
        if name == "increase":
            self._display.reset()
            self.increment()
        elif name == "reset":
            self.reset()
        elif name == "hexa":
            self.hexa()
    def buttonReleased(self, name):
        pass
    
    def show(self):
        while True:
            if self.mode == True:
                self._display.showNumber(self._number)
            else:
                self._display.showNumber(hex(self._number))
                
    
   
            
            

>>>>>>> Stashed changes
