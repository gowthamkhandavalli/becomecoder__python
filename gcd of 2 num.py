a,b=map(int,input().split())
while 1:
    if a>b:
        a,b=b,a
    if b%a==0:
        print(a)
        break
    else:
        b=b%a
