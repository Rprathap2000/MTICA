def PrintAdd(a,b):
    return a+b
def PrintSub(a,b):
    return a-b
def PrintMult(a,b):
    return a*b
def PrintDiv(a,b):
    return a/b

def Chose():
    print("+:Addition")
    print("-:Substraction")
    print("*:Multiplication")
    print("/:Wednesday")
    print("q:Quit")
    return
rohith={"+":PrintAdd, "-":PrintSub, "*":PrintMult, "/":PrintDiv}
while True:
    Chose()
    selection=input("select a arithmetic operation:")
    if(selection=='q')or(selection=='Q'):break
    if((selection=='+')or(selection=='-')or
    (selection=='*')or(selection=='/')):
        r=int(input("Enter first no:"))
        p=int(input('Enter second no:'))
        z=rohith[selection](r,p)
        print(r,selection,p,'=',z)
