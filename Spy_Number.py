n=int(input(""))
s=0
t=1
while n>0:
    x=n%10
    s+=x
    t*=x
    n=n//10
if s==t:
    print("Spy Number")
else:
    print("Not Spy Number")