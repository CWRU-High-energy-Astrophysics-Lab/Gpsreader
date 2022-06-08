import decoding
def sort_gps(message):
   if message[0:3] == 0x4040:
        if message[4:7] == 0x4861:
            return decoding.Ha(message)
        elif message[4:7] == 0x486E:
            return decoding.Hn(message)
        elif message[4:7] == 0x4862:
            return decoding.Hb(message)
        elif message[4:7] == 0x4262:
            return decoding.Bb(message)
        elif message[4:7] == 0x456B:
            return decoding.Ek(message)