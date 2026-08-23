from machine import Pin, time_pulse_us
import time

trig = Pin(13, Pin.OUT)
echo = Pin(12, Pin.IN)

while True:

    trig.value(0)
    time.sleep_us(2)

    trig.value(1)
    time.sleep_us(10)

    trig.value(0)

    duration = time_pulse_us(echo, 1)

    distance = duration * 0.0343 / 2

    print("Distance:", distance, "cm")

    time.sleep(1)