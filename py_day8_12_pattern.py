def printseriesIncreasing(ch,n):
    for i in range(1,n+1,1):
        print(ch*i)
    return None
def printseriesDecreasing(ch,n):
    for i in range(n,0,-1):
        print(ch*i)
    return None
inpch=input("Enter a charactter:")
inpnum=int(input("Enter a no:"))
printseriesIncreasing(inpch,inpnum)
print('-'*40)
printseriesDecreasing(inpch,inpnum)
