def count(n):
    c=0
    while n:
        n=n//10
        c+=1
    return c
def arm(n,c):
    s=0
    while n:
        r=n%10
        n=n//10
        s=s+pow(r,c)
    return s

n=int(input())
c=count(n)
a=arm(n,c)
if n==a:
    print(" armstrong numnber")
else:
    print("not an armstrong number")
