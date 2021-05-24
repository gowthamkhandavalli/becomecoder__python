a,b=map(int,input().split())
t=2
res=1
while 1:
    if a%t==0 and b%t==0:
         res=res*t
         a=a//t
         b=b//t
    else:
        t+=1
    if a<t or b<t:
        break
print(res*a*b)
        
