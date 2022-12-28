##rp=[]
##for i in range(1,16):
##    temp=[]
##    for j in  range(1,10):
##        if i%j==0:
##            temp.append(i)
##    rp.append([i,max(temp)])
##print(rp)


#rp=[]
#for i in range(1,16):
#    rp.append([i,max([j for j in  range(1,10) if i%j==0])])
#print(rp)



rp=[[i,max([j for j in  range(1,10) if i%j==0 ])] for i in range(1,16)   ]

print(rp)
