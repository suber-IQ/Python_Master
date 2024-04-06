# 👉 Guessing Game with Random Module

import random

cnumber = 5
# cnumber =  random.randrange(1,101)
userInput = int(input("Enter Your Number 1 to 100 :"))

if userInput > cnumber:
      print("Computer Number",cnumber)
      print("Your guess number is high")
elif userInput < cnumber:
      print("Computer Number",cnumber)
      print("Your guess number is low")
else:
      print("Computer Number",cnumber)
      print("🎉 Congratulations, Your guess number is Equal")
      