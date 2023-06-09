from Lights import *
import time
import machine, neopixel



class LightSignal:
    
    
    #added option to use neopixel instead of multiple LEDs
    #use pass value to addr to select which pixel is the traffic light for the instance
    def __init__(self, npin=14, npix=10):
        print("LightSignal: constructor")
        self._pin = npin
        self._pix = npix
        self._np = neopixel.NeoPixel(machine.Pin(npin), npix)
        self.redLight = Light(12, "redlight")
        self.yellowLight = Light(0, "yellowlight")
        self.greenLight = Light(15, "greenlight")

    def goGreen(self, timeYellow =5):
        #set signal to go
        self.greenLight.on()
        self.yellowLight.off()
        self.redLight.off()
        
        self._np[9] = (0, 0, 0)
        self._np[9] = (255, 255, 0) #set NorthBound light yellow
        self._np.write()
        
        time.sleep(timeYellow)
        
        self._np[9] = (0, 0, 0)
        self._np[9] = (255, 0, 0) #set Northbound light red
        self._np[8] = (255,255,255) # set EastBound crosswalk to Walk
        
        
        self._np[0] = (0, 0, 0)
        self._np[0] = (0, 255, 0) #set EastBound light to Green
        self._np[1] = (255,60, 0) #set NorthBound crosswalk to Stop
        self._np.write()
        

    def goRed(self, timeYellow =5):
        #sets signal to yellow and then to red to stop
        #set signal parameter allows to set seconds of yellow light warning
        self.greenLight.off()
        self.yellowLight.on()
        self.redLight.off()
        
        self._np[0] = (0, 0, 0)
        self._np[0] = (255, 255, 0) #set EastBound light to Yellow
        self._np.write()
        
        time.sleep(timeYellow)
        self.yellowLight.off()
        self.redLight.on()
        self._np[0] = (0, 0, 0)
        self._np[0] = (255, 0, 0) # set Eastbound light to Red
        self._np[1] = (255,255,255) # set Northbound crosswalk to Walk
        
        self._np[9] = (0,255,0)  #set Northbound light to Green
        self._np[8] = (255, 60, 0) #set Eastbound crosswalk to stop
        self._np.write()
        








