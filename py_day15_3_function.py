class  vehicle:
    def __init__(self,name,speed,milage):
        self.name=name
        self.speed=speed
        self.milage=milage
class bus(vehicle):
    pass
school_bus =bus("School Volvo ", 180,12)
print("vehicle name :",school_bus.name,"\nspeed:",school_bus.speed,"\nmilage:",school_bus.milage)
