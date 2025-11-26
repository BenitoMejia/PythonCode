# ---------------------------------------------
# BMI Calculator Program
# Get user input for name, height and weight
# Make sure height and weight are positive
# Calculate and display BMI value and BMI category
# ---------------------------------------------

def getPositiveNumber(prompt):
    """
    Ask the user for a positive number using a while loop.
    Repeats until the user enters a value greater than 0.
    """
    value = 0
    while value <= 0:
        # Prompt the user for input
        value = float(input(prompt))
        # Check if input is positive
        if value <= 0:
            print("Please enter a positive number greater than zero.")
    return value

def calculatebmi(weight, height):
    bmi = (weight/(height*height))*703
    return bmi

def getCategory(bmi):
    """
    Determine the BMI category based on value.
    """
    category = ""
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return category

# --- Main Program ---
print("BMI Calculator (Python)")

# Ask for user's name
name = input("Enter your name: ")

# Get valid positive inputs for weight and height
weight = getPositiveNumber("Enter weight (lbs): ")
height = getPositiveNumber("Enter height (inches): ")

bmiValue = calculatebmi(weight, height)
truebmi = round(bmiValue)
category = getCategory(bmiValue)

print(f"Name:{name}", f"Your BMI is:{truebmi}", f"Status:{category}")
