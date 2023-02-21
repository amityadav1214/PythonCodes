import random,sys
print("SNAKE WATER GUN GAME")
wins = 0
tie = 0
losses = 0
while True:
  #Taking Input from Player\
  print('%s Wins , %s Losses , %s Ties' % (wins,losses,tie))
  while True:
    playermove = input("Enter your choices for (s)nake, (w)ater and g(un) or q(uit) to quit from the game: ")
    playermove.lower()
    if playermove == "q":
      print("Quiting from the game")
      sys.exit()
    if playermove == "s" or playermove == "r" or playermove == "g":
      break
  print("Please type one of 's','w','g' or 'q' ") 
  #Displaying what Player have choosen
  if playermove == "s":
    print("SNAKE VERSUS: ")
  elif playermove == "w":
    print("WATER VERSUS: ")
  elif playermove == "g":
    print("GUNS VERSUS: ")
  rand = random.randint(1,3)
  if rand == 1:
    print("Computer Move is SNAKE")
    computermove = "s"
  elif rand ==2:
    print("Computer Move is Water")
    computermove = "w"
  elif rand ==3:
    print("Computer Move is Gun")
    computermove = "g"
#Counting Wins, Losses and Ties
  if playermove == computermove:
    print('Its a Tie')
    tie = tie + 1
  elif playermove == "s" and  computermove == "w":
    print('You win')
    wins = wins + 1
  elif playermove == "w" and  computermove == "g":
    print('You win')
    wins = wins + 1
  elif playermove == "s" and  computermove == "g":
    print('You win')
    wins = wins + 1
  elif playermove == "w" and  computermove == "s":
    print('You Lose')
    losses = losses + 1
  elif playermove == "g" and  computermove == "w":
    print('You Lose')
    losses = losses + 1
  elif playermove == "g" and  computermove == "s":
    print('You Lose')
    losses = losses + 1
