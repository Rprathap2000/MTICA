def fun(s):
    print(s)
    return
fun("I'm first call to user defined function!")
fun("Again second call to the same function")

def printu(s,num):
    num[0]='rohith'
    print(s,num)
    return
inp=['Rohith','Rajeesh']
printu("Wakeup_its already 10 o clock",inp)
print('inp:',inp)

