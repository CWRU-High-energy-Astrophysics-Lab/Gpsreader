import decoding
def sort_gps_data(array):
    ha_list = []
    hn_list = []
    hb_list = []
    bb_list = []
    ek_list = []
    output_list = []
    for i in range(len(array)):
        if array[i][0:3] == 0x4040:
            if array[i][4:7] == 0x4861:
                ha_list.append(array[i])
                output_list.append(decoding.Ha(array[i]))
            elif array[i][4:7] == 0x486E:
                hn_list.append(array[i])
                output_list.append(decoding.Hn(array[i]))
            elif array[i][4:7] == 0x4862:
                hb_list.append(array[i])
                output_list.append(decoding.Hb(array[i]))
            elif array[i][4:7] == 0x4262:
                bb_list.append(array[i])
                output_list.append(decoding.Bb(array[i]))
            elif array[i][4:7] == 0x456B:
                ek_list.append(array[i])
                output_list.append(decoding.Ek(array[i]))
