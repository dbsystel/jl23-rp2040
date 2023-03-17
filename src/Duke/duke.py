from picographics import PicoGraphics, DISPLAY_TUFTY_2040
from pimoroni import Button
import time
import jpegdec
import qrcode

display = PicoGraphics(display=DISPLAY_TUFTY_2040)

# remember to upload the image to RP2040 first!
IMAGE_NAME = "Duke_small.jpg"
j = jpegdec.JPEG(display)

# Open the JPEG file
j.open_file(IMAGE_NAME)
# Decode the JPEG at position
j.decode(20, 0)
display.update()

