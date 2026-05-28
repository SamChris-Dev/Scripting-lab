class Car:
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return f"Car model: {self.model}"

    
    def is_electric(self):
        return issubclass(self.__class__, ElectricCar)  


class ElectricCar(Car):
    def __init__(self, model, battery_range):
        super().__init__(model) 
        self.battery_range = battery_range

    def __str__(self):
        
        return f"Electric Car model: {self.model}, Battery Range: {self.battery_range}km"



car1 = Car("Honda Civic")
car2 = Car("Honda Civic")
electric_car1 = ElectricCar("Tesla Model S", 400)

print(car1)  
print(electric_car1)   

print("Is instance: " + str(isinstance(electric_car1, Car)))  

print("The same object: " + str(car1 is car1)) 
print("The same object: " + str(car1 is car2))  
print("The same model: " + str(car1.model is car2.model))  


class LuxuryCar(ElectricCar):
    def __init__(self, model, battery_range, features):
        super().__init__(model, battery_range)  
        self.features = features

    def get_info(self):
       
        return super().__str__() + f"\nFeatures: {self.features}"


luxury_car = LuxuryCar("Tesla Model X", 500, "Autopilot, Self-parking")
print(
    luxury_car.get_info())
