#!/usr/bin/env python3

from ev3dev.ev3 import * #подключение модулей
from time import sleep

speed = 360 #скорость робота град/сек
us = UltrasonicSensor('in3')
assert us.connected
us.mode='US-DIST-CM'
units = us.units
barrierDistance = 20 # критическое расстояние до барьера
barrierCount = 0 #количество поворотов

motorLeft = LargeMotor('outA') #создаём левый мотор
assert motorLeft.connected, 'Connect left motor in  port A' # assert=if  не работает прога напишет подключите...
motorRight = LargeMotor('outB') #создаём правый мотор
assert motorRight.connected, 'Connect left motor in  por B'


#motorRight.run_to_rel_pos(position_sp=90, speed_sp=100)


#sleep(3)

Sound.beep()

motorLeft.run_forever(speed_sp = speed) #задали скорость -900.900
motorRight.run_forever(speed_sp = speed)

while True:
    distance = us.value()/10 # Переводим ММ в СМ
    if distance < barrierDistance:
        barrierCount += 1
        motorLeft.run_forever(speed_sp = speed/2) #задали скорость -900.900
        motorRight.run_forever(speed_sp = -speed/2)
        sleep(1.5)
        motorLeft.stop() #остановка робота
        motorRight.stop()
        distanceLeft = us.value()/10
        
        motorLeft.run_forever(speed_sp = -speed/2) #задали скорость -900.900
        motorRight.run_forever(speed_sp = speed/2)
        sleep(3)
        motorLeft.stop() #остановка робота
        motorRight.stop() 
        distanceRight = us.value()/10

        if distanceLeft > distanceRight:
            motorLeft.run_forever(speed_sp = speed/2) #задали скорость -900.900
            motorRight.run_forever(speed_sp = -speed/2)
            sleep(3)
            motorLeft.stop() #остановка робота
            motorRight.stop()
        if barrierCount > 3:
            break
        motorLeft.run_forever(speed_sp = speed) #задали скорость -900.900
        motorRight.run_forever(speed_sp = speed)
        
    sleep(0.1)
    
motorLeft.stop() #остановка робота
motorRight.stop()

