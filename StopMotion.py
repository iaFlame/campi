#Stop Motion
#2-21-18 My mom's birthday!

from picamera import PiCamera
from time import sleep
from gpiozero import Button
button = Button(17)
camera = PiCamera()

#camera = PiCamera()

#camera.start_preview()
#sleep(3)
#camera.capture('/home/pi/Desktop/image.jpg')
#camera.stop_preview()



#from picamera import PiCamera
#from time import sleep

#camera = PiCamera()

#camera.rotation = 180
#camera.start_preview()
#sleep(3)
#camera.capture('/home/pi/Desktop/image.jpg')
#camera.stop_preview()

#Take picture with button


#from picamera import PiCamera
#from time import sleep



#camera.start_preview()
#button.wait_for_press()
#camera.capture('/home/pi/image3.jpg')
#camera.stop_preview()
#camera.start_preview()
#button.wait_for_press()
#sleep(3)
#camera.capture('/home/pi/Desktop/image5.jpg')
#camera.stop_preview()

#camera.start_preview()
#frame = 1
#while True:
 #   try:
  #      button.wait_for_press()
   #     camera.capture('/home/pi/animation/frame%03d.jpg' % frame)
    #    frame +=1
    #except KeyboardInterrupt:
     #   camera.stop_preview()
      #  break
