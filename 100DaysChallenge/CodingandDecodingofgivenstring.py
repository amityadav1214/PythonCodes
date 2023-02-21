#For coding of string
str = input("Enter message: \n")
str1 = str.split(" ")
print(str1)
words = []
coding = False
if(coding):
  for word in str1:
    if (len(word)>=3):
      rnc1 = "ksk"
      rnc2 = "bsk"
      strnew = rnc1+word[1:]+word[0]+rnc2
      words.append(strnew)
    else:
      words.append(word[::-1])
  print(" ".join(words))
else:
#For Decoding of string 
  words = []
  for word in str1:
    if (len(word)>=3):
      strnew = word[3:-3]
      strnew = strnew[-1]+strnew[:-1]
      words.append(strnew)
    else:
      words.append(word[::-1])
  print(" ".join(words))
