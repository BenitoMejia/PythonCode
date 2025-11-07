print("Dice Game")
import random
# 1. Generate two random single-digit integers (1-6)
number1 = random.randint(1, 6)
number2 = random.randint(1, 6)
total = number1+number2

# Dice numbers 
print("Dice 1:",number1,"Dice 2:",number2) 
print("Total:",total)

# Dice test (nested if)
if total == 7 or total == 11:
    print("You win!") #or means either both or one are true
elif number1 == number2:
    if number1 == 6 and number2 == 6:
        print("Jackpot!") #and means both have to be true 
    else:
        print("Doubles, you win!") #if previous condition isn't met, then it'll choose the else
else:
    print("You loose")