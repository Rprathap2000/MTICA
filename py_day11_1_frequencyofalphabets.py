##def frequency(s):
##    d=dict()
##    for i in s:
##        if i in d:
##            d[i] +=1
##        else:
##            d[i]=1
##    return d
##def f(m):
##    for i in sorted(m):
##        print(i,m[i])
##a=int(input())
##for i in range(a):
##    inps=input()
##    f(frequency(inps))
##
def frequency(s):
    d=dict()
    for i in s:
        if i in d:
            d[i] +=1
        else:
            d[i]=1
    return d
a=int(input())
for i in range(a):
    inps=input()
    print(frequency(inps))
    
