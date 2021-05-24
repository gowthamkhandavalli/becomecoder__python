def disarium(n):
    t=n
    c=0
    s=0
    while n:
        n=n//10
        c+=1
    n=t
    while n:
        r=n%10
        n=n//10
        s=s+pow(r,c)
        c-=1
    if t==s:
        return True
    else:
        return False


n=int(input())
print(disarium(n))

