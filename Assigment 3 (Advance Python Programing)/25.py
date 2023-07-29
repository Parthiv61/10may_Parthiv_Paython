"""Explain Inheritance in Python with an example? What is init? Or What 
Is A Constructor In Python?"""

#Inheritance is a fundamental object-oriented programming concept that allows a class (subclass) to inherit attributes and behaviors from another class (superclass). This means that the subclass can reuse code from the superclass and extend or modify its functionality as needed. Inheritance facilitates code reusability and promotes a hierarchical organization of classes.

class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(f"The {self.species} makes a {self.sound} sound.")

class Dog(Animal):
    def __init__(self, breed, sound):
        super().__init__('dog', sound)
        self.breed = breed

    def make_sound(self):
        print(f"The {self.breed} dog barks: {self.sound}!")

class Cat(Animal):
    def __init__(self, breed, sound):
        super().__init__('cat', sound)
        self.breed = breed

    def make_sound(self):
        print(f"The {self.breed} cat meows: {self.sound}!")

dog = Dog('Golden Retriever', 'Woof')
cat = Cat('Siamese', 'Meow')

dog.make_sound()  # Output: "The Golden Retriever dog barks: Woof!"
cat.make_sound()  # Output: "The Siamese cat meows: Meow!"

