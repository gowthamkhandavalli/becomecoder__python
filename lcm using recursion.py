t=2
def lcm(a,b):
    global t
    if a%b==0 or b%a==0:
        if a>b:
            return a
        if b<a:
            return b
    if t>=a or t>=b:
        return a*b
    if a%t==0 and b%t==0:
        return t*lcm(a//t,b//t)
    else:
        t+=1
        return t*lcm(a//t,b//t)

a,b=map(int,input().split())
t=lcm(a,b)
print(t)
