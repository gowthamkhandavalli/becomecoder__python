def palindrome(num):
    t=num
    s=0
    while num:
        r=num%10
        num=num//10
        s=s*10+r
    if s==t:
        return 1
    else:
        return 0


def palindrome_of_digits(data,n):
    c=0
    for i in range(len(data)):
        if palindrome(data[i]):
            c+=1
    return c

    
n=int(input())
data=list(map(int,input().split()))
print(palindrome_of_digits(data,n))

