import threading


class Interface():


    def __init__(self):
        self.__incomingmsg = []
        self.__outgoingmsg = []
        self.__todisplay = []
        self.__triggercond=False
        self.__stop = False
        self.__mutexout = threading.Lock()
        self.__mutexin = threading.Lock()
        self.__mutexstop = threading.Lock()
        self.__mutexdisplay = threading.Lock()
        self.__mutextrig = threading.Lock()

    def addincoming(self, msg):
        self.__mutexin.acquire(timeout=.5)
        self.__incomingmsg.append(msg)
        self.__mutexin.release()

    def getincoming(self):
        self.__mutexin.acquire(timeout=.5)
        temp = None
        try:
            temp = self.__incomingmsg.pop(0)

        except IndexError:
            pass
        self.__mutexin.release()
        return temp

    def addoutgoing(self, msg):
        self.__mutexout.acquire(timeout=.5)
        self.__outgoingmsg.append(msg)
        self.__mutexout.release()

    def getoutgoing(self):
        self.__mutexout.acquire(timeout=.5)
        temp = None
        try:
            temp = self.__outgoingmsg.pop(0)

        except IndexError:
            pass
        self.__mutexout.release()
        return temp

    def getstop(self) -> bool:
        self.__mutexstop.acquire()
        msg = self.__stop
        self.__mutexstop.release()
        return msg
    def getdisplaymsg(self):
        self.__mutexdisplay.acquire(timeout=.5)
        temp = None
        try:
            temp = self.__todisplay.pop(0)

        except IndexError:
            pass
        self.__mutexdisplay.release()
        return temp

    def adddisplaymsg(self, msg):
        self.__mutexdisplay.acquire(timeout=.5)
        self.__todisplay.append(msg)
        self.__mutexdisplay.release()

    def getTriggercond(self):
        self.__mutextrig.acquire(timeout=.5)
        temp = self.__triggercond
        self.__mutextrig.release()
        return temp
    def setTriggercond(self,trig):
        self.__mutextrig.acquire(timeout=.5)
        self.__triggercond=trig
        self.__mutextrig.release()
