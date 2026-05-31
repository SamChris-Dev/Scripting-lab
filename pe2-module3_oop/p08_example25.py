class Animal:
    def __init__(self, species):
        self.species = species

    def __str__(self):
        return f"Animal species: {self.species}"
    
    def is_bird(self):
        return issubclass(self.__class__, Bird)  


class Bird(Animal):
    def __init__(self, species, wingspan):
        super().__init__(species) 
        self.wingspan = wingspan

    def __str__(self):
        return f"Bird species: {self.species}, Wingspan: {self.wingspan}cm"


animal1 = Animal("Python")
animal2 = Animal("Python")
bird1 = Bird("Bald Eagle", 200)

print(animal1)  
print(bird1)   

print("Is instance: " + str(isinstance(bird1, Animal)))  

print("The same object: " + str(animal1 is animal1)) 
print("The same object: " + str(animal1 is animal2))  
print("The same species: " + str(animal1.species is animal2.species))  


class BirdOfPrey(Bird):
    def __init__(self, species, wingspan, traits):
        super().__init__(species, wingspan)  
        self.traits = traits

    def get_info(self):
        return super().__str__() + f"\nTraits: {self.traits}"


apex_predator = BirdOfPrey("Peregrine Falcon", 120, "Dive-bombing, Exceptional vision")
print(apex_predator.get_info())