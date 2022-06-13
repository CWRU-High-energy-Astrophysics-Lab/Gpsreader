from serialinterface import  portrw
from gpsmain.interface import Interface
from serialinterface import pulse
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
    portthread.join()
