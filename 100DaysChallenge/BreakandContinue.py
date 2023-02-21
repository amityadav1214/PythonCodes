#Break Statement
i = int(input("Enter the number which you need the table of: "))
for j in range(12):
  if j == 10:
    break
  print(i," X ",j+1," = ",i*(j+1))

#Continue Statement
i = int(input("Enter the number which you need the table of: "))
for j in range(12):
  if j == 10:
    print("Skip the Iteration")
    continue
  print(i," X ",j+1," = ",i*(j+1))
