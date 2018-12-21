from os import environ

from blinkpy import blinkpy

try:
    username = environ['USERNAME']
except KeyError:
    sys.exit("'USERNAME' environment variable is not set")
try:
    password = environ['PASSWORD']
except KeyError:
    sys.exit("'PASSWORD' environment variable is not set")

blink = blinkpy.Blink(username=username, password=password)
blink.start()

for name, camera in blink.cameras.items():
    print(name, camera.attributes)
