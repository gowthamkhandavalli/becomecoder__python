import math as m
def isprime(num):
    s=int(m.sqrt(num))
    for i in range(2,s+1):
        if num==1:
            return 0
        if num%i==0:
            return 0
    return 1 
def findprime(n,data):
    c=[]
    np=[]
    for i in data:
        if isprime(i):
            c.append(i)
        else:
            np.append(i)
    return c,np
            





n=int(input())
data=list(map(int,input().split()))
prime=findprime(n,data)
print(*prime)
