def dayname(dn):
    if(dn==1):
        return 'Sunday'
    elif(dn==2):
        return 'Monday'
    elif(dn==3):
        return 'Tuesday'
    elif(dn==4):
        return 'Wednesday'
    elif(dn==5):
        return 'Thrusday'
    elif(dn==6):
        return 'Friday'
    elif(dn==7):
        return 'Saturday'
    else:
        return 'NOT VALID'
import time
for i in range(7):
    inpNum=int(input("Enter the number:"))
    start=time.time()
    print(dayname(inpNum))
    print((time.time()-start)*100000)
    start=time.time()
    print(dayname(inpNum))
    print((time.time()-start)*100000)
    
