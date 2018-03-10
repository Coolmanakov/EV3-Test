#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep


speed = 360
cl = ColorSensor('in4')
assert cl.connected, "Подключите датчик цвета EV3 in 2"

motorLeft = LargeMotor('outD') #создаём левый мотор
assert motorLeft.connected, 'Connect left motor in  port D' # assert=if  не работает прога напишет подключите...
motorRight = LargeMotor('outC') #создаём правый мотор
assert motorRight.connected, 'Connect right motor in  por C'

us = UltrasonicSensor('in3')
assert us.connected

ts = TouchSensor('in2')
summ = 0
barrierDistance = 30 # критическое расстояние до барьера
us.mode='US-DIST-CM'
units = us.units
time = 0

def speedGo (speed):
    motorLeft.run_forever(speed_sp = speed) #задали скорость -900.900
    motorRight.run_forever(speed_sp = speed)
def speedTurn(speed):
    motorLeft.run_forever(speed_sp = speed/2) #задали скорость -900.900
    motorRight.run_forever(speed_sp = -speed/2)
    
                         # Переводим датчик в режим измерения освещенности
cl.mode='COL-REFLECT'    # в этом режиме датчик выдает освещенность 0..100%

while not ts.value():
    sleep(0.1)
    
colorBlack = cl.value()    #получаем значение черного
print(colorBlack)
    
sleep(3)

while not ts.value():       #крутимся в цикле пока не будт нажата какая-либо кнопка на блоке
    sleep(0.1)
    
colorWhite = cl.value()     #получаем значение белого
print(colorWhite)
    
summ = (colorWhite + colorBlack) / 2
print(summ)

sleep(2)

while True:
    distance = us.value()/10 # Переводим ММ в СМ
    print(distance)
    sleep(0.1)
    speedTurn(speed)
    print(1111111)
    
    if distance < barrierDistance:
        motorLeft.stop() #остановка робота
        motorRight.stop()
        print(2222222)
        sleep(0.5)
        speedGo(speed)
        
            
        
        while cl.value() > summ:
            print(3333333333)
            sleep(0.1)
            
            
        
        motorLeft.stop() #остановка робота
        motorRight.stop()
        sleep(0.5)
        
        speedGo(-speed)
        print(44444444444)
        sleep(5)
                   
        
motorLeft.stop() #остановка робота
motorRight.stop()    
