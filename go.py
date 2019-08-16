# coding:utf-8
import RPi.GPIO as GPIO
import time
#绑定对应的引脚，来自于图纸
PWMA=18
AIN1 = 22
AIN2 = 27
PWMB=23
BIN1= 25
BIN2 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# 设置引脚为输出
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)
#电机
leftMotor = GPIO.PWM(PWMA, 100)
rightMotor = GPIO.PWM(PWMB, 100)
leftMotor.start(0)
rightMotor.start(0)

def forward(speed,runtime):
    leftMotor.ChangeDutyCycle(speed)
    GPIO.output(AIN1, True)#AIN1高电平则正转
    GPIO.output(AIN2, True)#如果为True则翻转
    rightMotor.ChangeDutyCycle(speed)
    GPIO.output(BIN1, True)
    GPIO.output(BIN2, True)
    time.sleep(runtime)

def backword(speed, backtime):
      leftMotor.ChangeDutyCycle(speed)
      GPIO.output(AIN2, True)  # AIN2
      GPIO.output(AIN1, False)  # AIN1
      rightMotor.ChangeDutyCycle(speed)
      GPIO.output(BIN2, True)  # BIN2
      GPIO.output(BIN1, False)  # BIN1
      time.sleep(backtime)

def turnLeft(speed, lefttime):
    leftMotor.ChangeDutyCycle(speed)
    GPIO.output(AIN1, False)
    GPIO.output(AIN2, True)
    rightMotor.ChangeDutyCycle(speed)
    GPIO.output(BIN1, True)
    GPIO.output(BIN2, False)
    time.sleep(lefttime)

#右转弯函数
def turnRight(speed, righttime):
    leftMotor.ChangeDutyCycle(speed)
    GPIO.output(AIN1, True)
    GPIO.output(AIN2, False)
    rightMotor.ChangeDutyCycle(speed)
    GPIO.output(BIN1, False)
    GPIO.output(BIN2, True)
    time.sleep(righttime)

if __name__ == '__main__':
    try:
         while True:
             forward(50,3)
    except KeyboardInterrupt:
         GPIO.cleanup()