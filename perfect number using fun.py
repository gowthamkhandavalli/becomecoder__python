import math as m
def isperfect(n):
    r=1
    s=int(m.sqrt(n))
    for i in range(2,s+1):
        if n%i==0:
            r+=i+n//i
        return r==n

n=int(input())
print(isperfect(n))

