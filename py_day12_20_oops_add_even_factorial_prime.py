class Number:
    def __init__(self,n):
        self.n=n
    def Factorial(self):
        if self.n==0:
            return 1
        res=1
        for i in range(1,self.n+1):
            res*=i
        return res
    def evenodd(self):
        if self.n%2==0:
            return "Even"
        else:
            return "ODD"
    def sod(self):
        if self.n<0:
            self.n=abs(self.n)
        temp=str(self.n)
        t=0
        for i in temp:
            t=int(i)
        return t
    def  armstrongnumber(self):
        if self.n<0:
            self.n=abs(self.n)
        temp=str(self.n)
        t=0
        for i in temp:
            t+=int(i)**len(temp)
        if self.n==1:
            return "A N"
        else:

            return " not a n  "
    def prime(self):
        assert (self.n>=0),"not vallid"
        if self.n==1 or self.n==2 or self.n==3:
            return "a prime number"
        else:
            for i in range(2,self.n):
                if self.n%i== 0:
                    return "Not a prime number"
                return "Is a prime number"
        
inp=int(input())
o=Number(inp)
print('Factioral of ',inp, 'is' ,o.Factorial())
print(inp,'is',o.evenodd())
print('sum of digits of',inp,'is',o.sod())
print('\n'+str(inp),'is',o.armstrongnumber())
try:
    p=o.prime()
    print(p)
except AssertionError as obj:
    print(obj)
