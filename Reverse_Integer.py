n=int(input())
s=0
d=False
if n<0:
    n=abs(n)
    d=True
while n>0:
    x=n%10
    s=s*10+x
    n=n//10
if d:
    print(-s)
else:
    print(s)