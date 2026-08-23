LED Blink With ESP32 and MicroPython

This project demonstrates a basic LED blinking operation using an ESP32 development board and MicroPython. The LED connected to GPIO 2 turns ON for one second and OFF for one second continuously.

---

Objective

Objective| Description
GPIO Control| Configure GPIO 2 as a digital output
LED Control| Turn the LED ON and OFF using MicroPython
Timing| Use the "time" module to create 1-second delays
Programming| Learn the basic structure of an ESP32 MicroPython program

---

Components Required

Component| Quantity| Purpose
ESP32 Development Board| 1| Main microcontroller
LED| 1| Output indicator
220Ω–330Ω Resistor| 1| Limits current through the LED
Breadboard| 1| Circuit assembly
Jumper Wires| 2–3| Electrical connections
USB Cable| 1| Power and programming

«Note: If your ESP32 board has an onboard LED connected to GPIO 2, an external LED is not required.»

---

Circuit Connections

Component| Pin| ESP32 Connection
LED| Anode (+)| GPIO 2 through 220Ω–330Ω resistor
LED| Cathode (−)| GND

Connection Flow

ESP32 GPIO 2
     │
     │
  220Ω–330Ω
   Resistor
     │
     │
 LED Anode (+)
 LED Cathode (−)
     │
     │
    GND

---

Software Requirements

Software / Tool| Purpose
Thonny IDE| Writing, uploading and running MicroPython programs
MicroPython| Programming environment running on the ESP32
USB Cable| Communication between ESP32 and computer

«Note: MicroPython firmware only needs to be installed on the ESP32 during the initial setup. If MicroPython is already installed, the program can be directly uploaded and executed using Thonny.»

---

Modules Used

Module| Purpose
"machine.Pin"| Configures and controls the ESP32 GPIO pin
"time"| Provides the delay function used in the program

No external libraries are required for this project.

---

GPIO Configuration

GPIO Pin| Configuration| Function
GPIO 2| "Pin.OUT"| Controls the LED

---

 Working Principle

1. The "Pin" class is imported from the "machine" module.
2. GPIO 2 is configured as an output pin.
3. The LED is turned ON using "led.on()".
4. The program waits for 1 second.
5. The LED is turned OFF using "led.off()".
6. The program waits for another 1 second.
7. The process repeats continuously using the "while True" loop.

---

LED Operation

Step| LED State| Duration
1| ON| 1 second
2| OFF| 1 second
3| ON| 1 second
4| OFF| 1 second
5| Repeats continuously| —

---

Program Code

from machine import Pin
import time

led = Pin(2, Pin.OUT)

while True:
    led.on()
    time.sleep(1)

    led.off()
    time.sleep(1)

---

Procedure

Step| Procedure
1| Connect the ESP32 to the computer using a USB cable.
2| Open Thonny IDE.
3| Select the MicroPython interpreter for ESP32.
4| Connect Thonny to the ESP32.
5| Enter or open the MicroPython program.
6| Run the program using Thonny.
7| Observe the LED connected to GPIO 2.

---

Expected Output

Parameter| Expected Result
LED ON Time| 1 second
LED OFF Time| 1 second
Operation| Continuous blinking
Controlled Pin| GPIO 2

The LED continuously follows the sequence:

ON → 1 second → OFF → 1 second → ON → OFF → ...

---