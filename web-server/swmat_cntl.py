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
   17 : {'name' : 'relay1', 'state' : GPIO.LOW, 'antstate' : 'allterm'},
   18 : {'name' : 'relay2', 'state' : GPIO.LOW, 'antstate' : 'allterm'},
   27 : {'name' : 'relay3', 'state' : GPIO.LOW, 'antstate' : 'allterm'},
   22 : {'name' : 'relay4', 'state' : GPIO.LOW, 'antstate' : 'allterm'},
   23 : {'name' : 'relay5', 'state' : GPIO.LOW, 'antstate' : 'allterm'},
   24 : {'name' : 'relay6', 'state' : GPIO.LOW, 'antstate' : 'allterm'},
   25 : {'name' : 'dummy', 'state' : GPIO.LOW, 'antstate' : 'allterm'}
   }

# Set each pin as an output and make it low:
for pin in pins:
   GPIO.setup(pin, GPIO.OUT)
   GPIO.output(pin, GPIO.LOW)

@app.route("/")
def main():
   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)
   # Put the pin dictionary into the template data dictionary:
   templateData = {
      'pins' : pins
      }
   # Pass the template data into the template main.html and return it to the user
   return render_template('main.html', **templateData)

# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<changePin>/<action>")
def action(changePin, action):
   # Convert the pin from the URL into an integer:
   changePin = int(changePin)
   # Get the device name for the pin being changed:
   deviceName = pins[changePin]['name']
   # If the action part of the URL is "on," execute the code indented below:
   if action == "on":
      # Set the pin high:
      GPIO.output(changePin, GPIO.HIGH)
      # Save the status message to be passed into the template:
      message = "Turned " + deviceName + " on."
   if action == "off":
      GPIO.output(changePin, GPIO.LOW)
      message = "Turned " + deviceName + " off."

   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)
      
   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'pins' : pins
   }
      
   # print(pins)
      
   if pins[17]['state'] == 0 and \
      pins[18]['state'] == 0 and \
      pins[27]['state'] == 0 and \
      pins[22]['state'] == 0 and \
      pins[23]['state'] == 0 and \
      pins[24]['state'] == 0:
          pins[25]['antstate'] = 'allterm'
   elif pins[17]['state'] == 1 and \
        pins[18]['state'] == 0 and \
        pins[27]['state'] == 0 and \
        pins[22]['state'] == 0 and \
        pins[23]['state'] == 0 and \
        pins[24]['state'] == 0:
            pins[25]['antstate'] = 'ant1rig1'
   elif pins[17]['state'] == 1 and \
        pins[18]['state'] == 0 and \
        pins[27]['state'] == 0 and \
        pins[22]['state'] == 1 and \
        pins[23]['state'] == 0 and \
        pins[24]['state'] == 0:
            pins[25]['antstate'] = 'ant1rig2'        
   elif pins[17]['state'] == 0 and \
        pins[18]['state'] == 1 and \
        pins[27]['state'] == 0 and \
        pins[22]['state']== 0 and \
        pins[23]['state'] == 0 and \
        pins[24]['state'] == 0:
            pins[25]['antstate'] = 'ant2rig1' 
   elif pins[17]['state'] == 0 and \
        pins[18]['state'] == 1 and \
        pins[27]['state'] == 0 and \
        pins[22]['state'] == 0 and \
        pins[23]['state'] == 0 and \
        pins[24]['state'] == 0:
            pins[25]['antstate'] = 'ant2rig2' 
   elif pins[17]['state'] == 0 and \
        pins[18]['state'] == 0 and \
        pins[27]['state'] == 1 and \
        pins[22]['state'] == 0 and \
        pins[23]['state'] == 0 and \
        pins[24]['state'] == 0:
            pins[25]['antstate'] = 'ant3rig1'
   elif pins[17]['state'] == 0 and \
        pins[18]['state'] == 0 and \
        pins[27]['state'] == 1 and \
        pins[22]['state'] == 0 and \
        pins[23]['state'] == 0 and \
        pins[24]['state'] == 1:
            pins[25]['antstate'] = 'ant3rig2'
   elif pins[17]['state'] == 1 and \
        pins[18]['state'] == 1 and \
        pins[27]['state'] == 0 and \
        pins[22]['state'] == 0 and \
        pins[23]['state'] == 1 and \
        pins[24]['state'] == 0:
            pins[25]['antstate'] = 'ant1rig1_ant2rig2'
   elif pins[17]['state'] == 1 and \
        pins[18]['state'] == 1 and \
        pins[27]['state'] == 0 and \
        pins[22]['state'] == 1 and \
        pins[23]['state'] == 0 and \
        pins[24]['state'] == 0:
            pins[25]['antstate'] = 'ant1rig2_ant2rig1'
   elif pins[17]['state'] == 1 and \
        pins[18]['state'] == 1 and \
        pins[27]['state'] == 0 and \
        pins[22]['state'] == 1 and \
        pins[23]['state'] == 0 and \
        pins[24]['state'] == 0:
            pins[25]['antstate'] = 'ant1rig1_ant3rig2'
   elif pins[17]['state'] == 1 and \
        pins[18]['state'] == 0 and \
        pins[27]['state'] == 1 and \
        pins[22]['state'] == 1 and \
        pins[23]['state'] == 0 and \
        pins[24]['state'] == 0:
            pins[25]['antstate'] = 'ant1rig2_ant3rig1'
   elif pins[17]['state'] == 0 and \
        pins[18]['state'] == 1 and \
        pins[27]['state'] == 1 and \
        pins[22]['state'] == 0 and \
        pins[23]['state'] == 0 and \
        pins[24]['state'] == 1:
            pins[25]['antstate'] = 'ant2rig1_ant3rig2'
   elif pins[17]['state'] == 0 and \
        pins[18]['state'] == 1 and \
        pins[27]['state'] == 1 and \
        pins[22]['state'] == 0 and \
        pins[23]['state'] == 1 and \
        pins[24]['state'] == 0:
            pins[25]['antstate'] = 'ant2rig2_ant3rig1'
   else:
        pins[25]['antstate'] = 'undefined'
            
   # antstate = 'allterm'
   # Along with the pin dictionary, put the message into the template data dictionary:
   # templateData = {
   #   antstate
   # }

   return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=GPIO.HIGH)