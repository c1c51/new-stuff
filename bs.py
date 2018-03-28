x=[]
i=1
comparisons=changes=0
n=z=p=0
n=int(input("how many numbers to sort"))       #this is the bit that allows list input
n+=1
while i!=n:
    print("number")
    g=float(input())
    x.append(g)
    i=i+1
while z<(len(x)-1):
    y=0
    while y<(len(x)-1):
        if x[y]>x[y+1]:
            print(x)
            x[y],x[y+1]=x[y+1],x[y]
            comparisons+=1
            changes+=1
            y+=1
        else:
            print(x)
            comparisons+=1
            y+=1
    z+=1
print("done")
print(x)
print("comparisons:",comparisons)
print("changes:",changes)   
