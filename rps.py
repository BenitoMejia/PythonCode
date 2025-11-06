print ("Rock, Paper, Sccisors")
import random
mylist = ["rock", "paper", "sccisors"]

player1 = input('rock, paper, or sccisors?:')
player2 = random.choice(mylist)

if player1 == player2:
     print("Computer:", player2)
     print("Draw!")
elif player1 == 'sccisors' and player2 == 'paper':
     print("Computer:", player2)
     print("You Win!")
elif player1 == 'paper' and player2 == 'rock':
     print("Computer:", player2)
     print("You Win!")
elif player1 == 'rock' and player2 == 'sccisors':
     print("Computer:", player2)
     print("You Win!")
else:
     print("You lost")