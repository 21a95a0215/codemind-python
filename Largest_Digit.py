n=int(input())
s=0
while n>0:
    x=n%10
    n=n//10
    if x>s :
        s=x
print(s)        
        