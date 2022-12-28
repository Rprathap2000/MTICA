dict1={"sedan":1500,"SUV":2000,"Pickup":2500,"Bicycle":7,"Motorcycle": 110}
##rp=[]
##for i in dict1:
##    if dict1[i]<5000:
##        rp.append(i.upper())
##        
##print(rp)





##print([i.upper() for i in dict1 if dict1[i]<5000])





rp=[i.upper() for i in dict1 if dict1[i]<5000]
print(rp)
