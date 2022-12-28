l1=[11,22,33,44,55]
l2=[1,2,3,4,5,6,7,8]
l3=[5,6,5,2,1,3,2,3]
print(l1)
print(l2)
print(l3)
ans=list(map(lambda a,b,c:a*b+c,l1,l2,l3))
print(ans)
