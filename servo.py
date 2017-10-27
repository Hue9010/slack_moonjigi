import RPi.GPIO as GPIO
import time

def run_servo():
    pin = 18 # PWM pin num 18

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    p = GPIO.PWM(pin, 50)
    p.start(0)
    cnt = 0
    try:
        p.ChangeDutyCycle(2.5)
        time.sleep(1)
        p.ChangeDutyCycle(12.5)
        time.sleep(1)
    except KeyboardInterrupt:
        p.stop()
    GPIO.cleanup()

if __name__ == '__main__':
    run_servo()
