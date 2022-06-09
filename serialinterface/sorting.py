import decoding
from gpsmain.interface import Interface
def sort_gps_data(msg:list):

        if msg[0:3] == 0x4040:
            if msg[4:7] == 0x4861:

                return msg[0:7].extend(decoding.Ha(msg))
            elif msg[4:7] == 0x486E:
                return msg[0:7].extend(decoding.Hn(msg[7::]))
            elif msg[4:7] == 0x4862:

                return msg[0:7].extend(decoding.Hb(msg[7::]))
            elif msg[4:7] == 0x4262:

                return msg[0:7].extend(decoding.Bb(msg[7::]))
            elif msg[4:7] == 0x456B:
               return msg[0:7].extend(decoding.Ek(msg[7::]))
        else:
            return msg

def sortthread(intface:Interface):
    while not intface.getstop():
        msg = intface.getincoming()
        sortedmsg = sort_gps_data(msg)
        intface.adddisplaymsg(sortedmsg)
