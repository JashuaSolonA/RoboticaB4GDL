import RPi.GPIO as GPIO
import time

servo1 = 11
servo2 = 12
servo3 = 13
servo4 = 14

GPIO.setmode(GPIO.BOARD)

GPIO.setup(servo1,GPIO.OUT)
GPIO.setup(servo2,GPIO.OUT)
GPIO.setup(servo3,GPIO.OUT)
GPIO.setup(servo4,GPIO.OUT)

servo_1  = GPIO.PWM(servo1,50)
servo_2  = GPIO.PWM(servo2,50) 
servo_3  = GPIO.PWM(servo3,50)  
servo_4  = GPIO.PWM(servo4,50)  

servo_1.start(0)
servo_2.start(0)
servo_3.start(0)
servo_4.start(0)


def angulos(q1,q2,q3,q4):
    angle1 = q1/18 + 2
    angle2 = q2/18 + 2
    angle3 = q3/18 + 2 
    angle4 = q4/18 + 2

    servo1.ChangeDutyCycle(angle1)
    time.sleep(0.5)
    servo2.ChangeDutyCycle(angle2)
    time.sleep(0.5)
    servo3.ChangeDutyCycle(angle3)
    time.sleep(0.5)
    servo4.ChangeDutyCycle(angle4)
    time.sleep(0.5)    