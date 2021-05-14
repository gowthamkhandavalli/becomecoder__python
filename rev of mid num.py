while 1:
    num=int(input())
    c=s=k=0
    temp=num
    while num:
        r=num%10
        num=num//10
        c+=1
    c=s=c-1
    num=temp
    p=num%10
    q=num//(10**c)
    while num:
        r=num%10
        num=num//10
        if c==s:
            r=q
        elif c==0:
            r=p
        k=k*10+r
        c-=1
    print(k)
