def sum(num):
    s=0
    while num:
        r=num%10
        num=num//10
        s=s+r
    return s


def sum_of_digits(data,n):
    for i in data:
       for i in range(len(data)):
           data[i]=sum(data[i])
       return data




    
n=int(input())
data=list(map(int,input().split()))
sum_of_digits(data,n)
print(*data)
