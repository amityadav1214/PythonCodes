#Instance Variables V/s Class Variables
class Employee:
  company = "Apple" #Example of Class Variable
  def __init__(self,name):
    self.name = name
    self.raise_amount = 0.02
  def showDetails(self):
    print(f"{self.name} got raised in {self.company} of {self.raise_amount}")

a = Employee("Harry")
a.showDetails()
b = Employee("Amit")
b.raise_amount = 0.3
b.company = "Apple India" #Examle of Instance Variable
b.showDetails()
#If Instance Variable is not decalred with the object then value of class variable is defined.
