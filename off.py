import RPi.GPIO as GPIO

in1 = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)

GPIO.output(in1, False)

try:
  GPIO.output(in1, False)
  GPIO.cleanup()
except KeyboardInterrupt:
  GPIO.cleanup()
