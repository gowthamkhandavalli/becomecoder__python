def supermax_min(data,n):
    mn=min(data)
    mx=max(data)
    s1,s2=0,0
    while mn:
        r=mn%10
        mn=mn//10
        s1=s1*10+r
    while mx:
        r=mx%10
        mx=mx//10
        s2=s2*10+r
    print(s1,s2)
    for i in data:
        if i>s2:
            res=0
        else:
            res=1
    if res==1:
        print("super max")
    else:
        print("not a super max")
    for i in  data:
        if i<s1:
            res=0
        else:
            res=1
    if res==1:
        print("super min")
    else:
        print("not a super min")
            



n=int(input())
data=list(map(int,input().split()))
supermax_min(data,n)
