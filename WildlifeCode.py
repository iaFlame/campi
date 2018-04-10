# Wildlife Camera Code
# Tristan and Mahit
# 3-14-18 (PI DAY!)

# Imports
import time
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep

#GPIO Setup
button_pin = 21
PIR_pin = 23
LED_pin = 12
camera_on = False
frame = 1
#Functions

# Setup for GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN)
GPIO.setup(PIR_pin, GPIO.IN)
GPIO.setup(LED_pin, GPIO.OUT)

# Setup Camera
camera = PiCamera()
blinks = 0
# Main Program
while True:
    # Toggle on and off the motion sensing loop using button
    if GPIO.input(button_pin):
        # Flip the flag (True --> False; False --> True)
        print("Camera Disabled")
        if camera_on == True:
            camera_on = False
        else:
            camera_on = True
            blinks = 0

    # Check for motion, if motion detected
    if camera_on == True and GPIO.input(PIR_pin):
        try:
            # Create the filename
            camera.capture('/home/pi/wcam/frame%03d.jpg' % frame)
            frame += 1
            # Take a picture or video
            print("Picture taken")
        except:
            print("Oops, I couldn't take the picture.")
    if camera_on == True and blinks < 5:
        blinks += 1
        GPIO.output(LED_pin,GPIO.HIGH)
        print("Camera Activated")
        time.sleep(.2)
        GPIO.output(LED_pin,GPIO.LOW)
        

    time.sleep(1)
    
                    




