from serialinterface import  portrw
from gpsmain.interface import Interface
import threading



if __name__ == '__main__':
    intface= Interface()
    port = "/dev/ttyUSB0"
    serialthread= threading.Thread(target=portrw.serialthread,args=(port,intface))
    serialthread.start()
    sortingthread=threading.Thread()