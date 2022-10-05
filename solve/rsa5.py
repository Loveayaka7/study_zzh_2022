import tools
from Crypto.Util.number import *
import gmpy2


'''
secret = bytes_to_long(os.urandom(31))

p = getPrime(128)
q = getPrime(128)
n = p * q
e = 65537

encrypted_secret = pow(secret, e, n)
print(encrypted_secret)
print(n)

if int(input()) == secret:
    print(open("flag").read())
else:
    print("Nope")

'''
#using yafu:  cmd='yafu-x64 factor(n)

p=178556620859081700450590416911437973931
q=225222292816448295012830274021125759941
encrypted_secret=16399968387144595342021113011539654329338615184871978426114669101565803207545
n = p * q
n0=40214931547439638254389026422523177048570881370392625263925732388377722098071

e = 65537
d = gmpy2.invert(e,(p-1)*(q-1))
t=pow(e*d,1,(p-1)*(q-1))
if __name__ == '__main__':
    print(n-n0,' ',t)
    sec=pow(encrypted_secret,d,n)
    print(sec)


