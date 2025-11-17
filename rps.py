print ("Rock, Paper, Scissors Game")
import random
mylist = ["rock", "paper", "scissors"]

player1 = input('Do you choose rock, paper, or scissors?:')
player2 = random.choice(mylist)

if player1 == player2:
     print("Computer chose:", player2)
     print("Draw!")
elif player1 == 'scissors' and player2 == 'paper':
     print("Computer chose:", player2)
     print("You Win!")
elif player1 == 'paper' and player2 == 'rock':
     print("Computer chose:", player2)
     print("You Win!")
elif player1 == 'rock' and player2 == 'scissors':
     print("Computer chose:", player2)
     print("You Win!")
else:
     print("Computer chose:", player2)
     print("Computer Won. Better luck next time")