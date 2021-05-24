def lcm(a,b):
    t=2
    res=1
    while a>=t and b>=t:
        a=a//t
        b=b//t
        res=res*t
    else:
        t+=1
    return res*a*b

a,b=map(int,input().split())
print(lcm(a,b))
