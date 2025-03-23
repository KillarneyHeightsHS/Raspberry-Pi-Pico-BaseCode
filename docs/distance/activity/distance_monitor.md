# Parking Sensor

You have been approached to develop a parking sensor system for a car. The system should be able to detect when the car is too close to another object and provide an alert to the driver. The system should also be able to measure the distance between the car and the object. You should display varying levels of alerts based on the distance, such as "Red" for 10cm, "Orange" for 20cm, "Yellow" for 30cm, "Green" for 40cm, and "Blue" for 50cm. The system could also display the distance in centimetres on a digital display.

## Wiring Diagram

## Steps to Implement

### Step 1: Components
- Ultrasonic Sensor (SR04)
- 8 LED RGB Module
- LCD Display
- Breadboard and Jumper Wires
- Raspberry Pi Pico

### Step 2: Setup the Ultrasonic Sensor
Connect the ultrasonic sensor to the Raspberry Pi Pico according to the wiring diagram. Make sure to connect the VCC and GND pins of the sensor to a 3.3V power source on the Raspberry Pi Pico.

| Ultrasonic Sensor | Raspberry Pi Pico | Colour |
|------------------|-------------------| ---|
| VCC              | 3.3V              | Red |
| GND              | GND               | Black |
| Trig             | GP17              | Green |
| Echo             | GP16              | Yellow |

### Step 3: Setup the RGB LED Module
Connect the RGB LED module to the Raspberry Pi Pico according to the wiring diagram. Make sure to connect the VCC and GND pins of the module to a 3.3V power source on the Raspberry Pi Pico.

| RGB LED Module | Raspberry Pi Pico | Colour |
|----------------|-------------------| ---|
| VCC              | 3.3V              | Red |
| GND              | GND               | Black |
| S                | GP21              | Brown |

### Step 4: Setup the LCD Display (Optional)
Connect the LCD display to the Raspberry Pi Pico according to the wiring diagram. Make sure to connect the VCC and GND pins of the module to a 3.3V power source on the Raspberry Pi Pico.

| LCD Display | Raspberry Pi Pico | Colour |
|-------------|-------------------| ---|
| VCC         | 3.3V              | Red |
| GND         | GND               | Black |
| SDA         | GP14              | Brown |
| SCL         | GP15              | Orange |

### Step 5: Write the Code

### Step 6: Test the System
