def printingstars(ch,n):
    assert isinstance(ch,str),"first argument should be string"
    assert isinstance(n,int),"second argument should be integer"
    for i in range(1,n+1,1):
        print(ch*i)
    for i in range(n,0,-1):
        print(ch*i)
    return None

inpc=input("Enter a Character:")
inpn=int(input("Enter a no:"))
print('-'*40)
try:
    printingstars(inpc,inpn)
except AssertionError as obj:
    print(obj)

