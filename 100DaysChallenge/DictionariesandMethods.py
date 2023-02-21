#Dictionaries
info = {'name': "Amit",'Age':32,'Eligible': True}
print(info.keys())
print(info.get('name')) #Not gives an error if key not present in Dictionary
print(info.values())
for key in info.keys():
  print(f"The value corresponds to {key} is: {info[key]}")

#Dictionaries Method
empl1 = {100:45,101:69,102:72,103:84}
empl2 = {104:54,105:61}
empl1.update(empl2)
print(empl1)
empl2.pop(105) #popitem removes the last key and value from the dictionary
print(empl2)
empl2.clear()
print(empl2)
#del keyword deletes the whole dictionary. Here we can del a single key as well like
del empl1[100]

print({x: x**2 for x in (2,3,4)})#dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:
for i,v in enumerate(["Amit","Sameer","Mom"]):
  print(i,v)
