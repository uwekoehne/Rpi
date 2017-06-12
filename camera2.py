from picamera import PiCamera
from os import system
from time import sleep

camera = PiCamera()
camera.resolution = (1024, 768)

for i in range(5):
    camera.capture('/home/pi/time-lapse2/image{0:04d}.jpg'.format(i))
    sleep(2)

# system('convert -delay 10 -loop 0 /home/pi/time-lapse2/image*.jpg /home/pi/time-lapse2/animation.gif')

