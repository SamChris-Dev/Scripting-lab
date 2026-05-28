class Animal:

    def make_sound(self):

        return "Animal sound (maybe unknown). "


class Dog(Animal):

    def __init__(self, name: str, breed: str):

        self.name = name
        self.breed = breed

    def make_sound(self):

        return super().make_sound() + f"{self.name} the {self.breed} says: Woof!"


class Cat(Animal):

    def __init__(self, name: str):

        self.name = name

    def make_sound(self):

        return f"{self.name} says: Meow!"


def print_animal_sound(animal: Animal):

    print("animal.make_sound(): " + str(animal.make_sound()))



animal1 = Animal()
print_animal_sound(animal1)

dog = Dog("Buddy", "Golden Retriever")
print_animal_sound(dog)

cat = Cat("Whiskers")
print_animal_sound(cat)