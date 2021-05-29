n=int(input())
for i in range(1,n+1):
    for s in range (2,i+1):
        print(" ",end="")
    for j in range(n+1,i,-1):
        print("*",end="")
    print()
"""
o/p:
5
*****
 ****
  ***
   **
    *
"""
