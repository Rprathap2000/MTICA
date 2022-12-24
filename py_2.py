import math
n=input("Enter the number") 
total=0
for i in n:
    total +=math.pow(int(i),len(n))
    if int(n)==total:
        print(n,"armstrong number")
    else:
        print(n,"is not a armstronf number")
        
    
