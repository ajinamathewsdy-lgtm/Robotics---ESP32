Ultrasonic Distance Measurement With ESP32 and MicroPython

This project demonstrates distance measurement using an HC-SR04 ultrasonic sensor, ESP32, and MicroPython. The sensor uses a trigger pulse and measures the time taken for the echo signal to return. The calculated distance is displayed in the Thonny Shell in centimeters.


---

Objective

| Objective | Description |
|-----------|-------------|
| Distance Measurement | Measure the distance of an object using an ultrasonic sensor |
| GPIO Control | Configure GPIO 13 as the trigger output and GPIO 12 as the echo input |
| Pulse Measurement | Measure the duration of the returning ultrasonic echo |
| Distance Calculation | Convert the measured echo duration into distance in centimeters |
| MicroPython Programming | Interface the ESP32 with an ultrasonic sensor using MicroPython |
| Continuous Measurement | Continuously measure and display the distance |

---

Components Required

| Component | Quantity |
|-----------|----------|
| ESP32 Development Board | 1 |
| HC-SR04 Ultrasonic Sensor | 1 |
| Breadboard | 1 |
| Jumper Wires | 4 |
| USB Cable | 1 |

---

Circuit Connections

| Connection | Purpose |
|------------|---------|
| HC-SR04 VCC → ESP32 5V/VIN | Supplies power to the ultrasonic sensor |
| HC-SR04 GND → ESP32 GND | Provides common ground |
| HC-SR04 TRIG → ESP32 GPIO 13 | Sends the ultrasonic trigger pulse |
| HC-SR04 ECHO → ESP32 GPIO 12 | Receives the returning echo signal |

Connection Flow

ESP32 GPIO 13 → HC-SR04 TRIG

ESP32 GPIO 12 ← HC-SR04 ECHO

ESP32 5V/VIN  → HC-SR04 VCC

ESP32 GND     → HC-SR04 GND

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
| `machine.time_pulse_us` | Measures the duration of the echo pulse |
| `time` | Provides microsecond and second delay functions |

No external libraries are required for this project.

---

GPIO Configuration

| GPIO Connection | Configuration | Purpose |
|-----------------|---------------|---------|
| GPIO 13 | `Pin.OUT` | Sends the trigger pulse to the ultrasonic sensor |
| GPIO 12 | `Pin.IN` | Receives the echo signal from the ultrasonic sensor |
| GND | Ground | Provides common ground |

---

Working Principle

1. GPIO 13 is configured as an output for the ultrasonic sensor's trigger signal.
2. GPIO 12 is configured as an input for receiving the echo signal.
3. The trigger pin is first set LOW for 2 microseconds.
4. The trigger pin is then set HIGH for 10 microseconds to start ultrasonic transmission.
5. The trigger pin is set LOW again.
6. time_pulse_us() measures how long the echo pin remains HIGH.
7. The measured pulse duration is used to calculate the distance.
8. The calculated distance is printed in centimeters.
9. The process repeats every 1 second.

---

Ultrasonic Sensor Operation

| Operation | Duration / Action |
|-----------|-------------------|
| Trigger LOW | 2 microseconds |
| Trigger HIGH | 10 microseconds |
| Trigger LOW | Starts echo measurement |
| Echo Measurement | Measures the returning ultrasonic pulse |
| Distance Calculation | Converts pulse duration into centimeters |
| Measurement Interval | 1 second |
| Operation | Repeats continuously |

---

Program Code

The complete program code is available in the Ultrasonic_Distance_Measurement_With_ESP32_and_MicroPython.py file.

---

Procedure

1. Connect the HC-SR04 VCC to the appropriate ESP32 power supply.
2. Connect the HC-SR04 GND to ESP32 GND.
3. Connect the HC-SR04 TRIG pin to GPIO 13.
4. Connect the HC-SR04 ECHO pin to GPIO 12.
5. Connect the ESP32 to the computer using a USB cable.
6. Open Thonny IDE.
7. Select the MicroPython interpreter for ESP32.
8. Connect Thonny to the ESP32.
9. Enter or open the MicroPython program.
10. Run the program using Thonny.
11. Observe the measured distance in the Thonny Shell.

---

Expected Output

| Parameter | Expected Output |
|-----------|-----------------|
| Sensor | HC-SR04 Ultrasonic Sensor |
| Trigger Pin | GPIO 13 |
| Echo Pin | GPIO 12 |
| Output | Distance in centimeters |
| Display | Thonny Shell |
| Measurement | Updated every 1 second |
| Operation | Continuous distance measurement |

The Thonny Shell will display output similar to:

Distance: 25.43 cm

Distance: 25.18 cm

Distance: 24.97 cm

Distance: 25.31 cm

...

---
