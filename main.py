import time
import RPi.GPIO as GPIO

TRIG = 40
ECHO = 38
BUZZ = 12

GPIO.setmode(GPIO.BOARD)

GPIO.setup(BUZZ, GPIO.OUT)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

pwm = GPIO.PWM(BUZZ, 2000)
pwm.start(1)


def distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    start = time.time()
    stop = time.time()

    while GPIO.input(ECHO) == 0:
        start = time.time()

    while GPIO.input(ECHO) == 1:
        stop = time.time()

    timeDist = stop - start
    distance = timeDist * 17000

    return distance


try:
    while True:
        dist = distance()
        if dist < 100:
            pwm.ChangeDutyCycle(dist)
            print(dist)
        time.sleep(0.1)
except KeyboardInterrupt:
    pwm.ChangeDutyCycle(0)
    print("stopped")
    GPIO.cleanup()