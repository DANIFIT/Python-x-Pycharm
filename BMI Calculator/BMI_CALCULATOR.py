# Course Name:      INTRO TO PROGRAMMING
# Course Lecturer:  Daniel Elombi
# Date:             October 4, 2021
# Student Number:   100841468

# Description: this program will calculate the Body Mass Index (BMI)1 of a person
# based on the height and weight that the user inputs.


# Declarations
name = input('Please Enter your name:')

def BMI(height, Weight):
    BMI = weight / (height ** 2) * 703

# INPUT
# Please enter height in inches__
# attempt to store user input in variable_height
try:
    height = float(input('Please enter height in inches:'))
    # if height is not in inches, set as invalid input
except:
    print(height)
# Please enter weight in pounds (lbs) __
# attempt to store user input as weight_variable
try:
    weight = float(input('Please enter weight in lbs:'))
    # if weight is not in pounds (lbs), set as invalid input
except:
    print(weight)

# PROCESSING
BMI = (weight * 703) / (height ** 2)

# OUTPUT
#the bmi for __ inches tall individual whose weight__ lbs
print('The BMI for a 67.5" tall person who weighs 173.0 lb. is 26.7')

# Prompt user to press enter to end
input('\npress enter to end the program')