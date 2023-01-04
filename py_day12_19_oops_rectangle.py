class Rectangle:
    def __init__(self,length,width):
        assert (length>0),"Invalid"
        self.length=length
        self.width=width
    def calarea(self):
        temp=self.length*self.width
        return temp
    def perimeter(self):
        temp=2*(length+width)
        return temp





    
length=int(input())
width=int(input())
try:
    ob=Rectangle(length,width)
    area=ob.calarea()
    peri=ob.perimeter()
    print('Area of rectangle is' ,area)
    print('Perimeter of rectangle is',peri)
except AssertionError as o:
    print(o)
