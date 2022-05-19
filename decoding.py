import numpy as np

def twosComplement_hex(hexval, length):
    bits = 16
    val = int(hexval, bits)
    if val & (1 << (length-1)):
        val -= 1 << length
    return val

def Bb(hex):
    n = int(hex[0], 16)
    i = np.zeros(n)
    dd = np.zeros(n)
    e = np.zeros(n)
    aa = np.zeros(n)
    s = np.zeros(n)
    iddeaas = np.zeros(n)
    for j in range(n):
        i[j] = int(hex[1], 16)
        dd[j] = int(hex[2]+hex[3], 16)
        e[j] = int(hex[4], 16)
        aa[j] = int(hex[5]+hex[6], 16)
        s[j] = int(hex[7], 16)
        iddeaas[j] = (i[j], dd[j], e[j], aa[j], s[j])
    return n, iddeaas

def Ha(hex):
    M = int(hex[0], 16)
    d = int(hex[1], 16)
    yy = int(hex[2]+hex[3], 16)
    h = int(hex[4], 16)
    m = int(hex[5], 16)
    s = int(hex[6], 16)
    ffff = int(hex[7]+hex[8]+hex[9]+hex[10], 16)
    aaaa = twosComplement_hex(hex[11]+hex[12]+hex[13]+hex[14], 32)
    oooo = twosComplement_hex(hex[15]+hex[16]+hex[17]+hex[18], 32)
    hhhh = twosComplement_hex(hex[19]+hex[20]+hex[21]+hex[22], 32)
    mmmm = int(hex[23]+hex[24]+hex[25]+hex[26], 16)
    AAAA = twosComplement_hex(hex[27]+hex[28]+hex[29]+hex[30], 32)
    OOOO = twosComplement_hex(hex[31]+hex[32]+hex[33]+hex[34], 32)
    HHHH = twosComplement_hex(hex[35]+hex[36]+hex[37]+hex[38], 32)
    MMMM = int(hex[39]+hex[40]+hex[41]+hex[42], 16)
    VV = int(hex[43]+hex[44], 16)
    vv = int(hex[45]+hex[46], 16)
    hh = int(hex[47]+hex[48], 16)
    dd = int(hex[49]+hex[50], 16)
    n = int(hex[51], 16)
    t = int(hex[52], 17)
    i_ = np.zeros(12)
    m_ = np.zeros(12)
    s_ = np.zeros(12)
    I_ = np.zeros(12)
    dd_ = np.zeros(12)
    imsidd = np.zeros((12, 5))
    for j in range((0,11)):
        i_[j] = int(hex[53+8*j], 16)
        m_[j] = int(hex[54+8*j], 16)
        s_[j] = int(hex[55+8*j], 16)
        I_[j] = int(hex[56+8*j], 16)
        dd_[j] = format(int(hex[57+8*j]+hex[58+8*j], 16), '0>42b')
        imsIdd[j] = [i[j], m[j], s[j], I[j], DD[j]]
    ss = format(int(hex[146]+hex[147], 16), '0>42b')
    rr = format(int(hex[148]+hex[149], 16), '0>42b')
    cc = twosComplement_hex(hex[150]+hex[151], 16)
    OoOo = int(hex[152]+hex[153]+hex[154]+hex[155], 16)
    TT = twosComplement_hex(hex[156]+hex[157], 16)
    u = format(int(hex[158], 16), '0>42b')
    S = hex[159]
    if (S == '00'):
        S = '+'
    if (S == 'FF'):
        S = '-'
    H = int(hex[160], 16)
    M = int(hex[161], 16)
    vvvvvv = hex[162]+hex[163]+hex[164]+hex[165]+hex[166]+hex[167]
    C = hex[168]
    return M, d, yy, h, m, s+ffff*1e-9

    def Hb(hex):
    M = int(hex[0], 16)
    d = int(hex[1], 16)
    yy = int(hex[2]+hex[3], 16)
    h = int(hex[4], 16)
    m = int(hex[5], 16)
    s = int(hex[6], 16)
    ffff = int(hex[7]+hex[8]+hex[9]+hex[10], 16)
    aaaa = twosComplement_hex(hex[11]+hex[12]+hex[13]+hex[14], 32)
    oooo = twosComplement_hex(hex[15]+hex[16]+hex[17]+hex[18], 32)
    hhhh = twosComplement_hex(hex[19]+hex[20]+hex[21]+hex[22], 32)
    mmmm = int(hex[23]+hex[24]+hex[25]+hex[26], 16)
    VV = int(hex[27]+hex[28], 16)
    vv = int(hex[29]+hex[30], 16)
    hh = int(hex[31]+hex[32], 16)
    dd = int(hex[33]+hex[34], 16)
    n = int(hex[35], 16)
    t = int(hex[36], 17)
    ss = format(int(hex[37]+hex[38], 16), '0>42b')
    rr = format(int(hex[39]+hex[40], 16), '0>42b')
    vvvvvv = hex[41]+hex[42]+hex[43]+hex[44]+hex[45]+hex[46]
    C = hex[47]
    return M, d, yy, h, m, s+ffff*1e-9

    def Hn(hex):
    p = int(hex[0], 16)
    y = int(hex[1], 16)
    s = int(hex[2], 16)
    r = int(hex[3], 16)
    vvvv = int(hex[4]+hex[5]+hex[6]+hex[7], 16)
    ee = int(hex[8]+hex[9], 16)
    n = twosComplement_hex(hex[10], 8)
    s = np.zeros(12)
    ffff = np.zeros(12)
    sffff = np.zeros(12)
    for j in range(12):
        s[j] = int(hex[11+5*j], 16)
        ffff[j] = int(hex[12+5*j]+hex[13+5*j]+hex[14+5*j]+hex[15+5*j], 16)
        sffff[j] = (s[j], ffff[j])
    C = hex[76]
    print('Sawtooth =', n, '   One-Sigma Accuracy =', ee)
