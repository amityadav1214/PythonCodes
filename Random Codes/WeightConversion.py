weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Your weight in LBS "+str(converted))
else:
    converted = weight * 0.45
    print("Your weight in KG "+str(converted))
