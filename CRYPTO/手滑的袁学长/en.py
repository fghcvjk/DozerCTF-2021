import os
from Crypto.Util import *
from Crypto.Util.strxor import *
from Crypto.Cipher import AES


answer = open('FLAG1/flag', 'rb').read()
print(len(answer))

def Function_enc(msg, key, p_2, c_2):
    msg = Padding.pad(msg, 16)
    struct = [msg[i:i+16] for i in range(0, len(msg), 16)]

    out = b''
    for p in struct:
        c = strxor(p, c_2)
        c = AES.new(key, AES.MODE_ECB).encrypt(c)

        out += strxor(p_2, c)
        c_2 = c
        p_2 = p

    return out

KEY = os.urandom(16)
msg = 'I do not care the result' + KEY.hex()
text = Function_enc(msg.encode(), KEY, answer[:16], answer[16:])

print('key = ' + KEY.hex())
print('cipher =' + text.hex())