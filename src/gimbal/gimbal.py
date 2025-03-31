# Needs the servo_lib and MPU6050 libraries to be installed and imported.

from servo_lib import Servo
from mpu6050 import MPU6050
from machine import Pin, I2C
import time

time.sleep_ms(1000)

servo = Servo(7)
servo.ServoAngle(90)
time.sleep_ms(1000)

i2c = I2C(1, sda=Pin(14), scl=Pin(15))
mpu = MPU6050(i2c)
mpu.wake()

position = 90
try:
  # continuously print the data
  while True:
      gyro = mpu.read_gyro_data()
      accel = mpu.read_accel_data()
      #print("Gyro: " + str(gyro) + ", Accel: " + str(accel))

      if gyro[1] < -1 or gyro[1] > 1:
         print(f'y-axis {gyro[1]}')
         rotation = 0
         if gyro[1] < -180:
            rotation = 180 / 2
         elif gyro[1] > 180:
            rotation = 180 / 2
         else:
            rotation = gyro[1] / 2
         print(f'rotation {rotation}')
         position += rotation
         servo.ServoAngle(position)

      time.sleep(0.1)
except:
  pass