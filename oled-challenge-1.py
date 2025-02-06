import board
import busio
from adafruit_ssd1306 import SSD1306_I2C
import time

# Create I2C interface
i2c = busio.I2C(scl=board.SCL, sda=board.SDA)

# Define display dimensions
WIDTH = 128
HEIGHT = 32

# Create SSD1306 OLED instance
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Clear the display
oled.fill(1)
oled.show()
time.sleep(0.5)
oled.fill(0)
oled.show()

contrast = 0
x_pos = 0
while True:
    #change contrast
    oled.contrast(...)
    
    #write the test using x_pos variable
    oled.text(...)
    oled.show()
    
    # wait a 0.5 second
    time.sleep(0.5)

    # Clear the display
    oled.fill(...)
    oled.show()
    
    # increase the contrast and x_pos by 10
    contrast ...
    x_pos ...
    
    # check if contrast is over 255 and reset
    if ... >= ...:
        contrast = 0
    
    # check if x_pos is over 128
    # fill the screen with white and reset x_pos to 0
    if ... >= ...:
        oled.fill(...)
        oled.show()
        x_pos = ....
 


