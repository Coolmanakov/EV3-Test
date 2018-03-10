#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep

speed = 360 #скорость робота град/сек
gy = GyroSensor('in1')
assert gy.connected, ("Подключите гироскоп в порт 1")

motorLeft = LargeMotor('outA') #создаём левый мотор
assert motorLeft.connected, 'Connect left motor in  port A' # assert=if  не работает прога напишет подключите...
motorRight = LargeMotor('outB') #создаём правый мотор
assert motorRight.connected, 'Connect left motor in  por B'



gy.mode='GYRO-ANG'                   # Переключаем гироскоп в режим измерения угла
units = gy.units                    # Вернет 'deg' в режиме измерения угла


zeroAngle =  gy.value()

def RotateGyroscope (speed, angle):
    if angle > 0:
        motorLeft.run_forever(speed_sp = -speed) #задали скорость -900.900
        motorRight.run_forever(speed_sp = speed)
        while gy.value() - zeroAngle < angle:
            #print(str(angle) + " " + units)
            sleep(0.1)
    else:
        motorLeft.run_forever(speed_sp = speed) #задали скорость -900.900
        motorRight.run_forever(speed_sp = -speed)
        while gy.value() - zeroAngle > angle :
            sleep(0.1)
    motorLeft.stop() #остановка робота
    motorRight.stop()
    

RotateGyroscope(900, -90)
sleep(5)
RotateGyroscope(900, 90)
