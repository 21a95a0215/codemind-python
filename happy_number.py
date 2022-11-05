def happy(a):
    s=0
    if a<=9:
        return a==1 or a==7
    while a:
        r=a%10
        s+=r**2
        a=a//10
    return happy(s) 
a=int(input())
print(happy(a))
        