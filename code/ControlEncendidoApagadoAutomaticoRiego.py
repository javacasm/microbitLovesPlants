"""
Encendemos/apagamos el riego (bomba controlada por un relé) automáticamente
según el valor de un sensor de humedad de suelo:
* Por debajo de un valor de humedad se enciende el motor
* Por encima se apaga
* Se usa un sensor de lluvia para detectar si la planta ya está expulsando
    agua por abajo
Controlamos el nivel de agua de un depósito con sensor de nivel de agua
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

# Valores umbral para activaciones
alarmaNivelAgua = 400
humedadParaRiego = 500
sensorLluviaMojado = 800

humedadSuelo = 0
valorSensorLluvia = 0
nivelDeposito = 0


def EnciendeRiego():
    global nivelDeposito
    if nivelDeposito > alarmaNivelAgua:
        display.show(imageUp)
        pin16.write_digital(True)

def ApagaRiego():
    display.show(imageDown)
    pin16.write_digital(False)

def EstaEncendidoRiego():
    return pin16.value()

def MostrarNivelAgua():
    global nivelDeposito
    if nivelDeposito < alarmaNivelAgua:
        if EstaEncendidoRiego() :
            ApagaRiego()
        display.show(imageEmpty)
    elif nivelDeposito < 1.5 * alarmaNivelAgua:
        display.show(imageHalf)
    else:
        display.show(imageFull)

def MedirSensores():
    nivelDeposito = pin2.read_analog()
    uart.write('NivelDeposito=' + str(nivelDeposito) + '\n')
    valorSensorLluvia = pin1.read_analog()
    uart.write('valorSensorLluvia=' + str(valorSensorLluvia) + '\n')
    # El sensor de humedad es inversamente proporcional a la humedad
    humedadSuelo = 1023 - pin0.read_analog()
    uart.write('humedadSuelo=' + str(humedadSuelo) + '\n')


def RevisarHumedadSuelo():
    global humedadSuelo, valorSensorLluvia
    if humedadSuelo < humedadParaRiego:
        EnciendeRiego()
        # Mantenemos encendido el riego mientras se cumplan estas condiciones
        while humedadSuelo < humedadParaRiego and valorSensorLluvia > sensorLluviaMojado:
            MedirSensores()
        ApagaRiego()

def miMain():
    # uart.init()
    while True:
        MedirSensores()
        MostrarNivelAgua()
        RevisarHumedadSuelo()
        if button_a.is_pressed():
            EnciendeRiego()
        if button_b.is_pressed():
            ApagaRiego()
