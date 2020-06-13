"""
Control del nivel de agua de un depósito con sensor de nivel de agua
Podemos controlar el encendido de un motor de bombeo (por medio de un relé)
Usando los botones A y B
Si el nivel es bajo el motor se apaga automáticamente

CC by SA by @javacasm
Junio 2020

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

imageFull = Image("99999:"
                  "99999:"
                  "99999:"
                  "99999:"
                  "99999")

imageHalf = Image("90009:"
                  "90009:"
                  "99999:"
                  "99999:"
                  "99999")

imageEmpty = Image("90009:"
                   "90009:"
                   "90009:"
                   "90009:"
                   "99999")

alarmaNivelAgua = 400

def EnciendeRiego():
    if nivelDeposito > alarmaNivelAgua:
        display.show(imageUp)
        pin16.write_digital(True)

def ApagaRiego():
    display.show(imageDown)
    pin16.write_digital(False)

def MostrarNivelAgua():
    if nivelDeposito < alarmaNivelAgua:
        display.show(imageEmpty)
    elif nivelDeposito < 1.5 * alarmaNivelAgua:
        display.show(imageHalf)
    else:
        display.show(imageFull)


while True:
    nivelDeposito = pin2.read_analog()
    MostrarNivelAgua()
    if button_a.is_pressed():
        EnciendeRiego()
    if button_b.is_pressed():
        ApagaRiego()


