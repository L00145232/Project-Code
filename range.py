import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

TRIG= 24
ECHO= 25

GPIO.setup(TRIG,GPIO.OUT)
GPIO.output(TRIG,0)

GPIO.setup(ECHO,GPIO.IN)

GPIO.setup(16,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)


time.sleep(0.1)

print ('starting measurement')

GPIO.output(TRIG,1)
time.sleep(0.00001)
GPIO.output(TRIG,0)

while GPIO.input(ECHO) == 0:
        pass
start = time.time()

while GPIO.input(ECHO) == 1:
        pass
stop=time.time()

if (stop-start)*17000 <= 8:
   print ("you have used hand sanitiser, a blue light is indictating the message")
   print ("your distance was","{:.2f}".format((stop-start)*17000)," cm")
   GPIO.output(16,GPIO.HIGH)
   time.sleep(2)
   GPIO.output(16,GPIO.LOW)



else:
   print ("please use hand sanitiser, a red light is indicating the message")
   print ("your distance was","{:.2f}".format((stop-start)*17000)," cm")
   GPIO.output(21,GPIO.HIGH)
   time.sleep(2)
   GPIO.output(21,GPIO.LOW)


GPIO.cleanup()
