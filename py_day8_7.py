def checkevenodd(num1):
    assert(num1>0),"Negitive numbers"
    if num1%2==1:
        return "Even"
    else:
        return "odd"
for i in range(3):
    num=int(input("Enter a no:"))
    try:
        print(num,"is",checkevenodd(num))
    except AssertionError as ob:
        print(ob)
