n=int(input())
a=[]
while n>0:
    x=n%10
    a.append(x)
    n=n//10
b=set(a)    
if len(a)==len(b):
    print('Unique Number')
else:
    print('Not Unique Number')