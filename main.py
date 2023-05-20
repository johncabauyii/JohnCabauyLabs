from LightSignal import *
from WalkSignal import *
from CrossButton import *
from CarDetect import *
from time import sleep


#push crosswalk button to initialize system

carW = False
pedestrianW = True

def pedestrianCross():
    global carW
    global pedestrianW
    l.goRed()
    w.walk()
    carW = True
    pedestrianW = False

def carGo():
    global carW
    global pedestrianW
    w.warning()
    l.goGreen()
    w.dont()
    carW = False
    pedestrianW = True






if __name__ == "__main__":

    c = CrossButton()
    l = LightSignal()
    w = WalkSignal()
    h = CarDetect()


    while True:
        sleep(0.2)
        


        if c.requestState() and pedestrianW:
            print("request to cross")
            pedestrianCross()
            sleep(5)
        else:
            pass
        
        if h.carHall() and carW:
            carGo()
            sleep(5)
        else:
            pass

#this works, except once the hall detector is tripped, it stays true
# how do I use the sensors class???



  
    
            


