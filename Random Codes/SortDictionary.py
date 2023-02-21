#Sort by Keys
dict1 = {1: "Apple", 5:"Banana", 2:"Oranges", 9:"Cherry"}
d = sorted(dict1.keys())
dict2 = {}
for i in d:
    dict2[i] = dict1[i]
print(dict2)

#Sort by Values
dict3 = {key: value for key, value in sorted(dict1.items(), key = lambda x: x[1])}
print(dict3)
