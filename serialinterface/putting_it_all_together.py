import portrw.py as port
import sorting.py as sorting
import encoding.py as encoding
import decoding.py as decoding

import board
import busio
import adafruit_ina219
import time
import matplotlib.pyplot as plt
import numpy as np

# startup the ADC
i2c = busio.I2C(board.SCL, board.SDA)
ina219 = adafruit_ina219.INA219(i2c)

# set initial values for the voltage vector and
trigger = 5
    if voltages[end] > trigger and voltages[end - 1] < trigger:
        encoding.hn(1)
time.sleep(.01)

x = np.arange(0, 300)
graph = plt.plot(x, voltages)
plt.show()

port.serialthread