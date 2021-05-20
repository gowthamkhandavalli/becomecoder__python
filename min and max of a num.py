n=int(input())
mi=9
ma=c=k=0
while n:
    r=n%10
    n=n//10
    if r>ma:
        ma=r
    elif r<mi:
        mi=r
print(mi,ma)

    
