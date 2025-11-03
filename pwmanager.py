print("Password Generator:")
#x is acting as a pool of values that can be randomly generated
import random
x = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789"

#"input" will register the values the user inputs, then assign them as integers
number = input('Number of Passwords:')
number = int(number)

length = input('Password Length:')
length = int(length)

for p in range(number): #for loop will look for the range given by users' input
    password = " "
    for count in range(length): 
        password += random.choice(x) #a random value from "x" is being obtained, a certain amount of times
    print(password)