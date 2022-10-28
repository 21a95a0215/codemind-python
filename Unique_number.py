n=int(input())
x=str(n)
y=set(x)
if len(x) == len(y):
    print('Unique Number')
else:
    print('Not Unique Number')
    