x= int(input("Enter the number: "))
match x:
  case 0:
    print(x," is zero")
  case _ if x>=10 and x<=20:
    print(x," is between 10 and 20")
  case _:
    print(x)
