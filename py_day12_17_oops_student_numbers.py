class number:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2
    def sub(self):
        return self.num1-self.num2
    def mul(self):
        return self.num1*self.num2
    def div(self):
        assert (self.num2!=0),"Division by Zero is not possible"
        return self.num1/self.num2
    def modulo(self):
        assert (self.num2!=0),"Division by Zero is not possible"
        return self.num1%self.num2
    def intdiv(self):
        assert (self.num2!=0),"Division by Zero is not possible"
        return self.num1//self.num2
    


    
for i in range(1):
    num1=int(input("Enter Your Number1:"))
    num2=int(input("Enter your  Number2:"))
    ob=number(num1,num2)
    print(num1, '+' ,num2, '=' ,ob.add(),sep='')
    print(num1, '-' ,num2, '=' ,ob.sub(),sep='')
    print(num1, '*' ,num2, '=' ,ob.mul(),sep='')
    try:
        print(num1, '/' ,num2, '=' ,ob.div(),sep='')
    except ZeroDivisionError as obj:
        print(obj)
    try:
        print(num1, '%' ,num2, '=' ,ob.modulo(),sep='')
    except ZeroDivisionError as obj:
        print(obj)
    try:
        print(num1, '//' ,num2, '=' ,ob.intdiv(),sep='')
    except ZeroDivisionError as obj:
        print(obj)
