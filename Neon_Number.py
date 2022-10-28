n=int(input())
x=n*n
s=0
while x>0 :
    a=x%10
    s=s+a
    x=x//10
if n==s :
    print("Neon Number")
else :
    print("Not Neon Number")