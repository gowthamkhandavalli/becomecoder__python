import math as m
a=int(input())
c=2
s=int(m.sqrt(a))
for i in range (2,s+1):
    if a%i==0:
        if i==a//i:
            c+=1
        else:
            c+=2
print(c)

        
        
