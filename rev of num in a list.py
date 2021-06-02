def rev(num):
    s=0
    while num:
        r=num%10
        num=num//10
        s=s*10+r
    return s


def rev_of_digits(data,n):
    for i in data:
       for i in range(len(data)):
           data[i]=rev(data[i])
       return data




    
n=int(input())
data=list(map(int,input().split()))
rev_of_digits(data,n)
print(*data)
