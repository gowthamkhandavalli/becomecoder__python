def  original(n,a):
    t=[]
    c=0
    for i in a:
        if i not in t:
            t.append(i)
    for i in range(len(t)):
        if a[i]==t[i]:
            c+=1
    print(t)
    return c
        


n=int(input())
a=list(map(int,input().split()))
c=original(n,a)
print(c)
