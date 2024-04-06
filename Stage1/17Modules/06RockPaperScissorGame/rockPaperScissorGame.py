# 👉 Rock,papper and Scissor Game with Random Module of Python

import random

l = ["rock", "scissor", "paper"]

# '''
#  rock vs paper -> paper wins
#  rock vs scissor -> rock wins
#  paper vs scissor -> scissor wins
# '''

while True:
      Ccount = 0
      Ucount = 0
      uc = int(input('''
       Game Start...
       1. Yes
       2. No | Exit
      '''))
      if uc==1:
            for a in range(1,6):
                  userInput = int(input('''
                        1. Rock
                        2. Scissor
                        3. Paper
                               '''))
                  if userInput==1:
                        uchoice = "rock"
                  elif userInput==2:
                        uchoice = "scissor"
                  elif userInput==3:
                        uchoice = "paper"
                  Cchoice = random.choice(l)
                  if Cchoice==uchoice:
                        print("Computer Value:",Cchoice)
                        print("User Value:",uchoice)
                        print("Game Draw")
                        Ucount += 1
                        Ccount += 1
                  elif (uchoice=="rock" and Cchoice == "scissor") or ( uchoice=="paper" and Cchoice == "rock") or ( uchoice=="scissor" and Cchoice == "papper"):
                        print("Computer Value:",Cchoice)
                        print("User Value:",uchoice)
                        print("You Win")
                        Ucount += 1
                  else:
                        print("Computer Value:",Cchoice)
                        print("User Value:",uchoice)
                        print("Computer Win")
                        Ccount += 1
            if Ccount==Ucount:
             print("Computer count:",Ccount)
             print("User count:",Ucount)
             print("Match Draw")
            elif Ucount > Ccount:
             print("Computer count:",Ccount)
             print("User count:",Ucount)
             print("🎉You Win")
            else:
              print("Computer count:",Ccount)
              print("User count:",Ucount)
              print("🎉Computer Win")
      else:
            break;
      