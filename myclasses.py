from Sensors import *
from machine import Pin, ADC
import machine, neopixel
import time


class LDRSensor(AnalogSensor):

    def __init__(self, pin, lowactive=True, threshold = 30000):
        super().__init__(pin, lowactive)

    def lightTrip(self):
        return self.tripped()
        print(self.rawValue())

class PartyLight:
    def __init__(self, npin = 5, npix = 300): #pin and number of LEDs
        self._pin = npin
        self._pix = npix
        self._np = neopixel.NeoPixel(machine.Pin(npin), npix)
        
        

    def disco(self): #this works, but it needs to complete an entire cycle before returning to work mode
                     # add other modes later
        for i in range(self._pix):
            for j in range(self._pix):
                self._np[j] = (0, 0, 0)
            self._np[i % self._pix] = (0, 102, 70) #you should add these as methods to function instead of hardcode
            self._np.write()
            time.sleep_ms(1)

            
    def off(self): #sends clear to all pixels to reset
        for i in range(self._pix):
            self._np[i] = (0, 0, 0)
            self._np.write()

class ServoLight:
    def __init__(self, mpin):
        self._pin = mpin
        self._pinNo = machine.Pin(self._pin)
        self._servo = machine.PWM(self._pinNo,freq=50) 
        
    def on(self):
        self._servo.duty(160) # pushes lightsiwch up to ON position
        
    def off(self):
        self._servo.duty(0) # turns lightswich down to OFF position
        
        
        
        
