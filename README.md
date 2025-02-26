# Raspberry-Pi-Pico-BaseCode
Base code for working with the raspberry pi pico

## Getting Started
### Loading the Firmware

1. You will need to download the latest micropython version to load onto the [Raspberry Pi Pico W](https://micropython.org/download/RPI_PICO_W/). Ensure you grab the latest build and not a preview build.

![Pico Download](./images/pico_download.png)

2. Place your Raspberry Pi Pico into the breadboard to protect the pins and your fingers.
3. Hold down the <kbd>BOOTSEL</kbd> button on the raspberry Pi Pico

![RP Pico W](./images/rp_pico_w.png)

3. Connect the Pi Pico to the USB cable connected to you laptop.
4. When the drive is displayed in Windows Explorer or Mac Finder copy the uf2 file from step 1 onto the Pi Pico drive.
5. If this was successful the drive will disappear as the device has been reset ready for use.

### Your First Program
We will be using [VSCode](https://code.visualstudio.com/download) so ensure you have that installed. 

1. Disconnect the Pi Pico from your laptop.
2. Download the VSCode profile for the Pi Pico from VSCode Setup Repo, [RP Pico.code-profile](https://github.com/KillarneyHeightsHS/vscode-setup/blob/main/profiles/RP%20Pico.code-profile) by clicking on the `Download raw file` icon.
3. Follow the instructions [here](https://github.com/KillarneyHeightsHS/vscode-setup/tree/main) to import it into VSCode
4. You should now see a new icon on the left called `Raspberry Pi Pico Project` ![Pico Project](./images/pico_project.png)
5. Connect the Pi Pico to your laptop
6. Click on it and select `New MicroPython Project`
![New Project](./images/new_project.png)
7. Give your project a name `Blinky` and change the location to where you want the project to be created.
![Create Project](./images/create_project.png)
8. Click `Create` to create your new Pi Pico project
9. If everything has gone smoothly you should have a new project that looks like the below image.
![Pico Project](./images/vscode_pico_project.png)
10. You should see that the Pico is connected and you can click on the run icon in the bottom left position to run the code python conde in `blink.py` on the Pi Pico.

## Sensors
 - Thermistor
 - Ultrasonic
 - Infrared remote(IR)
 - Accelerometer
 - Photoresistor
## Actuators
 - Servo
 - Motor
## Input and Output
 - LED / LED Bar
 - Analog and PWM
 - Button
 - Joystick
 - LCD1602
 - Logging

