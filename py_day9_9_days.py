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
intp=int(input("Enter the number:"))
print(dayname(intp))
