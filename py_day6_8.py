import time
inp=int(input("Enter the number:"))
start=time.time()
for i in range(inp):
    print("i=",i,"i^2=",i*i)
print("The taken by Loop:",(time.time()-start)*100000)
