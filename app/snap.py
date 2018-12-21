from datetime import datetime
from os import environ
import sys

from blinkpy import blinkpy


try:
    username = environ['USERNAME']
except KeyError:
    sys.exit("'USERNAME' environment variable is not set")
try:
    password = environ['PASSWORD']
except KeyError:
    sys.exit("'PASSWORD' environment variable is not set")
try:
    camera_names = environ['CAMERAS'].split(',')
except KeyError:
    sys.exit("'CAMERAS' environment variable is not set")


blink = blinkpy.Blink(username=username, password=password)
blink.start()

print(f'Taking pictures for cameras: {", ".join(camera_names)}')

for camera_name in camera_names:
    camera = blink.cameras[camera_name]
    camera.snap_picture()
    blink.refresh()

    path = f'/images/{camera_name}-{datetime.utcnow().isoformat(timespec="seconds")}.jpg'

    camera.image_to_file(path)
    print(f'Image from {camera_name} saved to {path}')
