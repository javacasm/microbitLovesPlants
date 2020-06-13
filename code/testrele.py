"""
Control del encendido/apagado de un relé conectado al pin 16
con lo botones
Se muestra una imagen cuando encendido y otra cuando apagado

CC by SA by @javacasm
Mayo 2020
"""
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

while True:
    if button_a.is_pressed():
        display.show(imageUp)
        pin16.write_digital(True)
    if button_b.is_pressed():
        display.show(imageDown)
        pin16.write_digital(False)
