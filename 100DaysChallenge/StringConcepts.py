##String Concepts
name = '''I am Amit Yadav.
Want to become a Data Engineer'''
for character in name:
  print(character)

##String Slicing and Opertions on Strings
fruit = 'Mango'
print(fruit[0:4])
print(fruit[:4])
print(fruit[0:])
print(fruit[2:4])
print(fruit[0:-3])
print(fruit[:-3])
print(fruit[-4:-2])


##String Methods in Python 
a = "mango is VerY tasty"
print(len(a))
print(a.upper())
print(a.lower())
print(a.replace("Mango","Orange"))
print(a.split(" "))
print(a.capitalize())
print(a.center(50))
print(a.count("no"))
print(a.endswith("rY",0,13))
print(a.find("is"))
print(a.index("is"))
print(a.isalnum())
print(a.isalpha())
print(a.islower())
print(a.isprintable())
print(a.isspace())
print(a.istitle())
print(a.startswith("rY",0,13))
print(a.swapcase())
