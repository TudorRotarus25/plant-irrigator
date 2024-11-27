# import RPi.GPIO as GPIO


class PumpService:
  gpio_pin: int

  def __init__(self, gpio_pin):
    self.gpio_pin = gpio_pin
    # GPIO.setmode(GPIO.BOARD)
    # GPIO.setup(gpio_pin, GPIO.OUT)

  def start_watering(self) -> None:
    print(f"turning on pin {self.gpio_pin}")
    # GPIO.output(self.gpio_pin, False)

  def stop_watering(self) -> None:
    print(f"turning off pin {self.gpio_pin}")
    # GPIO.output(self.gpio_pin, True)
    # GPIO.cleanup()
