import time
import board
import displayio
from adafruit_displayio_ssd1306 import SSD1306
from i2cdisplaybus import I2CDisplayBus

from adafruit_bme280 import basic as adafruit_bme280
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text.label import Label

WIDTH = 32
HEIGHT = 128
ROTATION = 90
BACKGROUND_COLOR = 0x000000
TEXT_COLOR = 0xFFFFFF

displayio.release_displays()
i2c = board.I2C()
display_bus = I2CDisplayBus(i2c, device_address=0x3C)
display = SSD1306(display_bus, width=WIDTH, height=HEIGHT, rotation=ROTATION)

# Temperature, Humidity, Pressure
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)

main_screen = displayio.Group()
display.root_group = main_screen


# Final OLED Prototype
# The final display needs to include everything:
# - time with AM/PM or 24-hour clock
# - Temperature(F), Humidity (%), Pressure (hPa)
# - Some sort of shapes that help define and clarify distinct parts of the oled
# Use the code from the other challenges to bring all this into one file
