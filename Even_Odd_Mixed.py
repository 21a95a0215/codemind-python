n=int(input(""))
s=0
t=0
while n>0:
    x=n%10
    if x%2==0:
        s+=1
    elif x%2!=0:
        t+=1
    n=n//10
if s==0:
    print("Odd")
elif t==0:
    print("Even")
else:
    print("Mixed")