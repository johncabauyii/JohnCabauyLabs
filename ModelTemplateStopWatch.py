"""
A basic template file for using the Model class in PicoLibrary
This will allow you to implement simple Statemodels with some basic
event-based transitions.

Currently supports only 4 buttons (hardcoded to BTN1 through BTN4)
and a TIMEOUT event for internal tranisitions.

For processing your own events such as sensors, you can implement
those in your run method for transitions based on sensor events.
"""

# Import whatever Library classes you need - Model is obviously needed
import time
import random
from Model import *
from Button import *
from Counters import *
from Displays import *
from Model import *
from myclasses import *

"""
This is the template Model Runner - you should rename this class to something
that is supported by your class diagram. This should associate with your other
classes, and any PicoLibrary classes. If you are using Buttons, you will implement
buttonPressed and buttonReleased.

To implement the model, you will need to implement 3 methods to support entry actions,
exit actions, and state actions.

This template currently implements a very simple state model that uses a button to
transition from state 0 to state 1 then a 5 second timer to go back to state 0.
"""

class StopWatch:
    
    def __init__(self):
        self.startbutton = Button(14, "startButton", buttonhandler=self)
        self.stopbutton = Button(2, "stopButton", buttonhandler=self)
        self.display = OLEDDisplay(sda=4, scl=5, i2cid=0, width=128, height=64)
        self.t1 = TimeKeeper()
        self.t2 = TimeKeeper()
        self.lapNumber = 0
        
        self._model = Model(4, self, debug=True)
        
        
        self._model.addTransition(0, BTN1_PRESS, 1)
        self._model.addTransition(1, BTN1_PRESS, 3)
        self._model.addTransition(2, BTN1_PRESS, 1)
        self._model.addTransition(3, BTN1_PRESS, 3)
        
        self._model.addTransition(1, BTN2_PRESS, 2)
        self._model.addTransition(2, BTN2_PRESS, 0)
        self._model.addTransition(3, BTN2_PRESS, 2)

        

    """
    Create a run() method - you can call it anything you want really, but
    this is what you will need to call from main.py or someplace to start
    the state model.
    """

    def run(self):
        # The run method should first start the model
        self._model.start()

        # Then it should do a continous loop while the model runs
        while self._model._running:
            # Inside, you can use if statements do handle various do/actions
            # that you need to perform for each state
            # Do not perform entry and exit actions here - those are separate
            
            # You can see which state the model is in (yeah i know)
            curstate = self._model._curState
            
            # Now if you want to do different things for each state you can do it:
            if curstate == 1:
                self.display.reset()
                self.display.showText(str(self.t1),0,0)
                self.display.showText(str(self.t2),0, 20)
                self.display.showText("Lap: " + str(self.lapNumber) , 0, 40)
                
                
            elif curstate == 3:
                self.display.reset()
                self.display.showText(str(self.t1),0,0)
                self.display.showText(str(self.t2),0, 20)
                self.display.showText("Lap: " + str(self.lapNumber) , 0, 40)
                
                
                # State1 do/actions
                # You can check your sensors here and perform transitions manually if needed
                # For example, if you want to go from state 1 to state 2 when the motion sensor
                # is tripped you can do something like this
                # if self.motionsensor.tripped():
                # gotoState(2)
                pass
            
            #etc.

            # If you are using a software timer, you will need to do a poll to
            # see if the timer has timed out. Hardware timer does not need polling
            # Note that Wokwi does not do well with Hardware timers

            
            # I suggest putting in a short wait so you are not overloading the poor Pico
            time.sleep(0.1)


    """
    stateEntered - is the handler for performing entry/actions
    You get the state number of the state that just entered
    Make sure actions here are quick
    """
    def stateEntered(self, state):
        # Again if statements to do whatever entry/actions you need
        if state == 0: #timeZero state
            self.display.reset()
            self.t1.reset()
            self.t2.reset()
            self.resetLap()
            self.display.showText(str(self.t1),0,0)
            self.display.showText(str(self.t2),0,20)
            self.display.showText("Lap: " + str(self.lapNumber) , 0, 40)
            print('State 0 entered')
            pass
        
        elif state == 1: #running state
            self.display.reset()
            self.t1.start()
            self.t2.start()
            print('State 1 entered')
        elif state == 2: #pause state
            self.t1.stop()
            self.t2.stop()
            print('State 2 entered')
        elif state == 3: #lap state
            self.t2.reset()
            self.addLap()
            print('State 3 entered')
            
    """
    stateLeft - is the handler for performing exit/actions
    You get the state number of the state that just entered
    Make sure actions here are quick
    
    This is just like stateEntered, perform only exit/actions here
    """

    def stateLeft(self, state):
        pass

    
    """
    If you are using buttons, you create the button handlers here.
    Associate up to 4 buttons with BTN1_PRESS through BTN4_PRESS
    """
    def buttonPressed(self, name):
        # For example, lets say the start button is BTN1 and stop button is BTN2
        if name == "startButton":
            self._model.processEvent(BTN1_PRESS)
        # if you have multiple buttons, feel free to add them. Up to 4 buttons
        # are supported by the model right now.
        elif name == "stopButton":
            self._model.processEvent(BTN2_PRESS)

    """
    Same thing with Button release, if you want to handle release events
    As well as press or just want to do release events only.
    """
    def buttonReleased(self, name):
        pass


    """
    If you are using a timer, handle the timeout callback
    My model can use timeout events for transitions, so simply
    send the event to the model and it will take care of
    the rest.
    """
    def timeout(self):
        self._model.processEvent(TIMEOUT)
        
            
        
    def addLap(self):
        self.lapNumber = self.lapNumber+1
    
    def resetLap(self):
        self.lapNumber = 0
        

# Test your model. Note that this only runs the template class above
# If you are using a separate main.py or other control script,
# you will run your model from there.
if __name__ == '__main__':
    StopWatch().run()