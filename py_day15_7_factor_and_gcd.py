def findfactor(n):
    temp=[]
    for i in range(1,n+1):
        if n%i==0:
            temp.append(i)
    return temp

def findGCD(n1,n2):
    lst1=findfactor(n1)
    lst2=findfactor(n2)
    s1=set(lst1)
    s2=set(lst2)
    ans=list(s1.intersection(s2))
    ans.sort()
    return ans[-1]

print("Enter two numbers:")
a=int(input())
b=int(input())

print(findGCD(a,b))
