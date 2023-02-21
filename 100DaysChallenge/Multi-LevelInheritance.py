#Multi Level Inheritance
class Animal:
  def __init__(self,name,species):
    self.name = name
    self.species = species
  def showDetails(self):#Defining Base method from Base Class
    print(f"name: {self.name}")
    print(f"Species: {self.species}")

class Dog(Animal):
  def __init__(self,name,breed):
    Animal.__init__(self,name,species = "Dog")
    self.breed = breed
  def showDetails(self):
    Animal.showDetails(self)#Calling Method of its Parent Class
    print(f"Breed: {self.breed}")

class GoldenRetriever(Dog):
  def __init__(self,name,color):
    Dog.__init__(self,name,breed = "Golden Retriever")
    self.color = color
  def showDetails(self):
    Dog.showDetails(self)#Calling Method of its Parent Class
    print(f"Color: {self.color}")

a = GoldenRetriever("Moti","Golden")
a.showDetails()
    
