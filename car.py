
import RPi.GPIO as gpio
import time

try:
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)

    def forward():
        gpio.setmode(gpio.BOARD)
        gpio.setup(7, gpio.OUT)
        gpio.setup(11, gpio.OUT)
        gpio.setup(13, gpio.OUT)
        gpio.setup(15, gpio.OUT)
        gpio.output(13, True)
        gpio.output(15, False)
        gpio.output(11, True)
        gpio.output(7, False)
        time.sleep(0.5)
        gpio.cleanup()

    def backward():
        gpio.setmode(gpio.BOARD)
        gpio.setup(7, gpio.OUT)
        gpio.setup(11, gpio.OUT)
        gpio.setup(13, gpio.OUT)
        gpio.setup(15, gpio.OUT)
        gpio.output(13, False)
        gpio.output(15, True)
        gpio.output(11, False)
        gpio.output(7, True)
        time.sleep(0.5)
        gpio.cleanup()

    def right():
        gpio.setmode(gpio.BOARD)
        gpio.setup(7, gpio.OUT)
        gpio.setup(11, gpio.OUT)
        gpio.setup(13, gpio.OUT)
        gpio.setup(15, gpio.OUT)
        gpio.output(13, False)
        gpio.output(15, True)
        gpio.output(11, True)
        gpio.output(7, False)
        time.sleep(1.5)
        gpio.cleanup()

    def left():
        gpio.setmode(gpio.BOARD)
        gpio.setup(7, gpio.OUT)
        gpio.setup(11, gpio.OUT)
        gpio.setup(13, gpio.OUT)
        gpio.setup(15, gpio.OUT)
        gpio.output(13, True)
        gpio.output(15, False)
        gpio.output(11, False)
        gpio.output(7, True)
        time.sleep(1.5)
        gpio.cleanup()

    def clean():
        gpio.cleanup()

except:
    gpio.cleanup()
