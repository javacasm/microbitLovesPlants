## Test de los relés

Vamos a hacer una primera prueba de control de la bomba con el relé, conectado todo a la micro:bit con la GPIO Board, todo los componentes de [micro:bit watering kit](https://www.digitspace.com/products/micro-bit/kit/microbit-kit-automatic-watering-pump-soil-humidity-detection-with-main-board?5bf8797b7ae48ca3) de [digitspace](https://www.digitspace.com?5bf8797b7ae48ca3)

![](https://www.digitspace.com/image/cache/catalog/products/Microbit%20Kit%20Automatic%20Watering%20Pump%20Soil%20Humidity%20Detection%20with%20No%20Board-1-1000x1000.jpg?5bf8797b7ae48ca3)

TODO: fotos de los componentes por separado

Usamos el módulo con 2 relés (aunque sólo usaremos 1)
![Modulo rele](./images/ModuloRele.jpg) 
para encender/apagar la bomba de agua.

Configuramos el módulo, conectado el jumper de manera que el estado activo encida el relé

![Montaje Rele](./images/TestRele.jpg)
![Montaje Rele](./images/TestRele2.jpg)

Conectamos el pin S2 de control del relé al pin 16 de la micro:bit

Un programa muy sencillo nos permite encender apagar el relé con los botones A y B de la micro:bit

Usando bloques:

![Test rele con bloques](./images/TestRelé.png)

Para la alimentación usamos una [Battery box](https://www.digitspace.com/raspberry-pi-pwm-shield-18650?5bf8797b7ae48ca3) que alimenta tanto la micro:bit como el relé. 

[![Vídeo: micro:bit controla un relé que enciende apaga una bomba de agua](https://img.youtube.com/vi/tDOVUjIaInU/0.jpg)](https://youtu.be/tDOVUjIaInU)

MEJORA: Si está mucho tiempo funcionando a veces se apaga, en 
v2 vamos a alimentar directnmente la bomba desde la batería sin pasar por el regular de la GPIO board.


