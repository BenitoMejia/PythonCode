# This program asks for your name and calculates your average and highest test scores
# It contains several errors (syntax, runtime, and logic) for you to find and fix

print("Welcome to the Debugging Lab!")

name = input("Enter your name: ")
print("Hello " + name + "!" + " Let's calculate your test scores.")

scores = [85, 90, 78, 88, 92] #an object: pool of items

total = 0
for score in scores:
    total = total + score #adds up the total to every item in score

#average will the finial "total" and divide it by the len
average = total / len(scores) #len: number of items in an object
print("Your average score is:", average)

#loop will repeat until highest value is found
highest = 0
for s in scores:
    if s > highest: 
        highest = s 

print("Your highest score was:" + str(highest))