from Crypto.Cipher import AES
from Crypto.Util.number import *
import tools

'''
flag = open("flag").read().encode()
key = b"ThisismyAESkey:)"
aes = AES.new(key, AES.MODE_ECB)
msg = b"Flag is:  " + flag
print(aes.encrypt(msg).hex())

'''

key = b"ThisismyAESkey:)"
c=long_to_bytes(int('0xfef29ccb541199b860a134e0e87c59d73bd312f7671107e184ee2382b475922a5ff7e713e0a30fe030ef15c4fd4fde52',16))


aes=AES.new(key,AES.MODE_ECB)
msg=aes.decrypt(c)
flag=msg.decode()
print(flag)
