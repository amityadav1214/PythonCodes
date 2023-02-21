#Multiple Inheritance
class Animal:
  def __init__(self,name,species):
    self.name = name
    self.species = species
  def makeSound(self):
    print("Sound made by Animal")

class Mammal:
  def __init__(self,name,fur_color):
    self.name = name
    self.fur_color = fur_color
  def makeSound(self):
    print("Sound made by Mammal")

class Dog(Mammal,Animal):#Class mentioned first will get its method called if the method names are same in parent classes
  def __init__(self,name,fur_color,breed):
    Animal.__init__(self,name,species = "Dog")
    Mammal.__init__(self,name,fur_color)
    self.breed = breed

a = Dog("Moti","Blue","Dobberman")
print(a.name)
print(a.breed)
print(a.fur_color)
a.makeSound()
    
