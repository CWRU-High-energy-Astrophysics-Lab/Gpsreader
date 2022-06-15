import time

import adafruit_ina219
import board
import busio

from gpsmain.interface import Interface
from serialinterface import sorting


def detect_pulse(interfac:Interface):
    i2c = busio.I2C(board.SCL, board.SDA)
    ina219 = adafruit_ina219.INA219(i2c)
    predictedpulse = 0
    lastpulse = 0
    while True:
        count = 0
        trigger = 4.12
        voltages = [0, 0]
        while (count < 2):
            voltages.append(ina219.bus_voltage)
            timedetected = time.time_ns()
            count += 1
            time.sleep(.000001)

        if voltages[-1] > trigger and voltages[-2] < trigger and timedetected - lastpulse > 500000000:
            interfac.setTriggercond(True)
            print('pulse detected at:  ' + str(timedetected))
            lastpulse = timedetected
            predictedpulse = lastpulse + 1000000000

        if timedetected - predictedpulse > 100100000:
            print('predicted pulse at: ' + str(predictedpulse))
            predictedpulse += 1000000000



def sortmain(inter:Interface):
    while True:
        message = inter.getincoming()
        # print(message)
        translation = sorting.sort_gps(message)
        if translation == None:
            continue
        else:
            print(translation)
