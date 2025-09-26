# Assignment 1:

# Question number 1 :
# Input & Output
# Write a python program that asks the user for their name and age, then prints:
# "Hello [name]! You are [age] years old."
#Answer:
name = input("Enter your name:")
age = input("Enter your age:")
print(f"Hello, {name}! You are {age} years old.")

# Question number 2 :
# Variables & Basic Operations
# Write a program that takes two numbers as input, stores them in variables first_number and second_number, then prints their sum, difference, and product.
# Answer:
# Take input for the first number
First_number = float(input("Enter the first number:"))
# Take input for the second number
Second_number = float(input("Enter the second number: "))
# Calculate sum, difference, and product
Sumresult = First_number + Second_number
Difference_result = First_number - Second_number
Productresult = First_number * Second_number
# Print the results
print(f"Sum: {Sumresult}")
print(f"Difference: {Difference_result}")
print(f"Product: {Productresult}")

# Question number 3 :
# Comments
# Add appropriate comments to the following code to explain what each line does:
"""x = 5
y = 10
result = x + y
print(result)"""
# Answer:
# Assign the value 5 to the variable x
x = 5
# Assign the value 10 to the variable y
y = 10
# Calculate the sum of x and y and store the result in the variable result
result = x + y
# Print the value of the variable result
print(result)

# Question number 4 :
# f-strings (Format String Literals)
# Given two variables:
# item = "book"
# price = 15.99
# Use an f-string to print:
# "The [item] costs $[price]."
# Answer:
# Given variables
item = "book"
price = 15.99
# Use an f-string to print the desired output
print(f"The {item} costs ${price}.")

# Question number 5 :
# Input & Type Conversion
# Write a program that takes two numbers as input (as strings), converts them to integers, and prints their sum
# Answer:
# Take input for the first number as a string
First_number = str(input("Enter the first number:"))
# Take input for the second number as a string
Second_number = str(input("Enter the second number:"))
# Convert the input strings to integers
First_number = int("45")
Second_number = int("65")
# Calculate the sum of the two numbers
Sumresult = First_number + Second_number
# Print the sum
print(f"The sum of {First_number} and {Second_number} is {Sumresult}.")

# Question number 6 :
# Variable Naming & Output
# Correct the variable names (if needed) and print them:
"""1st_num = 10 
second-num = 20 
total = 1st_num + second_num 
print(total)"""
# Answer :
# Correct the variable names
First_num = 10
Second_num = 20
# Calculate the sum
total = First_num + Second_num
# Print the result
print(total)

# Question number 7 :
# Multi-line String & Comments
# Write a program that uses a multi-line string to store a short paragraph and includes a comment explaining its purpose
# Answer:
# Store a short paragraph in a multi-line string
paragraph = """This is a short paragraph.
It spans multiple lines.
Each line is separated by a newline character."""
# Print the paragraph
print(paragraph)

# Question number 8 :
# f-strings with Calculations
# Given radius = 7, use an f-string to print: "The area of the circle is [area]." (Use 3.14 for pi.)
# Answer:
# Given radius
radius = 7
# Calculate the area of the circle
area = 3.14 * radius**2
# Use an f-string to print the result
print(f"The area of the circle is {area}.")

# Question number 9 :
# Input with Prompt
# Write a program that asks the user for their favorite color using a custom prompt ("Enter your favorite color: ") and then prints it in uppercase.
# Answer:
# Ask the user for their favorite color
favorite_color = input("Enter your favorite color: ")
# Print the favorite color in uppercase
print(favorite_color.upper())

# Question number 10 :
# Combining Input, Variables, and f-strings
# Write a program that takes three inputs (first name, last name, and birth year), stores them in variables, and prints: "Your full name is [first] [last], and you are [age] years old."
# Answer:
# Take inputs for first name, last name, and birth year
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_year = int(input("Enter your birth year: "))
# Calculate the current age
current_year = 2025
age = current_year - birth_year
# Print the result using an f-string
print(f"Your full name is {first_name} {last_name}, and you are {age} years old.")
