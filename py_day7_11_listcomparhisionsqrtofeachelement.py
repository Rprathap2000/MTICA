##rp=[10,15,2,25,30,3,40,4]
##ans=[]
##for i in rp:
##    if i**2>=50:
##        ans.append(i**2)
##print(ans)
##
##
##
##rp=[10,15,2,25,30,3,40,4]
##print([i**2 for i in rp if i**2>=50])




rp=[10,15,2,25,30,3,40,4]
ans=[i for i in rp if i**2>=50]
print(ans)
