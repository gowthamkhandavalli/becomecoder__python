def maxsort(n,data):
    f=0
    s=1
    for i in range(n-1):
        if data[i]<data[i+1]:
            f+=1
        else:
            if f+1>s:
                s=f+1
            f=0
    if f+1>s:
        return f+1
    return s

n=int(input())
data=list(map(int,input().split()))
print(maxsort(n,data))
