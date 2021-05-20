def gen_fib(n):
    a,b,c=0,1,0
    if n==0 and n==1:
        return True
    f=2
    while True:
        c=a+b
        a=b
        b=c
        f+=1
        if c==n:
            print(f)
            break
        if c<n:
            print(False)
            break
n=int(input())
gen_fib(n)
