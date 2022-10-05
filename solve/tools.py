from Crypto.Util.number import *
import gmpy2




def long_to_flag(num,ignore=0):
    if ignore:
        flag = long_to_bytes(num).decode(errors='ignore')
    else:
        flag = long_to_bytes(num).decode()
    return flag

def crt(b,m):          # b,m:list
    #判断是否互素
    for i in range(len(m)):
        for j in range(i+1,len(m)):
            if gmpy2.gcd(m[i],m[j]) != 1:
                print("m中含有不是互余的数")
                return -1
    #乘积
    M = 1
    for i in range(len(m)):
        M *= m[i]
    #求M/mi
    Mm = []
    for i in range(len(m)):
        Mm.append(M // m[i])
    #求Mm[i]的乘法逆元
    Mm_ = []
    for i in range(len(m)):
        _,a,_ = gmpy2.gcdext(Mm[i],m[i])
        Mm_.append(int(a % m[i]))
    #求MiM'ibi的累加
    y = 0
    for i in range(len(m)):
        print(Mm[i] * Mm_[i] * b[i])
        y += (Mm[i] * Mm_[i] * b[i])
    y = y % M
    return y

def phi(a):
    res = a
    for i in range(2, int(a**0.5)+1):
        if a % i == 0: res = (res//i) * (i-1)
        while a % i == 0:
            a //= i
    if a > 1: res = (res//a) * (a-1)
    return res

def lagrange(x:list,y:list,n,mod,num):
    l=0
    for i in range(n+1):
        ln=1
        for j in range(n+1):
            if j != i:
                ln*=(num-x[j])*inverse(x[i]-x[j],mod)
        l+=y[i]*ln
    return l




