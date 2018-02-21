from picamera import PiCamera
from time import sleep


camera = PiCamera()

#Picture

#camera.start_preview()
#sleep(5)
#camera.capture('/home/pi/Desktop/image.jpg')
#camera.stop_preview()

#Video

#camera.start_preview()
#camera.start_recording('/home/pi/video.h264')
#sleep(10)
#camera.stop_recording()
#camera.stop_preview()

#Transparent Picture

#camera.start_preview(alpha=200)
#sleep(10)
#camera.stop_preview()

#Five Pics

#camera.start_preview()
#for i in range(5):
   #sleep(5)
    #camera.capture('/home/pi/Desktop/image%s.jpg' % i)
#camera.stop_preview()

# picture with resolution

#camera.resolution = (2592, 1944)
#camera.framerate = 15
#camera.start_preview()
#sleep(5)
#camera.capture('/home/pi/Desktop/max.jpg')
#camera.stop_preview()

#pic with text

#camera.start_preview()
#camera.annotate_text = "Bello World"
#sleep(5)
#camera.capture('/home/pi/Desktop/text.jpg')
#camera.stop_preview()

# pic brightness

#camera.start_preview()
#camera.brightness = 70
#sleep(5)
#camera.capture('/home/pi/Desktop/bright.jpg')
#camera.stop_preview()

# Pic brightness change

#camera.start_preview()
#for i in range(100):
      #camera.annotate_text = "Brightness: %s" % i
      #camera.brightness = i
      #sleep(0.1)
#camera.stop_preview()

#pic contrast

#camera.start_preview()
#for i in range(100):
      #camera.annotate_text = "Contrast: %s" % i
      #camera.contrast = i
      #sleep(0.1)
#camera.stop_preview()

#Text Color

#camera.annotate_text_size = 50

#from picamera import PiCamera, Color

#camera.start_preview()
#camera.annotate_background = Color('blue')
#camera.annotate_foreground = Color('pink')
#camera.annotate_text = " YO WORLD DIS IS MAHET "
#sleep(5)
#camera.stop_preview()

#Camera effects

#camera.start_preview()
#camera.image_effect = 'solarize'
#sleep(5)
#camera.capture('home/pi/Desktop/solarize .jpg')
#camera.stop_preview()

#Camera effect loop

#camera.start_preview()
#for effect in camera.IMAGE_EFFECTS:
    #camera.image_effect = effect
    #camera.annotate_text = "Effect: %s" % effect
    #sleep(5)
#camera.stop_preview()

#agust pic

#camera.start_preview()
#camera.qwb_mode = 'sunlight'
#sleep(5)
#cmera.capture('/home/pi/Desktop/sunlight.jpg')
#camera.stop_preview()
#film vedio


#camera.start_preview()
#camera.exposure_mode = 'beach'
#sleep(5)
##camera.capture('/home/pi/Desktop/beach.jpg')
#camera.stop_preview() 























