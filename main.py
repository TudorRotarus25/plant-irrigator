import RPi.GPIO as GPIO
import time

in1 = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)

GPIO.output(in1, True)

try:
  GPIO.output(in1, False)
  time.sleep(3)
  GPIO.output(in1, True)
  GPIO.cleanup()
except KeyboardInterrupt:
  GPIO.cleanup()
