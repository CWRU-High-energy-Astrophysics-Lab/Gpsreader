from serialinterface import portrw as port
from serialinterface import Sorting_2 as sorting
from Gpsreader import interface
from serialinterface import encoding as encoding
import board
import busio
import adafruit_ina219
import time
import numpy as np

def detect_pulse():
    i2c = busio.I2C(board.SCL, board.SDA)
    ina219 = adafruit_ina219.INA219(i2c)

    count = 0
    trigger = 5
    voltages = []
    while (count < 2):
        voltages.append(ina219.bus_voltage)
        count += 1
        time.sleep(.001)
    if voltages[-1] > trigger and voltages[-2] < trigger:
        encoding.hn(1)

while True:
    message = interface.getincoming()
    translation = sorting.sort_gps(message)
    print(translation)