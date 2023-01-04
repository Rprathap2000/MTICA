def checklengthofstring(n):
    lst=n.split()
    return [len(i) for i in lst]
       
n=input()
print(*checklengthofstring(n))






