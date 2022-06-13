import time

import adafruit_ina219
import board
import busio

from gpsmain import interface
from serialinterface import sorting


def detect_pulse():
    i2c = busio.I2C(board.SCL, board.SDA)
    ina219 = adafruit_ina219.INA219(i2c)
    while True:
        count = 0
        trigger = 3.987
        voltages = [0, 0]
        while (count < 2):
            voltages.append(ina219.bus_voltage)
            timedetected = str(time.time_ns())
            count += 1
            time.sleep(.000001)
        if voltages[-1] > trigger and voltages[-2] < trigger:
            print('pulse detected at: ' + str(timedetected))


def sortmain(inter: interface.Interface):
    while True:
        message = inter.getincoming()
        # print(message)
        translation = sorting.sort_gps(message)
        if translation == None:
            continue
        else:
            print(translation)
