#Single Inheritance
class Animal:
  def __init__(self,animal,species):
    self.animal = animal
    self.species = species
  def makeSound(self):
    print("Sound made by Animal")
class Cat(Animal):
  def __init__(self,animal,breed):
    Animal.__init__(self,animal,species = "Cat")
    self.breed = breed
  def makeSound(self):
    print("Meow")

a= Animal("Lion","Wild Cat")
a.makeSound()
b= Cat("Cat","Persian Cat")
b.makeSound()
