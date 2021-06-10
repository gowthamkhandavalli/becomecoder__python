def rotatelist(n,arr,r):
    r=r%n
    for j in range(r):
        for i in range(n-1):
            arr[i],arr[i+1]=arr[i+1],arr[i]
            

n=int(input())
r=int(input())
arr=list(map(int,input().split()))
rotatelist(n,arr,r)
print(*arr)
