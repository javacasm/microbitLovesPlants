from microbit import *

imageUp = Image("00900:"
             "09990:"
             "90909:"
             "00900:"
             "00900")

imageDown = Image("00900:"
             "00900:"
             "90909:"
             "09990:"
             "00900")

p16 = Pin(0, Pin.OUT)

while True:
    if button_a.is_pressed():
        display.show(imageUp)
        pin16.write_digital(True) 
    if button_b.is_pressed():
        display.show(imageDown)
        pin16.write_digital(False) 