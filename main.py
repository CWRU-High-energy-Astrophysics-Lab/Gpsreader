from serialinterface import  portrw
from gpsmain.interface import Interface
from serialinterface import pulse
from serialinterface import encoding
import threading

if __name__ == '__main__':
    interface = Interface()
    port = "/dev/ttyUSB0"
    portthread = threading.Thread(target = portrw.serialthread, args = (port, interface))
    portthread.start()
    datathread = threading.Thread(target = pulse.sortmain, args = (interface,))
    datathread.start()  
    pulsethread = threading.Thread(target = pulse.detect_pulse)
    pulsethread.start()
    bbthread = threading.Thread(target = encoding.bb, args = (0, interface))
    bbthread.start()
    hbthread = threading.Thread(target = encoding.hb, args = (1, interface))
    hbthread.start()
    hathread = threading.Thread(target = encoding.ha, args = (1, interface))
    hathread.start()
    hnthread = threading.Thread(target = encoding.hn, args = (1, interface))
    hnthread.start()
    portthread.join()
