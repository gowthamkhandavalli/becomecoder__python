def sec_largest(n,data):
    s=max(data)
    for i in data:
        if i==s:
            data.remove(s)
    t=max(data)
    return t 
    

n=int(input())
data=list(map(int,input().split()))
print(sec_largest(n,data))
