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
import tm1637
from gpio_lcd import *
from pico_i2c_lcd import I2cLcd
import ssd1306
import max7219

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


class SevenSegmentDisplay(Display):
    """
    Seven Segment Display class - implements a 4-digit seven segment display
    Decimal points not supported - colon can be used when showing two numbers
    """

    def __init__(self, clk=16, dio=17):
        self._tm = tm1637.TM1637(clk=Pin(clk), dio=Pin(dio))

    def reset(self):
        """ clear the display screen  """
        
        self._tm.write([0, 0, 0, 0])

    def showNumber(self, number):
        """ show a single number """
        
        self._tm.number(number)

    def showNumbers(self, num1, num2, colon=True):
        """  Show two numbers optionally separated by a colon by default, the colon is shown """
        
        self._tm.numbers(num1, num2, colon)

    def showText(self, text):
        """
        Show a string - only first 4 characters will be shown
        for anything bigger than 4 characters.
        """
        
        self._tm.show(text)

    def scroll(self, text, speed=250):
        """
        Scroll a longer text - note that this will use a sleep
        call to pause between movements.
        """
        
        self._tm.scroll(text, speed)


class LCDDisplay(Display):
    """
    LCD Display class - currently supports displays with an I2C backpack
    as well as displays directly driven via the d4-d7 pins
    
    Parameters
    --------
    This is important since Python does not have method overloading, we have one init
    to do both parallel as well as i2c displays
    pass rs, e, d4, d5, d6, d7 pin numbers for parallel displays
    
    pass sda, scl, i2cid for i2c displays - default is to use parallel so must pass sda/scl/i2cid
    if using i2c
    
    To connect the display to I2C 0 on GPIO pins 0,1
    usage: LCDDisplay(sda=0, scl=1, i2cid=0)
    
    To connect the display to I2C ID 1 on GPIO pins 2,3
    usage: LCDDisplay(sda=2, scl=3, i2cid=1)
    
    To connect via parallel with rs on pin 5, e on pin 4
    and d4,d5,d6,d7 to pins 3,2,1 and 0:
    usage:  LCDDisplay()  # yeah those are the default so you don't need to send
    usage: LCDDisplay(rs=5, e=4, d4=3, d5=2, d6=1, d7=0) # preferred - you can see how its hooked up
    
    """
    
    def __init__(self, rs=5, e=4, d4=3, d5=2, d6=1, d7=0, *, sda=-1, scl=-1, i2cid=0):
        """
        Combined constructor for the direct-driven displays
        explicitly pass in the sda and scl if you need to use I2C
        """
        
        if sda < 0:
            print("LCDDisplay Constructor")
            self._lcd = GpioLcd(rs_pin=Pin(rs),
                enable_pin=Pin(e),
                d4_pin=Pin(d4),
                d5_pin=Pin(d5),
                d6_pin=Pin(d6),
                d7_pin=Pin(d7),
                num_lines=2, num_columns=16)
        else:
            print("LCDDisplay (I2C) Constructor")
            i2c = I2C(i2cid, sda=Pin(sda), scl=Pin(scl), freq=400000)
            I2C_ADDR = i2c.scan()[0]
            self._lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

    def reset(self):
        """ 
        clear the display screen
        """
        
        print("LCDDisplay: reset")
        self._lcd.clear()

    def showNumber(self, number, row=0, col=0):
        """
        show a single number
        """
        
        print(f"LCDDisplay - showing number {number} at {row},{col}")
        self._lcd.move_to(col, row)
        self._lcd.putstr(f"{number}")

    def showNumbers(self, num1, num2, colon=True, row=0, col=0):
        """
        Show two numbers optionally separated by a colon
        by default, the colon is shown
        """
        
        print(f"LCDDisplay - showing numbers {num1}, {num2} at {row},{col}")
        self._lcd.move_to(col, row)
        colsym = ":" if colon else " "
        self._lcd.putstr(f"{num1}{colsym}{num2}")

    def showText(self, text, row=0, col=0):
        """
        Show a string - only first 4 characters will be shown
        for anything bigger than 4 characters.
        """
        
        print(f"LCDDisplay - showing text {text} at {row},{col}")
        self._lcd.move_to(col, row)
        self._lcd.putstr(text)

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
        
    def showNumber(self, number):
        self._oled.text(str(number), 0, 0, 1)
        self._oled.show()

    def showText(self, text):
        self._oled.text(text, 0, 0, 1)
        self._oled.show()

