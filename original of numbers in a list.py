def  original(n,a):
    t=[]
    for i in a:
        if i not in t:
            t.append(i)
    return t


n=int(input())
a=list(map(int,input().split()))
l=original(n,a)
print(*l)
