class circle:
    pi=22/7
    def __init__(self,radius):
        self.radius=radius
    def calarea(self):
        temp=self.pi*self.radius**2
        return temp
    def perimeter(self):
        temp=2*self.pi*self.radius
        return temp
        
radius=int(input())
ob=circle(radius)
area=ob.calarea()
peri=ob.perimeter()
print('Area of circle with radius ',radius, 'is' ,area)
print('Perimeter of circle with radius ',radius,'is',peri)
   
