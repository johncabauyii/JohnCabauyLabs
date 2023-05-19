from Button import *
from time import sleep


class CrossButton:

    def __init__(self):
        self.walkButton = Button(14, "walkButton", buttonhandler = self , lowActive=True)
        self.state = False
        self.crossTime = 5

    def setStateTrue(self):
        self.state = True

    def setStateFalse(self):
        self.state = False

    def buttonPressed(self, name):
        if name == "walkButton":
            self.setStateTrue()
            sleep(0.2)
    
    def buttonReleased(self, name):
        if name == "walkButton":
            self.setStateFalse()
    
    def requestState(self):
        #use this to return the button's state
        return self.state