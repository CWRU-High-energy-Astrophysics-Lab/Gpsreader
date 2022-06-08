import threading
from time import sleep
from unittest import TestCase

import numpy as np

from interface import Interface


class TestInterface(TestCase):
    def setUp(self) -> None:
        self.stop = False
        self.data = list(np.arange(1, 100))

        self.out = []
        self.intface = Interface()
        self.intface.outgoingmsg = list(np.arange(100, 200))
        self.intface.incomingmsg = list(np.arange(200, 300))
        th1 = threading.Thread(target=self.thread1)
        th2 = threading.Thread(target=self.thread2)
        th3 = threading.Thread(target=self.thread3)
        th1.start()
        th2.start()
        th3.start()
        th1.join()
    def test_all(self):
        self.out.sort()

        self.assertListEqual (list(np.arange(1,300)),self.out)


    def thread1(self):
        while (not self.stop):
            msg =self.intface.getoutgoing()
            if msg is not None:
                self.out.append(msg)

    def thread2(self):
        while (not self.stop):
            msg= self.intface.getincoming()
            if msg is not None:
                self.intface.addoutgoing(msg)

    def thread3(self):
        while self.data:
            self.intface.addincoming(self.data.pop())

        sleep(0.03)
        self.stop = True
