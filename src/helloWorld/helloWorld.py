from machine import Pin
from picographics import PicoGraphics, DISPLAY_TUFTY_2040
from time import sleep

# turn LED on and off

led = Pin(25, Pin.OUT)
led.value(1)
sleep(1)
led.value(0)

# Console Input and Output
name = input("you name: ")
print ("Hello "+name)

# write Text on Display
display = PicoGraphics(display=DISPLAY_TUFTY_2040)

WHITE = display.create_pen(255, 255, 255)

display.set_pen(WHITE)
display.text("Hello JavaLand!", 0, 0, 320, 4)
display.update()


