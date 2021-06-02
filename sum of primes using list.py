import math as m
def isprime(num):
    s=int(m.sqrt(num))
    for i in range(2,s+1):
        if num==1:
            return 0
        if num%i==0:
            return 0
    return 1 
def sum_of_prime(n,data):
    c=[]
    np=[]
    for i in data:
        if isprime(i):
            c.append(i)
            l=sum(c)
        else:
            np.append(i)
            p=sum(np)
    return l,p
            





n=int(input())
data=list(map(int,input().split()))
prime=sum_of_prime(n,data)
print(*prime)
