# Eric Lehmphul

# Assignment 1

#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

high_score = 95

# Get the test scores.
test1 = float(input('Enter the score for test 1: '))
test2 = float(input('Enter the score for test 2: '))
test3 = float(input('Enter the score for test 3: '))

# Calculate the average test score.
average = (test1 + test2 + test3) / 3
# Print the average.
print('The average score is ', average)
# If the average is a high score,
# congratulate the user.
if average >= high_score:
    print('Congratulations!')
    print('That is a great average!')

#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles. 

# Get user input
length1 = float(input('Please enter the length of rectangle 1: '))
width1 = float(input('Please enter the width of rectangle 1: '))
length2 = float(input('Please enter the length of rectangle 2: '))
width2 = float(input('Please enter the width of rectangle 2: '))

# Find area
area1 = length1 * width1
area2 = length2 * width2

# Print area to user
print("The area of rectangle 1 is ", area1)
print("The area of rectangle 2 is ", area2)


#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.  

#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"

# Get user input
name = input('Please enter your first name: ') # input is a string data type by default
age = int(input('Please enter your age: '))

# Print message
print("Happy birthday, " + name + "! You are " + str(age) + " years old today!")

