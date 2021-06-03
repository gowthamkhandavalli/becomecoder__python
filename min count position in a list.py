def min_max(n,data): #13 11 12 11 11 21 
    a=data[0]
    l=[]
    c=0
    for i in data:
        if i==a:
            c+=1
        if i<a:
            a=i
            c=1
    l.append(a)
    l.append(c)
    for i in range(n):
        if data[i]==a:
            l.append(i)
    return l
    
            




    
n=int(input())
data=list(map(int,input().split()))
mi=min_max(n,data)
print(*mi)
