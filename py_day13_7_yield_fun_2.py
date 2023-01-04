def sum_series(r,p):
    assert(r<p),"first argument should be smaller than second"
    total=0
    for i in range(r,p,1):
        total=total +i
        yield total
r=int(input())
p=int(input())
ob=sum_series(r,p)
x=0
try:
    while x<10:
        print(next(ob))
        x=x+1
except AssertionError as obj:
    print(obj)

