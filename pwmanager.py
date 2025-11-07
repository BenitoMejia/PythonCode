print("Password Generator:")
#x is acting as a pool of values that can be randomly generated
import random
x = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789"

number = int(input('Number of Passwords:'))

length = int(input('Password Length:'))

for p in range(number): #for loop will according to the users' input
    password = " "
    for count in range(length): #for loop will according to the users' input
        password += random.choice(x) #a random value from "x" is being obtained, a certain amount of times
    print("Password:", password)