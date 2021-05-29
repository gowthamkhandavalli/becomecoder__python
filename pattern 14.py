num=int(input())
for i in range(num,0,-1):
    if i%2==0:
        for j in range(i,0,-1):
            print(j,end="")
    else:
        for j in range(1,i+1):
            print(j,end="")
    print()
"""
o/p:
5
12345
4321
123
21
1
"""
