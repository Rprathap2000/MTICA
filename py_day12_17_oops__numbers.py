class number:
    college='MTICA'
    course='MCA'
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def bark(self):
        print('Name :'+self.name.title()+'\nrollno :'\
              +str(self.rollno))
        print('college :'+self.college+'\ncourse :'+self.course)
lstobj=[]
for i in range(1):
    n=input("Enter Your Name:")
    r=int(input("Enter your hallticket Number:"))
    print("*********************")
    temp='obj'+str(i)
    temp=student(n,r)
    lstobj.append(temp)
for i in lstobj:
    i.bark()
   
