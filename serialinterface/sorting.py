from serialinterface import decodinggps

def sort_gps(message):
    try:
        if message[0] == '48':
            if message[1] == '61':
                return decodinggps.Ha(message)
            elif message[1] == '6e':
                return decodinggps.Hn(message)
            elif message[1] == '62':
                return decodinggps.Hb(message)
        elif message[0] == '42':
            return decodinggps.Bb(message)
        elif message[0] == '45':
            return decodinggps.Ek(message)

    except TypeError:
        return
    except IndexError:
        return
