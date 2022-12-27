r=[]
r_even=[]
r_odd=[]
while(True):
    inp=int(input("Enter a value(-1 to end):"))
    if inp==-1:
        break
    if inp%2==0:
       r_even.append(inp)
    else:
        r_odd.append(inp) 
r.sort()
print("r_even",*r_even)
print("min_even",min(r_even))
print("max_even",max(r_even))
print("avg_even",round(sum(r_even)/len(r_even),1))
print("p_odd",*r_odd)
print("min_odd",min(r_odd))
print("max_odd",max(r_odd))
print("avg_odd",round(sum(r_odd)/len(r_odd),1))

