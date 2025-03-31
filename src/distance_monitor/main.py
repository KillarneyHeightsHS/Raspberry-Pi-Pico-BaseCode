# Import necessary libraries
import time
import math
from machine import Pin, PWM
import neopixel

# Define pins for ultrasonic sensor
trig = Pin(17, Pin.OUT)
echo = Pin(16, Pin.IN)

# Define pin for LEDs
pixel = neopixel.NeoPixel(Pin(8, Pin.OUT), 8)

# Define pin for buzzer
passiveBuzzer = PWM(Pin(15, Pin.OUT))
passiveBuzzer.freq(1000)
PI = 3.14

# Function to set the colour of the pixel ring
def set_pixel_colour(colour):
    print(f'set colour: {colour}')
    if colour == 'Red': 
        pixel.fill((64, 0, 0))
    elif colour == 'Yellow': 
        pixel.fill((64, 64, 0))
    else: 
        pixel.fill((0, 64, 0))
    pixel.write()

# Function to measure distance
def measure_distance():
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    while echo.value() == 0:
        pulse_start = time.ticks_us()
    while echo.value() == 1:
        pulse_end = time.ticks_us()
    pulse_duration = time.ticks_diff(pulse_end, pulse_start)
    distance = pulse_duration * 0.0343 / 2
    return distance

def sound_distance():
    print('Make sound')
    passiveBuzzer.duty_u16(2*4092)
    for x in range(0, 36):
        sinVal = math.sin(x * 10 * PI / 180)
        toneVal = 1500 + int(sinVal * 500)
        passiveBuzzer.freq(toneVal)
        time.sleep_ms(10)

# Main loop
while True:
    distance = measure_distance()
    print("Distance:", distance, "cm")
    time.sleep_ms(500)

    if distance < 5:
        pixel.write()
        set_pixel_colour('Red')
        sound_distance()
    elif distance < 20:
        set_pixel_colour('Yellow')
        passiveBuzzer.duty_u16(0)
    else:
        set_pixel_colour('Green')
        passiveBuzzer.duty_u16(0)