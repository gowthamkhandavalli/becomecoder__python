def min_max(n,data):
    mi=data[0]
    ma=data[0]
    for i in data:
        if ma<i:
            ma=i
        if mi>i:
            mi=i
    return ma,mi




    
n=int(input())
data=list(map(int,input().split()))
mi,ma=min_max(n,data)
print(*min_max(n,data))
