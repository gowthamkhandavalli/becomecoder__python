n=int(input())
for i in range(1,n+1):
    for s in range (i,n):
        print(" ",end="")
    for j in range(1,2*i):
        print(j,end="")
    print()
