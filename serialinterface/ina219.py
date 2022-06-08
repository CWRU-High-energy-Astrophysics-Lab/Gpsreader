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
count = 0
voltages = []
while (count < 300):
    voltages.append(ina219.bus_voltage)
    print("Bus Voltage:   {} V".format(ina219.bus_voltage))
    count += 1
    time.sleep(.01)
x = np.arange(0, 300)

graph = plt.plot(x, voltages)
plt.show()