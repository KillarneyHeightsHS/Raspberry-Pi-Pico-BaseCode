from mpu6050 import MPU6050
from machine import Pin
import time

time.sleep(0.1) # Wait for USB to become ready

# configure the pins
errorLed = Pin(3, Pin.OUT)
okLed = Pin(4, Pin.OUT)
button = Pin(8, Pin.IN)

# indicate if the alarm is armed
alarm_armed = False

# configure the accelerometer
i2c = machine.I2C(1, sda=Pin(14), scl=Pin(15))
mpu = MPU6050(i2c)

# wake up the MPU6050 from sleep
mpu.wake()

def flash_led():
    # Flash the on led 4 times in 2 seocnds
    for flash_count in range(8):
        print(f'Arming the alarm {flash_count}')
        okLed.value(flash_count % 2)
        time.sleep(0.5)

def get_strength(mpu):
    # Gets the combined acceleration measurement across all 3 axis as a +ve value in g
    accel = mpu.read_accel_data()
    return sum(abs(a) for a in accel)

while True:
    
    # Arm the alarm 
    if button.value() == 0:
        alarm_armed = True
        print('Arming the alarm')
        flash_led()

    # Check if the alarm has been triggered
    if alarm_armed and get_strength(mpu) > 0.1:
        errorLed.high()
        okLed.low()
        print('Alarm Triggered')

    time.sleep(0.1)