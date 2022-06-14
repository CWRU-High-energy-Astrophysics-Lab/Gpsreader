import board
import busio
import adafruit_ina219
import time
import matplotlib.pyplot as plt
import numpy as np

# startup the ADC
i2c = busio.I2C(board.SCL, board.SDA)
ina219 = adafruit_ina219.INA219(i2c)

# while (count < 300):
#     voltages.append(ina219.bus_voltage)
#     print("Bus Voltage:   {} V".format(ina219.bus_voltage))
#     count += 1
#     time.sleep(.01)
# time.gmtime(0)
# x = np.arange(0, 300)
# graph = plt.plot(x, voltages)
# plt.show()

while True:
    count = 0
    trigger = 4.112
    voltages = [0,0]
    while (count < 2):
            voltages.append(ina219.bus_voltage)
            timedetected = str(time.time_ns())
            count += 1
            time.sleep(.01)
    if voltages[-1] > trigger and voltages[-2] < trigger:
            print('pulse detected at: ' + str(timedetected))
