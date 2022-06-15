from serialinterface import  portrw
from gpsmain.interface import Interface
from serialinterface import pulse
from serialinterface import encoding
import threading
import time

if __name__ == '__main__':
    interface = Interface()
    port = "/dev/ttyUSB0"
    portthread = threading.Thread(target = portrw.serialthread, args = (port, interface))
    portthread.start()
    datathread = threading.Thread(target = pulse.sortmain, args = (interface,))
    datathread.start()  
    pulsethread = threading.Thread(target = pulse.detect_pulse)
    pulsethread.start()
    encoding.ha(1, interface)
    encoding.hb(1, interface)
    encoding.bb(1, interface)
    while(not interface.getTriggercond()):
        continue
    time.sleep(.1)
    encoding.bb(0, interface)
    portthread.join()
