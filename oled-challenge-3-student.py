import time
import board
import displayio
from adafruit_displayio_ssd1306 import SSD1306
from i2cdisplaybus import I2CDisplayBus

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

main_screen = displayio.Group()
display.root_group = main_screen


small_font = bitmap_font.load_font("fonts/helvB08.bdf")
medium_font = bitmap_font.load_font("fonts/NotoSans-Medium-strip-10px.bdf")

def display_time():
    now = time.localtime()
    h = ...
    m = ...
    s = ...
    return [h, m, s]

# Labels
# hours
l1 = Label(
            ..., #pick your font - small fon
            anchor_point=(..., ...),
            anchored_position=(...,...),
            text=...,
            color=TEXT_COLOR,
    )

# minutes
l2 = Label(
            ..., #pick your font
            anchor_point=(..., ...),
            anchored_position=(...,...),
            text=...,
            color=TEXT_COLOR,
)

# seconds
l3 = Label(
            ..., #pick your font
            anchor_point=(..., ...),
            anchored_position=(...,...),
            text=...,
            color=TEXT_COLOR,
)

main_screen.append(l1)
main_screen.append(l2)
main_screen.append(l3)

while True:
    l1.text = ...
    l2.text = ...
    l3.text = ...
    time.sleep(1)  # Update every second
