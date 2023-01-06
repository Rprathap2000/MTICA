class  vehicle:
    def __init__(self,name,speed,milage):
        self.name=name
        self.speed=speed
        self.milage=milage
    def seating_capacity(self,capacity):
        return f"The seating capacity of a {self.name}is {capacity} passengers"
class bus(vehicle):
    def seating_capacity(self,capacity=50):
        return super().seating_capacity(capacity=50)
school_bus =bus("School Volvo ", 180,12)
print(school_bus.seating_capacity())
