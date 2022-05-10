import board
import busio as io
import adafruit_mlx90614
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)


i2c = io.I2C(board.SCL, board.SDA, frequency = 100000)
mlx = adafruit_mlx90614.MLX90614(i2c)

ambientTemp = "{:.2f}".format(mlx.ambient_temperature)
targetTemp = "{:.2f}".format(mlx.object_temperature)

sleep(1)

if float(targetTemp) <= 37.9 and float(targetTemp) >= 32:
    print ("Temperature is fine, green light ahead")    
    print ("ambient temperature:", ambientTemp, " DEGREES CELSIUS")
    print ("target temperature:", targetTemp," DEGREES CELSIUS")
    GPIO.output(20,GPIO.HIGH)
    sleep(4)
    GPIO.output(20,GPIO.LOW)
    
elif float(targetTemp) <= 32:
    print ("Please walk closer to the sensor,temperature is too low, blue light shown")    
    print ("ambient temperature:", ambientTemp, " DEGREES CELSIUS")
    print ("target temperature:", targetTemp," DEGREES CELSIUS")
    GPIO.output(16,GPIO.HIGH)
    sleep(2)
    GPIO.output(16,GPIO.LOW)

else :
    print ("Temperature is too high,you may have a fever, red light stop")    
    print ("ambient temperature:", ambientTemp, " DEGREES CELSIUS")
    print ("target temperature:", targetTemp," DEGREES CELSIUS")
    GPIO.output(21,GPIO.HIGH)
    sleep(2)
    GPIO.output(21,GPIO.LOW)
