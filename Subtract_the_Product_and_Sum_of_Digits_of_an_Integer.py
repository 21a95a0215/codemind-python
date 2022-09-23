n=int(input(""))
s=1
t=0
while n>0:
    x=n%10
    s*=x
    t+=x
    n=n//10
print(s-t) 