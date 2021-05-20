def seq(a):
    print(a)
    while a!=1:
        if a%2:
            a=(3*a)+1
            print(a)
        else:
            a=a//2
            print (a)



a=int(input())
seq(a)
