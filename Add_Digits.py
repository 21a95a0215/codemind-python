n=int(input())
y=0
while n>0:
    x=n%10
    y=y+x
    n=n//10
    if n==0 and y>9:
        n=y
        y=0
print(y)
    