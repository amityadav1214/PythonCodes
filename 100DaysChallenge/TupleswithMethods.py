#Tuples
tup = (1,2,3)
print(type(tup),tup)
tu1 = (1,)  # Need to add comma for python to understand that its a tuple
print(tu1)
#Tuples object does not change values inside tuples
for i in range(len(tup)):
  print(tup[i])

if 1 in tup:
  print("Yes 1 is in tup")
else:
  print("1 is not in tup")

#Difference between tuples and lists are tuples cannot be chnged, they are immutable.

#Tuples Methods manipulating tuples-Cannot change values in tuple. First make it to list and then change it to tuple
countries = ("India","Spain","Germany","Italy","France","England")
print(countries)
temp = list(countries)
temp.append("Pakistan")
countries = tuple(temp)
print(countries)

#tuples can be concatenated as a new tuple is create while doing it.
tup2 = (1,1,1,1,1,2,3,4,5,6,7)
print(tup2.count(1))
print(tup2.index(3))
