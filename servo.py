import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
p = GPIO.PWM(17, 50)
p.start(5)
try:
    while True:
        p.ChangeDutyCycle(2.5)
        time.sleep(2)
        p.ChangeDutyCycle(11.5)
        time.sleep(2)
        p.ChangeDutyCycle(20.5)
        time.sleep(2)

except KeyboardInterrupt:
        GPIO.cleanup()
