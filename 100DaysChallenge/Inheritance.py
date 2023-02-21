#Inheritance
class Employee:
  def __init__(self,name,id):
    self.name = name
    self.id = id
  def showDetails(self):
    print(f"Employee for {self.id} is : {self.name}")

class Programmer(Employee):
  def showLanguage(self):
    print("The default language is Python")

a = Employee("Amit",100)
a.showDetails()
b = Employee("Sameer",200)
b.showDetails()
#b.showLanguage() #Will not work
c = Programmer("Shiv",300)
c.showDetails()
c.showLanguage()
