from Crypto.Cipher import AES
import hashlib
from secrets import flag,secret

assert len(secret)==10
assert secret[:2]=='78'
init_key = 'look_at_here!you_may_need_it!!'
NUM = 640
fl4g='fl4g{I_HaTe_The_DaMn_FaKe_FlAg}'

def pad(s):
    return s + (16 - (len(s) % 16)) * '\x11'

def genKeys(init):
    keys=[]
    for _ in range(NUM):
        key = hashlib.md5(init).hexdigest()
        keys.append(key)
        init = key
    return keys

def extend(s):
    s1 = [ int(s[2 * i], 16) for i in range(len(s)//2)]
    s2 = [ int(s[2 * i + 1], 16) for i in range(len(s)//2)][::-1]
    part1 = ''.join(map(lambda x : '{:>04}'.format(bin(x)[2:]), s1)) * 16
    part2 = ''.join(map(lambda x : '{:>04}'.format(bin(x)[2:]), s2)) * 16
    return part1 + part2

keys = genKeys(init_key)
ex = extend(secret)

def encrypt(msg):
    for i,k in enumerate(keys):
        b = int(ex[i]) & 1
        key = k[ b * 16 : (b + 1) * 16]
        aes = AES.new(key, AES.MODE_ECB)
        msg = aes.encrypt(msg)
    return msg


print encrypt(pad(fl4g)).encode('hex')
print encrypt(pad(flag)).encode('hex')
