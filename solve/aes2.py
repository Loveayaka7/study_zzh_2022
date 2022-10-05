from Crypto.Cipher import AES
from Crypto.Util.number import *
import os
'''
flag = open("flag").read()
key = os.urandom(16)
aes = AES.new(key, AES.MODE_ECB)
while True:
    name = input("Your name: ")
    msg = "Hello, " + name + "! Your flag is " + flag
    msg = msg.encode()
    msg += b"\x00" * (-len(msg) % AES.block_size)
    print(aes.encrypt(msg).hex())
'''
flag=''
name='123456789'
msg = "Hello, " + name
enc=''
#AES.block_size = 16,msg_min=22
print(len(msg),AES.block_size)

for i in range(2**15,2**16):
    k=long_to_bytes(i)
    print(len(k),k)
    aes = AES.new(k,AES.MODE_ECB)
    c=aes.encrypt(msg).hex()
    if c == enc[0:16]:
        print(k)
        break