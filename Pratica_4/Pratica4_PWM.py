import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(3, GPIO.OUT)

pwm = GPIO.PWM(3, 100)
pwm.start(0)

for dc in range(101):
    pwm.ChangeDutyCycle(dc)
    sleep(0.1)