
from gpiozero import AngularServo
from time import sleep

servo = AngularServo(17, min_pulse_width=0.0006, max_pulse_width=0.0023)


servo.angle = 90
sleep(1)

servo.detach()
sleep(5)

servo.angle = 0
sleep(1)

