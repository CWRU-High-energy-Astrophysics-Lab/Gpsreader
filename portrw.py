import threading
import time
import serial

from gpsmain.interface import Interface

def serialthread(bus, intface:Interface):
    port = serial.Serial(bus)

    response = []
    while threading.main_thread().is_alive():
        next2byte = port.read(2)
        if b'@@' == next2byte:
            print('serial message recieved at: ' + str(time.time_ns()))
            #print(response)
            intface.addincoming(response)
            response = []

        else:
            #print(next2byte.hex())
            response.append( next2byte.hex()[0:2])
            response.append( next2byte.hex()[2::])

        try:
            out = intface.getoutgoing()
            port.write(out)
        except:
            continue