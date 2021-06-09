def maxofones(n,data):
    c=0
    count=0
    for i in range(n):
        if data[i]==1:
            c+=1
        else:
            if c>count:
                count=c
            c=0
    return max(c,count)

n=int(input())
data=list(map(int,input().split()))
print(maxofones(n,data))
