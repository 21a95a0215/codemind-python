n=input()
a=n.split(":")
h=int(a[0])
m=int(a[1])
Hh=h*30
Mm=m*(11/2)
x=abs(Hh-Mm)
if x<180:
    print(x)
else:
    print(360-x)