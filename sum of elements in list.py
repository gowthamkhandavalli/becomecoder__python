def total_marks(n,data):
    r=0
    for i in data:
        r+=i
    return r

n=int(input())
data=list(map(int,input().split()))
total=total_marks(n,data)
print(total)
