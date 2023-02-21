#Classes and Object
class Person:
  name  = "Harry"
  Occupation = "Software Engineer"
  Networth = 10
  def info(self):# Self parameter is used to access variables defined in the class itself.
    print(f"{self.name} is a {self.Occupation}")

a = Person() # a is an Object of Class Person
a.info()
