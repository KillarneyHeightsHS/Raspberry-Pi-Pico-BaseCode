from phew import server, access_point
import machine

wlan = access_point('PICO-W')

while wlan.active() == False:
    pass
print('AP Mode Is Active, You can Now Connect')
print('IP Address To Connect to:: ' + wlan.ifconfig()[0])

page = open("index.html","r")
html= page.read()
page.close()

led = machine.Pin("LED", machine.Pin.OUT)

@server.route("/", methods=["GET"])
def home(request):
    return str(html)

@server.route("/on", methods=["GET"])
def on_command(request):
    led.on()
    return str(html)

@server.route("/off", methods=["GET"])
def off_command(request):
    led.off()
    return str(html)

@server.route("/bootstrap.min.css", methods=['GET'])
def get_bootstrap_css(request):
    return server.FileResponse('static/bootstrap.min.css', headers={'Content-Type':'text/css', 'Cache-Control': 'max-age=604800', 'Age':100})

@server.route("/bootstrap.min.js", methods=['GET'])
def get_bootstrap_js(request):
    return server.FileResponse('static/bootstrap.min.js', headers={'Content-Type': 'text/js', 'Cache-Control': 'max-age=604800', 'Age':100})

@server.route("/bootstrap.min.js.map", methods=['GET'])
def get_bootstrap_js_map(request):
    return server.FileResponse('static/bootstrap.min.js.map', headers={'Content-Type': 'text/json', 'Cache-Control': 'max-age=604800', 'Age':100})

@server.catchall()
def catchall(request):
    return "Page not found", 404

server.run()