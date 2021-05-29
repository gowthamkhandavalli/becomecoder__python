num=int(input())
for i in range(1,num+1):
        for j in range(1,i+1):
            if j%2==0:
                print(0,end="")
            else:
                print(1,end="")
        print()
    
"""
o/p:
5
1
10
101
1010
10101
"""
