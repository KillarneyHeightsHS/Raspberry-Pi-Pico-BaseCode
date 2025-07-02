import time
from machine import I2C, Pin, ADC
from I2C_LCD import I2CLcd
from stepmotor import Stepmotor

i2c = I2C(1, sda=Pin(14), scl=Pin(15), freq=400000)
devices = i2c.scan()
adc = ADC(26)
stepperMotor = Stepmotor(21, 20, 19, 18)


try:
    if devices != []:
        lcd = I2CLcd(i2c, devices[0], 2, 16)
        lcd.move_to(0, 0)
        lcd.putstr("Hello, world!")
        count = 0
        while True:

            adcValue = adc.read_u16()
            if adcValue < 65535 / 2:                
                lcd.move_to(0, 1)
                lcd.putstr("Turn Right")
                stepperMotor.moveSteps(1, 32*64, 2000)
                stepperMotor.stop()
                time.sleep(1)
            else:
                lcd.move_to(0, 1)
                lcd.putstr("Turn Left ")
                stepperMotor.moveSteps(0, 32*64, 2000)
                stepperMotor.stop()
                time.sleep(1)

    else:
        print("No address found")
except:
    pass