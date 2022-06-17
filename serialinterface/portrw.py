import threading
import time
import serial

from gpsmain.interface import Interface

def serialthread(bus, intface:Interface):
    port = serial.Serial(bus)
    
    response = []
    while threading.main_thread().is_alive():
        byte1 = port.read(1)
#         print(byte1)
        if b'@' == byte1:
            nextbyte = port.read()
#             print(nextbyte)
                if nextbyte == b'@':
                    print('serial message recieved at: ' + str(time.time_ns()))
                    intface.addincoming(response)
                    print(response)
                    response = []
                else:
                    response.append( byte1.hex())
                    response.append( nextbyte.hex())
                

        else:
            #print(next2byte.hex())
            response.append( byte1.hex())

        try:
            out = intface.getoutgoing()
            if out is not None: 
                port.write(out)
                port.send_break
        except:
            continue