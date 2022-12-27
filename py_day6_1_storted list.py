li=[]
while(True):
    n=int(input("Enter the number"))
    if n==0:
       break
    else:
        li.append(n)
li.sort()
print("min:",li[0])
print("max:",li[-1])
print("avg:",round(sum(li)/len(li),1))
