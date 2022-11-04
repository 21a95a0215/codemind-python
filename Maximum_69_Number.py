n=int(input())
a=str(n)
b=list(a)
c=len(b)
for i in range(0,c):
    if b[i]=="6":
        b[i]="9"
        break
print("".join(b))
