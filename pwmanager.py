print("Password Generator:")
#x is acting as a pool of data that can be randomly generated
import random
x = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789"

number = input('Number of Passwords:')
number = int(number)

length = input('Password Length:')
length = int(length)

for p in range(number):
    password = " "
    for count in range(length): 
        password += random.choice(x)
    print(password)