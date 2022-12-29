
def checkeven(num1):
    if num1%2==0:
        return "even"
    return None
def checkodd(num1):
    if num1%2==1:
         return "odd"
    return None
num1=int(input())
x=checkeven(num1)
y=checkodd(num1)
print("x=",x)
print("y=",y)
print(checkeven(num1))
print(checkodd(num1))
