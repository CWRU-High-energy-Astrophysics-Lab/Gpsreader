from gpsmain.interface import Interface
import time

def bb(parameter, interface):
    time.sleep(10)
    if parameter == 0:
        interface.addoutgoing(b'\x40\x40\x42\x62\x00\x20\x0d\x0a')
        print('Bb(00)')
    if parameter == 1:
        interface.addoutgoing(b'\x40\x40\x42\x62\x01\x21\x0d\x0a')
        print('Bb(01)')


def hn(parameter, interface):
    time.sleep(10)
    if parameter == 0:
        interface.addoutgoing(b'\x40\x40\x48\x6e\x00\x26\x0d\x0a')
        print('Hn(00)')
    if parameter == 1:
        interface.addoutgoing(b'\x40\x40\x48\x6e\x01\x27\x0d\x0a')
        print('Hn(01)')


def ha(parameter, interface):
    time.sleep(10)
    if parameter == 0:
        interface.addoutgoing(b'\x40\x40\x48\x61\x00\x29\x0d\x0a')
        print('Ha(00)')
    if parameter == 1:
        interface.addoutgoing(b'\x40\x40\x48\x61\x01\x28\x0d\x0a')
        print('Ha(01)')


def hb(parameter, interface):
    time.sleep(10)
    if parameter == 0:
        interface.addoutgoing(b'\x40\x40\x48\x62\x00\x2a\x0d\x0a')
        print('Hb(00)')
    if parameter == 1:
        interface.addoutgoing(b'\x40\x40\x48\x62\x01\x2b\x0d\x0a')
        print('Hb(01)')


def ek(parameter, interface):
    if parameter == 0:
        interface.addoutgoing(0x4040456B002E0d0a)
    if parameter == 1:
        interface.addoutgoing(0x4040456B012F0d0a)

