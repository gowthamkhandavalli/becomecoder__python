def even_odd(n,data):
    r,c=0,0
    for i in data:
        if i%2==0:
            c+=1
        else:
            r+=1
    return c,r

n=int(input())
data=list(map(int,input().split()))
count=even_odd(n,data)
print(count)
