Two LED Alternating Blink With ESP32 and MicroPython

This project demonstrates the control of two LEDs using an ESP32 development board and MicroPython. The two LEDs connected to GPIO 4 and GPIO 5 blink alternately, where one LED remains ON while the other remains OFF for one second.

---

Objective

| Objective | Description |
|-----------|-------------|
| GPIO Control | Configure GPIO 4 and GPIO 5 as digital outputs |
| LED Control | Control two LEDs independently using MicroPython |
| Alternating Operation | Make the two LEDs turn ON and OFF alternately |
| Timing Control | Use the `time` module to create 1-second delays |
| ESP32 Programming | Understand multiple GPIO control using MicroPython |
| Continuous Operation | Execute the alternating LED sequence continuously |

---

Components Required

| Component | Quantity |
|-----------|----------|
| ESP32 Development Board | 1 |
| LED | 2 |
| 220Ω–330Ω Resistor | 2 |
| Breadboard | 1 |
| Jumper Wires | 4–6 |
| USB Cable | 1 |

---

Circuit Connections

| Connection | Purpose |
|------------|---------|
| ESP32 GPIO 4 → 220Ω–330Ω Resistor → LED 1 Anode (+) | Controls LED 1 |
| LED 1 Cathode (−) → ESP32 GND | Completes LED 1 circuit |
| ESP32 GPIO 5 → 220Ω–330Ω Resistor → LED 2 Anode (+) | Controls LED 2 |
| LED 2 Cathode (−) → ESP32 GND | Completes LED 2 circuit |

Connection Flow

ESP32 GPIO 4
     |
  220Ω–330Ω
   Resistor
     |
 LED 1 Anode (+)
 LED 1 Cathode (−)
     |
    GND


ESP32 GPIO 5
     |
  220Ω–330Ω
   Resistor
     |
 LED 2 Anode (+)
 LED 2 Cathode (−)
     |
    GND

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
| `machine.Pin` | Configures and controls the ESP32 GPIO pins |
| `time` | Provides the delay function |

No external libraries are required for this project.

---

GPIO Configuration

| GPIO Connection | Configuration | Purpose |
|-----------------|---------------|---------|
| GPIO 4 | `Pin.OUT` | Controls LED 1 |
| GPIO 5 | `Pin.OUT` | Controls LED 2 |
| GND | Ground | Completes both LED circuits |

---

Working Principle

1. The "Pin" class is imported from the "machine" module.
2. GPIO 4 is configured as an output for LED 1.
3. GPIO 5 is configured as an output for LED 2.
4. LED 1 is turned ON while LED 2 is turned OFF.
5. The program waits for 1 second.
6. LED 1 is turned OFF while LED 2 is turned ON.
7. The program waits for another 1 second.
8. The process repeats continuously using the "while True" loop.

---

LED Operation

| LED 1 | LED 2 | Duration | Operation |
|-------|-------|----------|-----------|
| ON | OFF | 1 second | `led1.on()` and `led2.off()` |
| OFF | ON | 1 second | `led1.off()` and `led2.on()` |
| Repeat | Repeat | Continuous | `while True` |

---

Program Code

The complete program code is available in the "Two_LED_Alternating_Blink_With_ESP32_and_MicroPython.py" file.

---

Procedure

1. Connect LED 1 to GPIO 4 through a 220Ω–330Ω resistor.
2. Connect LED 2 to GPIO 5 through a 220Ω–330Ω resistor.
3. Connect the cathode of both LEDs to GND.
4. Connect the ESP32 to the computer using a USB cable.
5. Open Thonny IDE.
6. Select the MicroPython interpreter for ESP32.
7. Connect Thonny to the ESP32.
8. Enter or open the MicroPython program.
9. Run the program using Thonny.
10. Observe the two LEDs blinking alternately.

---

Expected Output

| Parameter | Expected Output |
|-----------|-----------------|
| LED 1 | ON for 1 second, then OFF |
| LED 2 | OFF for 1 second, then ON |
| Sequence | LED 1 → LED 2 → LED 1 → LED 2 |
| Operation | Repeats continuously |

The LEDs continuously follow the sequence:

LED 1 ON  →  1 second  →  LED 1 OFF

LED 2 OFF →  1 second  →  LED 2 ON


LED 1 OFF →  1 second  →  LED 1 ON

LED 2 ON  →  1 second  →  LED 2 OFF

          ↓
       Repeat

---