def palindrom(n):
    s=0
    while n>0:
        x=n%10
        s=s*10+x
        n=n//10
    return s
a= int(input())
if a==palindrom(a):
    print('True')
else:
    print('False')