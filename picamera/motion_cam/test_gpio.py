from gpiozero import LED
import time
print ("Testing all GPIOs")
yellow = LED(15)
brown = LED(16)
blue = LED(21)
time.sleep(1)
yellow.on()
print ("GPIO 15 on")
time.sleep(5)
brown.on()
print ("GPIO 16 on")
time.sleep(5)
blue.on()
print ("GPIO 21 on")
time.sleep(5)