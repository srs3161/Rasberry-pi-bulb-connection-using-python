##################################################
# name:Satyendra Raj Singh
# date:10/26/2023
#description: Python program to blink computer in the guven interval and after pressing switch
#########################################################
######importing relevent libraries#######
import pineworkslabs.RPi as GPIO
from time import sleep

#### now to set the naming convention a.k.a. mode
GPIO.setmode(GPIO.LE_POTATO_LOOKUP)

#####store an output pin number
led = 18
###### store an input pin number
switch = 19

#setting them up as either output or input pins
GPIO.setup(led, GPIO.OUT)
GPIO.setup(switch, GPIO.IN)

# loop during which the led blinks 0.5 sec
# if switched button led blinks 0.1 sec
# returns back to original if button isn't pressed anymore
while(True):
    if(GPIO.input(19) == GPIO.OUT):
        GPIO.output(18, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(18, GPIO.LOW)
        sleep(0.1)
    else:
        GPIO.output(18, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(18, GPIO.LOW)
        sleep(0.5)

