def reverse(n,s=0,r=0):
    if n==0:
        print(s)
        return s
    r=n%10
    n=n//10
    s=s*10+r
    reverse(n,s,r)


n=int(input())
reverse(n)
