s = "the cat and the dog"
new_s = " ".join(word[0].upper()+word[1:] for word in s.split(" "))
print(new_s)
