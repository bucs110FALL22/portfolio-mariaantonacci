import random

num=random.randrange(1,11)
num_guesses=1

for i in range(3):
  guess_num=int(input("Please guess a number:"))
  num_guesses = num_guesses + 1
  num_guesses = num_guesses + 1
  if guess_num>num:
      print("Too high")
  elif guess_num<num:
      print("Too low")
  else:
    print("Correct")
    break
