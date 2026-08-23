LED Blink With ESP32 and MicroPython

This project demonstrates a basic LED blinking operation using an ESP32 development board and MicroPython. The LED connected to GPIO 2 turns ON for one second and OFF for one second continuously.

---

Objective

| Objective | Description |
|-----------|-------------|
| GPIO Control | Configure GPIO 2 as a digital output |
| LED Control | Turn the LED ON and OFF using MicroPython |
| Timing Control | Use the `time` module to create 1-second delays |
| ESP32 Programming | Understand basic GPIO programming using MicroPython |
| Continuous Operation | Execute the LED blinking sequence continuously |

---

Components Required

| Component | Quantity |
|-----------|----------|
| ESP32 Development Board | 1 |
| LED | 1 |
| 220Ω–330Ω Resistor | 1 |
| Breadboard | 1 |
| Jumper Wires | 2–3 |
| USB Cable | 1 |

«Note: If your ESP32 board has an onboard LED connected to GPIO 2, an external LED is not required.»

---

Circuit Connections

| Connection | Purpose |
|------------|---------|
| ESP32 GPIO 2 → 220Ω–330Ω Resistor → LED Anode (+) | Controls the LED |
| LED Cathode (−) → ESP32 GND | Completes the circuit |

Connection Flow

ESP32 GPIO 2    → 220Ω–330Ω, Resistor   → LED Anode (+), LED Cathode (−)    → GND

---

Software Requirements

| Software | Purpose |
|----------|---------|
| Thonny IDE | Writing, uploading and running MicroPython programs |
| MicroPython | Programming environment for ESP32 |
| USB Cable | Connects ESP32 to the computer |

«Note: MicroPython firmware only needs to be installed on the ESP32 during the initial setup. If MicroPython is already installed, the program can be directly uploaded and executed using Thonny.»

---

Modules Used

| Module | Purpose |
|--------|---------|
| machine.Pin | Configures and controls the ESP32 GPIO pin |
| time | Provides the delay function |

No external libraries are required for this project.

---

GPIO Configuration

| GPIO Connection | Configuration | Purpose |
|-----------------|---------------|---------|
| GPIO 2 | Pin.OUT | Controls the LED |
| GND | Ground | Completes the LED circuit |


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

| LED State | Duration | Operation |
|-----------|----------|-----------|
| ON | 1 second | led.on() |
| OFF | 1 second | led.off() |
| Repeat | Continuous | while True 

---

Program Code

The complete Program code is available in the "LED_Blink_With_ESP32_and_MicroPython.py" file.

---

Procedure

1. Connect the ESP32 to the computer using a USB cable.
2. Open Thonny IDE.
3. Select the MicroPython interpreter for ESP32.
4. Connect Thonny to the ESP32.
5. Enter or open the MicroPython program.
6. Run the program using Thonny.
7. Observe the LED connected to GPIO 2.

---

Expected Output

| Parameter | Expected Output |
|-----------|-----------------|
| LED ON | LED remains ON for 1 second |
| LED OFF | LED remains OFF for 1 second |
| Sequence | ON → OFF → ON → OFF |
| Operation | Repeats continuously |

The LED continuously follows the sequence:

ON → 1 second → OFF → 1 second → ON → OFF → ...

---