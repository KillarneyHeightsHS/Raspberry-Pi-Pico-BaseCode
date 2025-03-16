from mpu6050 import MPU6050
from machine import Pin
import time

time.sleep(0.1) # Wait for USB to become ready

errorLed = Pin(3, Pin.OUT)
okLed = Pin(4, Pin.OUT)

i2c = machine.I2C(1, sda=Pin(14), scl=Pin(15))
mpu = MPU6050(i2c)

# wake up the MPU6050 from sleep
mpu.wake()


try:
  # continuously print the data
  while True:
      gyro = mpu.read_gyro_data()
      accel = mpu.read_accel_data()
      print("Gyro: " + str(gyro) + ", Accel: " + str(accel))

      if 20 > gyro[0] > -20:
        okLed.high()
        errorLed.low()
      else:
        okLed.low()
        errorLed.high()

      time.sleep(0.1)
except:
  pass