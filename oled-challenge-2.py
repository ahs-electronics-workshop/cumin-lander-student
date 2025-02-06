import time
import board
import busio
from adafruit_ssd1306 import SSD1306_I2C

# Create I2C interface
i2c = busio.I2C(scl=board.SCL, sda=board.SDA)

# Define OLED display dimensions (128x32)
WIDTH = 128
HEIGHT = 32

# Create SSD1306 OLED instance
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Clear the display
oled.fill(0)
oled.show()

# Function to display the current time
def display_time():
    current_time = ...  # Get the current local time
    
    # Extract hours, minutes, and seconds
    hours = ...
    minutes = ...
    seconds = ...
    
    # Format the time string manually
    time_string = "{:02}:{:02}:{:02}".format(hours, minutes, seconds)
    
    # Clear the screen
    oled.fill(...)
    
    # Display the time on the OLED
    oled.text(...)  # Position (x=20, y=12) on the screen
    oled.show()

# Loop to update the time every second
while True:
    display_time()
    time.sleep(1)  # Update every second


