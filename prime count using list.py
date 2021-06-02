import math as m
def isprime(num):
    s=int(m.sqrt(num))
    for i in range(2,s+1):
        if num%i==0:
            return 0
    return 1 
def primecount(n,data):
    c=0
    for i in data:
        if isprime(i):
            c+=1
    return c
            





n=int(input())
data=list(map(int,input().split()))
pc=primecount(n,data)
print(pc)
