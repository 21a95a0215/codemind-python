a,b=map(int,input().split())
if b+1==a or a+1==b:
    print("Yes")
elif a==1 and b==10:
    print("Yes")
elif a==10 and b==1:
    print("Yes")
else:
    print("No")