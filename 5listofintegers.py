a=[]
n=int(input("enter the limit:"))
for x in range(n):
    x=int(input("enter the numbers:"))
    if x>100:
        a.append("over")
    else:
        a.append(x)
print(a)