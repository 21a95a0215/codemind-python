def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
def revers(num):
    rev =0
    while num>0:
        r=num%10
        rev=rev*10+r
        num=num//10
    return rev 
n= int(input())
n+=1
while True:
    if n==revers(n) and is_prime(n) == True :
        print(n)
        break
    n+=1    