##def printingmonth(dn):
##    if(dn==1):
##        return 'Janvary'
##    elif(dn==2):
##        return 'Febravary'
##    elif(dn==3):
##        return 'March'
##    elif(dn==4):
##        return 'April'
##    elif(dn==5):
##        return 'May'
##    elif(dn==6):
##        return 'June'
##    elif(dn==7):
##        return 'July'
##    elif(dn==8):
##        return 'Aguest'
##    elif(dn==9):
##        return 'Septambar'
##    elif(dn==10):
##        return 'October'
##    elif(dn==11):
##        return 'November'
##    elif(dn==12):
##        return 'December'
##    else:
##        return 'NOT VALID'
##intp=int(input("Enter the number:"))
##print(printingmonth(intp))


def printingmonth(dn):
    mn=''
    if(dn==1):
        mn='Janvary'
    elif(dn==2):
        mn= 'Febravary'
    elif(dn==3):
        mn= 'March'
    elif(dn==4):
        mn='April'
    elif(dn==5):
        mn= 'May'
    elif(dn==6):
        mn= 'June'
    elif(dn==7):
        mn= 'July'
    elif(dn==8):
        mn= 'Aguest'
    elif(dn==9):
        mn= 'Septambar'
    elif(dn==10):
        mn= 'October'
    elif(dn==11):
        mn= 'November'
    elif(dn==12):
        mn= 'December'
    else:
        mn= 'NOT VALID'
    return mn
##intp=int(input("Enter the number:"))
##print(printingmonth(intp))
for i in range(3):
    inpNum=int(input("Enter the number:"))
    print(printingmonth(inpNum))
    

    
    
