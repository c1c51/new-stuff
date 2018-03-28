x=[]
i=1
comparisons=changes=0
n=z=p=car=q=0
n=int(input("how many numbers to sort"))
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
            x[y],x[y+1]=x[y+1],x[y]
            comparisons+=1
            changes+=1
            #print(x)
            while car==0:
                if x[y-q]<x[y-q-1]:
                    x[y-q-1],x[y-q]=x[y-q],x[y-q-1]
                    #print(x)
                    q+=1
                    car=0
                    comparisons+=1
                    changes+=1
                else:
                    car=1
                    comparisons+=1
            y+=1
            q=1
        else:
            y+=1
            comparisons+=1
    z+=1
print("done")
print(x)
print("comparisons:",comparisons)
print("changes:",changes)
            
