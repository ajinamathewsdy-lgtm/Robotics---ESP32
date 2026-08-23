from machine import Pin
import time

led1 = Pin(4, Pin.OUT)
led2 = Pin(5, Pin.OUT)

while True:

    led1.on()
    led2.off()
    time.sleep(1)

    led1.off()
    led2.on()
    time.sleep(1)