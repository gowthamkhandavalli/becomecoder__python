def harshad(n):
    t=n
    s=0
    while n:
        r=n%10
        n=n//10
        s=s+r
    n=t
    if n%s==0:
        return True
    else:
        return False



n=int(input())
print(harshad(n))
