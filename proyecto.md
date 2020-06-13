# Sistema de riego

Vamos a desarrollar con sistema de riego inteligente, que riegue las plantas cuando estén secas. Encenderemos la bomba de riego cuando el sensor de humedad que está en la macenta de nuestra planta dé una medida por debajo de un valor dado.

Usaremos la placa [micro:bit](https://www.digitspace.com/products/micro-bit/official-boards-1/microbit-go-nrf51822-development-board-python-starter?5bf8797b7ae48ca3) como controlador del sistema, programando los prototipos con [bloques](https://makecode.microbit.org/) y con [micropython](https://python.microbit.org/v/2.0)

Iremos desarrollando el proyecto en diferentes fases.

[Digitspace](https://www.digitspace.com?5bf8797b7ae48ca3) ha patrocinado todos los materiales del proyecto

## V0: Controlando una bomba de agua con un relé y micro:bit

Vamos a hacer una primera prueba de control de la bomba con el relé, conectado todo a la micro:bit con la GPIO Board, todo los componentes de [micro:bit watering kit](https://www.digitspace.com/products/micro-bit/kit/microbit-kit-automatic-watering-pump-soil-humidity-detection-with-main-board?5bf8797b7ae48ca3) de [digitspace](https://www.digitspace.com?5bf8797b7ae48ca3) y activaremos el riego con los botones de la micro:bit

![](https://www.digitspace.com/image/cache/catalog/products/Microbit%20Kit%20Automatic%20Watering%20Pump%20Soil%20Humidity%20Detection%20with%20No%20Board-1-1000x1000.jpg?5bf8797b7ae48ca3)

El montaje lo realizamos en una placa de prototipo a la que hemos conectado la GPIO Board

![](./images/Micro-bit-GPIO-Expansion-Board.png)

Usamos el módulo con 2 relés (aunque sólo usaremos 1) para encender/apagar la bomba de agua.
![Modulo rele](./images/ModuloReleTop.png) 



![Bomba de agua](./images/WaterPump.png)


Para la alimentación usamos una [Battery box](https://www.digitspace.com/raspberry-pi-pwm-shield-18650?5bf8797b7ae48ca3) que alimenta tanto la micro:bit como el relé. 

![Battery box](https://www.digitspace.com/image/cache/catalog/products/Raspberry%20Pi%20PWM%20Shield%2018650-1000x1000.jpg?5bf8797b7ae48ca3)

Configuramos el módulo, conectado el jumper de manera que el estado activo encida el relé

Conectamos el pin S2 de control del relé al pin 16 de la micro:bit

![Montaje Rele](./images/TestRele.jpg)
![Montaje Rele](./images/TestRele2.jpg)

Un programa muy sencillo nos permite encender apagar el relé con los botones A y B de la micro:bit

![Test rele con bloques](./images/TestRelé.png)

[Usando bloques](https://makecode.microbit.org/_iJDE3iHi2eDL):

Si usamos micropython

```python

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

```


En este [vídeo](https://youtu.be/tDOVUjIaInU) vemos como activamos y desactivamos el relé con los pulsadores de la micro:bit

[![Vídeo: micro:bit controla un relé que enciende apaga una bomba de agua](https://img.youtube.com/vi/tDOVUjIaInU/0.jpg)](https://youtu.be/tDOVUjIaInU)

MEJORA: Si está mucho tiempo funcionando a veces se apaga, puesto que estamos alimentando todo (micro:bit, relés y motores) a través del regulador de alimentación la placa GPIO.

Para evitarlo vamos a alimentar directnmente la bomba desde la batería sin pasar por el regular de la GPIO board.

![Montaje Rele](./images/TestRele3.jpg)

Usaremos los raíles de arriba en la imagen para todos lo que va alimentado desde la placa GPIO. Los raíles de abajo para la conexión directa a los 5V de la batería.



## Control del nivel de agua del depósito

Usamos un sensor de nivel de agua para detectar cuando nuestro depósito no tiene agua y así apagar el motor cuando no haya suficiente agua.

![](./images/SensorNivelAguaDeposito.jpg)


Hemos creado varias funciones, para controlar el riego y para visualizar el nivel de agua en el depósito: **EnciendeRiego**, **ApagaRiego**, **EstáEncendidoRiego** y **MostrarNivelAgua**

TODO: vídeo explicando el programa

![](./images/BloquesControlNivelAgua.png)

![](./images/MontajeSensorNivelAgua.jpg)

[Proyecto: Control de nivel de agua del depósito](https://makecode.microbit.org/_a8vYyX6zTWH2)


TODO: programa micropython


```python
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

```

[Vídeo del sistema en funcionamiento](https://photos.app.goo.gl/g6w9jHdvzEWb46SQ6)

## Encendido y apagado automático

Ahora vamos a utilizar un sensor de humedad de suelo para activar el riego cuando la tierra tenga una humedad por debajo de un cierto umbral. 

TODO: imagen sensor de humedad de suelo
El sensor de humedad de suelo da un valor de 1023 en el aire y un valor de 500 cuando el suelo está humedo

Para detener el riego colocaremos un sensor de lluvia debajo de nuestra maceta: cuando salga agua de ella consideraremos que ya se ha regado suficiente y detendremos el riego

TODO: imagen de sensor de lluvia

El sensor de lluvia da un valor de 1023 en el aire y baja de 800 cuando lo mojamos

![](./images/MontajeCompleto.jpg)

### Programación

Cuando se detecta que la humedad del suelo es más baja del umbral establecido de enciende el riego hasta que se detecta que el agua sale de la maceta, momento en el que cortamos el riego.


![](./images/BloquesEncendidoApagadoAutmaticoRiego.png)

[Proyecto de bloques](https://makecode.microbit.org/_cYceVT8Tb9bV)

![qr](data:image/gif;base64,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)

## Pinout

Relé riego: P16
Sensor humedad: P0
Sensor Agua: P1
Sensor nivel agua: P2

![](./images/pinoutMicrobit.png)