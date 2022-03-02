import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

# Create a dictionary called pins to store the pin number, name, and pin state:
# GPIO 17 = GPIO_GEN0
# GPIO 18 = GPIO_GEN1
# GPIO 27 = GPIO_GEN2
# GPIO 22 = GPIO_GEN3
# GPIO 23 = GPIO_GEN4
# GPIO 24 = GPIO_GEN5

pins = {
   'relay1' : {'name' : 'GPIO 17', 'state' : GPIO.LOW},
   'relay2' : {'name' : 'GPIO 18', 'state' : GPIO.LOW},
   'relay3' : {'name' : 'GPIO 27', 'state' : GPIO.LOW},
   'relay4' : {'name' : 'GPIO 22', 'state' : GPIO.LOW},
   'relay5' : {'name' : 'GPIO 23', 'state' : GPIO.LOW},
   'relay6' : {'name' : 'GPIO 24', 'state' : GPIO.LOW}
   }
