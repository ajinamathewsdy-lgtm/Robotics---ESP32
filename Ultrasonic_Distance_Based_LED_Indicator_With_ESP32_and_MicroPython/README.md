Ultrasonic Distance-Based LED Indicator With ESP32 and MicroPython

This project uses an HC-SR04 ultrasonic sensor with an ESP32 to measure the distance of an object and control two LEDs based on the measured distance. If the measured distance is 5 cm or more, LED 1 turns ON and LED 2 turns OFF. If the distance is less than 5 cm, LED 2 turns ON and LED 1 turns OFF.

---

Objective

| Objective | Description |
|-----------|-------------|
| Distance Measurement | Measure the distance of an object using an ultrasonic sensor |
| GPIO Control | Configure GPIO 13 and GPIO 12 for ultrasonic sensor communication |
| LED Control | Control two LEDs using GPIO 2 and GPIO 14 |
| Distance-Based Control | Control the LEDs according to the measured distance |
| Threshold Detection | Use 5 cm as the distance threshold |
| MicroPython Programming | Interface the ultrasonic sensor and LEDs using MicroPython |
| Continuous Monitoring | Continuously measure the distance and update the LED status |

---

Components Required

| Component | Quantity |
|-----------|----------|
| ESP32 Development Board | 1 |
| HC-SR04 Ultrasonic Sensor | 1 |
| LED | 2 |
| 220Ω–330Ω Resistor | 2 |
| Breadboard | 1 |
| Jumper Wires | 8 |
| USB Cable | 1 |

---

Circuit Connections

| Connection | Purpose |
|------------|---------|
| HC-SR04 VCC → ESP32 5V/VIN | Supplies power to the ultrasonic sensor |
| HC-SR04 GND → ESP32 GND | Provides common ground |
| HC-SR04 TRIG → ESP32 GPIO 13 | Sends the ultrasonic trigger pulse |
| HC-SR04 ECHO → ESP32 GPIO 12 | Receives the returning echo signal |
| ESP32 GPIO 2 → 220Ω–330Ω Resistor → LED 1 Anode (+) | Controls LED 1 |
| LED 1 Cathode (−) → ESP32 GND | Completes LED 1 circuit |
| ESP32 GPIO 14 → 220Ω–330Ω Resistor → LED 2 Anode (+) | Controls LED 2 |
| LED 2 Cathode (−) → ESP32 GND | Completes LED 2 circuit |

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
| machine.Pin | Configures and controls the ESP32 GPIO pins |
| machine.time_pulse_us | Measures the duration of the ultrasonic echo pulse |
| time | Provides microsecond and second delay functions |

No external libraries are required for this project.

---

GPIO Configuration

| GPIO Connection | Configuration | Purpose |
|-----------------|---------------|---------|
| GPIO 13 | Pin.OUT | Sends the trigger pulse to the ultrasonic sensor |
| GPIO 12 | Pin.IN | Receives the echo signal from the ultrasonic sensor |
| GPIO 2 | Pin.OUT | Controls LED 1 |
| GPIO 14 | Pin.OUT | Controls LED 2 |
| GND | Ground | Provides common ground |

---

Working Principle

1. GPIO 13 is configured as the trigger output of the ultrasonic sensor.
2. GPIO 12 is configured as the echo input.
3. A 10-microsecond trigger pulse is sent to the ultrasonic sensor.
4. The ESP32 measures the returning echo pulse using time_pulse_us().
5. The echo duration is converted into distance in centimeters.
6. The measured distance is displayed in the Thonny Shell.
7. The program checks whether the measured distance is 5 cm or greater.
8. If the distance is 5 cm or greater, LED 1 turns ON and LED 2 turns OFF.
9. If the distance is less than 5 cm, LED 2 turns ON and LED 1 turns OFF.
10. The process repeats continuously.

---

Ultrasonic Sensor Operation

| Operation | Duration / Action |
|-----------|-------------------|
| Trigger LOW | 2 microseconds |
| Trigger HIGH | 10 microseconds |
| Trigger LOW | Starts echo measurement |
| Echo Measurement | Measures the returning ultrasonic pulse |
| Distance Calculation | Converts the echo duration into centimeters |
| Distance Display | Displays the measured distance in the Thonny Shell |
| Measurement Interval | 1 second |
| Operation | Repeats continuously |

---

Distance-Based LED Operation

| Distance Condition | LED 1 | LED 2 | Status |
|---------------------|-------|-------|--------|
| Distance ≥ 5 cm | ON | OFF | Object is at or beyond the threshold |
| Distance < 5 cm | OFF | ON | Object is closer than the threshold |

---

Program Code

The complete program code is available in the Ultrasonic_Distance_Based_LED_Indicator_With_ESP32_and_MicroPython.py file.

---

Procedure

1. Connect the HC-SR04 VCC to the appropriate ESP32 power supply.
2. Connect the HC-SR04 GND to ESP32 GND.
3. Connect TRIG to GPIO 13.
4. Connect ECHO to GPIO 12.
5. Connect LED 1 to GPIO 2 through a 220Ω–330Ω resistor.
6. Connect LED 2 to GPIO 14 through a 220Ω–330Ω resistor.
7. Connect the cathodes of both LEDs to GND.
8. Connect the ESP32 to the computer using a USB cable.
9. Open Thonny IDE.
10. Select the MicroPython interpreter for ESP32.
11. Connect Thonny to the ESP32.
12. Open or enter the MicroPython program.
13. Run the program using Thonny.
14. Observe the distance measurement and LED status.

---

Expected Output

| Parameter | Expected Output |
|-----------|-----------------|
| Trigger Pin | GPIO 13 |
| Echo Pin | GPIO 12 |
| LED 1 Pin | GPIO 2 |
| LED 2 Pin | GPIO 14 |
| Distance Output | Displayed in centimeters |
| Distance ≥ 5 cm | LED 1 ON, LED 2 OFF |
| Distance < 5 cm | LED 1 OFF, LED 2 ON |
| Operation | Continuously monitors distance |

The Thonny Shell will display output similar to:

Distance: 8.42 cm

Distance: 7.91 cm

Distance: 4.73 cm

Distance: 3.85 cm

Distance: 6.21 cm

The LED response will follow:

Distance ≥ 5 cm → LED 1 ON  → LED 2 OFF

Distance < 5 cm → LED 1 OFF → LED 2 ON


---