"""
# Displays.py
# A collection of various text-based displays
# Currently supports 4-digit seven-segment displays - both with a tm1637 backpack
# and without (using PIO)
# And also LCD 1602 displays - both using an i2c backpack as well as GPIO
# Only supports number and basic text displays - PIO 7 seg only supports number
# Author: Arijit Sengupta
"""

from machine import Pin, I2C, SPI, SoftI2C
import time
import ssd1306

class Display:
    """
    The Display Base class - might not actually be needed
    But here to ensure we do not have a duckTyping problem
    """

    def reset(self):
        print(f"reset NOT IMPLEMENTED in {type(self).__name__}")

    def showNumber(self, number):
        print(f"showNumber NOT IMPLEMENTED! in {type(self).__name__}")

    def showText(self, text):
        print(f"showText NOT IMPLEMENTED! in {type(self).__name__}")

    def scroll(self, text, speed=250):
        print(f"Scroll NOT IMPLEMENTED! in {type(self).__name__}")



class OLEDDisplay(Display):
    """
    OLEDDisplay class - implements an OLED display
    
    Only supports I2C connection for now. Pass in sda, scl, i2cid, width and height
    
    Usage:
    Connect to I2C0 on sda to pin 0 and scl to pin 1:
    
    OLEDDisplay(sda=0, scl=1, i2cid=0, width=128, height=64)
    
    Connect to I2C1 on sda to pin 26, scl to pin 27:
    OLEDDisplay(sda=26, scl=27, i2cid=1, width=128, height=64) # default values
    
    Note that graphics outputs are not supported yet in this library.
    """

    def __init__(self, sda=0, scl=1, i2cid=1, width=128, height=64):
        #self._i2c = I2C(i2cid, sda=Pin(sda), scl=Pin(scl), freq=400000)
        i2c = SoftI2C(scl=Pin(5), sda=Pin(4))
        self._oled = ssd1306.SSD1306_I2C(width, height, i2c)
        #self._oled = SSD1306_I2C(width, height, self._i2c)
        self.reset()

    def reset(self):
        self._oled.fill(0)
        self._oled.show()
        
    def showNumber(self, number, row=0, col=0):
        self._oled.text(str(number), row, col, 1)
        self._oled.show()

    def showText(self, text, row=0, col=0):
        self._oled.text(text, row, col, 1)
        self._oled.show()

