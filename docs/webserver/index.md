# Webserver

We are going to develop a visually appealing web server on the Pico W using Phew and Bootstrap. 

This activity is to be completed in pairs. You need 2 computers to complete this activity.

## Phew
Phew!, developed by Pimoroni for their Enviro range, is designed to create captive Wi-Fi hotspots with a user-friendly web interface for device setup. It functions perfectly on Pico W boards and most other MicroPython devices, though it is tailored mainly for Pico W. Besides a reliable built-in web server, Phew! offers great features like logging and an easy-to-use templating system, simplifying the development of interactive websites.

- [Phew documentation](https://pypi.org/project/micropython-phew/)
- [Phew Code](https://github.com/pimoroni/phew/tree/main/phew)

## Steps
This code sets up a web server that can be accessed via the Pico W's IP address. The server has two routes: "/" and "/<command>". When you navigate to "/", it displays the HTML content of "index.html". When you navigate to "/<command>", it turns on or off an LED based on the command provided.

**Step 1.** Download all files in the [Phew Code](https://github.com/pimoroni/phew/tree/main/phew) github repository.

**Step 2.** Create a folder on your Pico W called /libs/phew and copy all files from step 1 into the folder

**Step 3.** Create a file called `index.html` and add the following code to it

``` html
<html>
<head>
    <title>Pico W Web Server</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:,">
    <style>
        html {
            font-family: Helvetica;
            display: inline-block;
            margin: 0px auto;
            text-align: center;
        }

        h1 {
            color: #0F3376;
            padding: 2vh;
        }

        p {
            font-size: 1.5rem;
        }

        button {
            display: inline-block;
            background-color: #4286f4;
            border: none;
            border-radius: 4px;
            color: white;
            padding: 16px 40px;
            text-decoration: none;
            font-size: 30px;
            margin:
                2px;
            cursor: pointer;
        }

        button2 {
            background-color: #4286f4;
        }
    </style>
</head>

<body>
    <h1>Pico W Web Server</h1>
    <p>GPIO state: <strong>gpio_state</strong></p>
    <p><a href="/on"><button class="button">ON</button></a></p>
    <p><a href="/off"><button class="button button2">OFF</button></a></p>
</body>
</html>
```

**Step 4.** Create a file called `main.py` and paste the following code into it:

``` python
from phew import server, connect_to_wifi
import machine

wifi = access_point("My-Access-Point-Beverley","1234567890")
```

- This code imports the necessary modules and creates an access point for your Pico W. 
    - `My-Access-Point-Beverley` is the SSID of the access point 
    - `1234567890` is the password

!!! Note
    You should change the SSID and password to something unique that you and your partner agree on.

``` python
page = open("index.html","r")
html= page.read()
page.close()
```

- This code reads the HTML content of "index.html" and stores it in a variable called `html`.

``` python
led = machine.Pin("LED", machine.Pin.OUT)

def gpio_state():
    if led.value() == 1:
        return 'On'
    else:
        return 'Off'
```

- This code creates a pin object for the onboard LED on your Pico W.
- Define a function called `gpio_state` that returns the current state of the LED. If the LED is on, it returns 'On'. Otherwise, it returns 'Off'.

``` python
@server.route("/", methods=["GET"])
def home(request):
    return str(html)
```

- This code defines a route for the home. A route is a URL that can be accessed by the user. In this case, the route is "/".

``` python
@server.route("/on", methods=["GET"])
def on_command(request):
    led.on()
    return str(html).replace('gpio_state', gpio_state())

@server.route("/off", methods=["GET"])
def off_command(request):
    led.off()
    return str(html).replace('gpio_state', gpio_state())
```

- This code defines routes for turning the LED on and off. The `<command>` part of the URL is a variable that can be accessed by the function. In this case, if the user goes to "/on", the LED will turn on. If the user goes to "/off", the LED will turn off.

``` python
@server.catchall()
def catchall(request):
    return "Page not found", 404
```

- This code defines a route for any other URL that is not defined above. If the user goes to a URL that is not defined, it will return "Page not found".

``` python
server.run()
```

- This code starts the server. The server will listen for incoming requests on port 8080.

!!! Question
    - What other features could be added to this webserver?
    - How could you use this to display a dashboard of sensor data?