import threading
class Interface():

    def __init__(self):
        self.incomingmsg = []
        self.outgoingmsg = []

        self.mutexout = threading.Lock()
        self.mutexin = threading.Lock()
    def addincoming(self,msg):
        self.mutexin.acquire(timeout=.5)
        self.incomingmsg.append(msg)
        self.mutexin.release()
    def getincoming(self):
        self.mutexin.acquire(timeout=.5)
        temp = None
        try:
            temp= self.incomingmsg.pop(0)

        except IndexError:
            pass
        self.mutexin.release()
        return temp
    def addoutgoing(self,msg):
        self.mutexout.acquire(timeout=.5)
        self.outgoingmsg.append(msg)
        self.mutexout.release()
    def getoutgoing(self):
        self.mutexout.acquire(timeout=.5)
        temp = None
        try:
            temp = self.outgoingmsg.pop(0)

        except IndexError:
            pass
        self.mutexout.release()
        return temp