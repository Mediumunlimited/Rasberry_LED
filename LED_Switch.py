# GPIO.setwarnings(False) to disable GPIO warnings
# GPIO.setmode(GPIO.BOARD) # Locate pins by numerical order (Number in the middle of the diagram)
# GPIO.setmode(GPIO.BCM) # Locate pins by Broadcom SOC Channel (Number on the sides of the diagram)
# GPIO.setup(Pin,OUT/IN) # Set pin to output or input

pin = 23 # Set var "pin" to int 23
import RPi.GPIO as GPIO # Required to control GPIO pins on the Raspberry Pi
GPIO.setwarnings(False) # Disable GPIO warnings
GPIO.setmode(GPIO.BCM) # Locate pins by Broadcom SOC Channel (Number on the sides of the diagram)
GPIO.setup(pin,GPIO.OUT) # Set pin to output (Pin, OUT/IN)

def led_switch ():
    if GPIO.input(pin): # If LED is on
        GPIO.output(pin,GPIO.LOW) # Turn off
        print ("OFF") 
    else: # Otherwise
        GPIO.output(pin,GPIO.HIGH) # Turn on
        print ("ON")

led_switch() # Calls led_switch function
