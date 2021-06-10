def fun(n,data,p,j):
    for i in range(j,n):
        if p<data[i]:
            return False
    return True

def leaderofnums(n,data):
    for i in range (n):
        if fun(n,data,data[i],i):
            a.append(data[i])
    return a

n=int(input())
a=[]
data=list(map(int,input().split()))
g=leaderofnums(n,data)
print(*g)
