class Cat:
    def __init__(self,colour,legs):
        self.colour=colour
        self.legs=legs
    def __str__(self):
        temp="Cat is "+self.colour+' colour '+'and has '+str(self.legs)+" legs"
        return temp
if __name__=="__main__":
    pet1=Cat("ginger",4)
    print(pet1.legs)
    print(pet1.colour)
    print(pet1)

    pet2=Cat("brown",3)
    print(pet2.legs)
    print(pet2.colour)
    print(pet2)
