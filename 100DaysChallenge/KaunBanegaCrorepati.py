questions = [
  ["Shiv won which BB Marathi season","2","1","3","4",1],
  ["Siddharth won which BB season","10","12","13","4",3],
  ["Rubina won which BB season","2","1","14","4",3],
  ["Gauhar won which BB season","7","1","3","4",1],
  ["Gautam won which BB season","2","1","3","8",4],
  ["Megha won which BB season","2","1","3","4",1],
  ["Shreesanth won which BB season","2","11","3","4",2],
  ["Prince won which BB season","2","1","3","9",4],
  ["Saai won which BB season","2","1","3","4",2],
  ["Khali won which BB season","4","1","3","14",1],
  ["Shweta won which BB season","2","1","5","4",3],
  ["Hina won which BB season","2","11","3","4",2],
  ["Veena won which BB season","2","1","3","4",1],
  ["Shalin won which BB season","2","1","3","16",4]
]
levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
money = 0
for i in range(0,len(questions)):
  question = questions[i]
  print(f"\n Question for Rs.{levels[i]} is \n {i+1}.{question[0]}")
  print(f"a.{question[1]}        b.{question[2]}")
  print(f"c.{question[3]}        d.{question[4]}")
  reply = int(input("Enter your answers in 1-4 format or 0 to quit: "))
  if reply == 0:
    money = levels[i-1]
    break
  if reply == question[-1]:
    print(f"You have won Rs. {levels[i]}")
    if i == 4:
      money = 10000
    elif i == 9:
      money = 320000
  else:
    print("Wrong Answer")
    break
print(f"You have won Rs. {money}")
