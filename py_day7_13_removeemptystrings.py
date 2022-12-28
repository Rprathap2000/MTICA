##for i in range(5):
##    inp=input()
##    if inp:
##        print("Hellow "+inp)
##    else:
##        print("Bye "+inp)





rp=["Sedan", "SVU", "", "", "Pickup",'', '  ']
ans=[]
for i in rp:
    if i:
        ans.append(i)
print(ans)



print([ i for i in rp if i])

ans=[i for i in rp if i]
print(ans)
