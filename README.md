# micro:bit Loves your Plants

## micro:bit loves your plants and will take care of them

Take care (in the STEAM way) of  plants/small garden using micro:bit 

![V0: manually operated](./images/V0.jpg)

# Sistema de riego

Vamos a desarrollar con sistema de riego inteligente, que riegue las plantas cuando estén secas. Encenderemos la bomba de riego cuando el sensor de humedad que está en la macenta de nuestra planta dé una medida por debajo de un valor dado.

Usaremos la placa [micro:bit](https://www.digitspace.com/products/micro-bit/official-boards-1/microbit-go-nrf51822-development-board-python-starter?5bf8797b7ae48ca3) como controlador del sistema, programando los prototipos con [bloques](https://makecode.microbit.org/) y con [micropython](https://python.microbit.org/v/2.0)

Iremos desarrollando el proyecto en diferentes fases.

[Digitspace](https://www.digitspace.com?5bf8797b7ae48ca3) ha patrocinado todos los materiales del proyecto

![DigiSpace](https://www.digitspace.com/image/cache/catalog/first%20page/logo-1x-180x40.png?5bf8797b7ae48ca3)

[V0: manually operated wattering system](./proyecto.md)

### Entry level
* Using [micro:bit watering kit](https://www.digitspace.com/products/micro-bit/kit/microbit-kit-automatic-watering-pump-soil-humidity-detection-with-main-board?5bf8797b7ae48ca3)
* [Some temperature sensors (DHT22 or GY-21-HTU21)](https://www.digitspace.com/sensor-kit-with-45-sensors?5bf8797b7ae48ca3)
* [Light sensors (LDR)](https://www.digitspace.com/sensor-kit-with-45-sensors?5bf8797b7ae48ca3) 
* [Uv sensor](https://www.digitspace.com/ml8511-uv-light-detection-sensor-module-for-arduino?5bf8797b7ae48ca3) [Tutorial: ml8511 with micro:bit](http://www.microbitlearning.com/code/arduino/microbit-ml8511-sensor-example.php)
* I would add a [visual rgb indicator](https://www.digitspace.com/products/micro-bit/breakout/bbc-microbit-expansion-board-full-color-led-module-rgb-usb-charging-battery?5bf8797b7ae48ca3). [Tutorials](https://www.yahboom.net/study/LED_Circular) [Details](./RGBRing.md)
* [Battery box](https://www.digitspace.com/raspberry-pi-pwm-shield-18650?5bf8797b7ae48ca3)
* I want to use micropython.
I think this could be a really cool project.

### Pro level
* Using ESP32 instead of the micro:bit, 
* Adding an [ESP-CAM](https://www.digitspace.com/wifi-ble-module-esp32-serial-wifi-camera-esp32-cam?search=esp32&description=true&page=4?5bf8797b7ae48ca3) and 
* publishing data via wifi.  
* I want to use micropython for the two versions.

