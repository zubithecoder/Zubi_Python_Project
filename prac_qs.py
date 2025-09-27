""" Practice Questions: (15) """
# Q 1-5 : Strings

# Question no 1: 
# Write a program to reverse a string.
text = "hello"
reversed_text = text [::-1]
print(reversed_text)
# Output: olleh

# Question no 2:
# Count the number of vowels in a given string.
# Input from user
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
print("Number of vowels:", count)
# Output: Number of vowels: 3

# Question no 3:
# Check if a string is a palindrome
text = "madam"
text = text[::-1]
if text == text:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
# Or
text = input("Enter a string: ")
text == text.replace(" ", "").lower()
if text == text[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not palindrome")
# Output: (depends on what you input)

# Question no 4:
# Take a name from the user and greet with "Hello, [Name]!"
name = input("Enter your name: ")
print("Hello", name + "!")

# Questions no 5:
# Replace all spaces with hyphens in a string.
# Hyphens are - and spaces are " "
text = input("Enter a string: ")
new_text = text.replace(" ", "-")
print("String after replacing places with hyphens:", new_text)

# Q 6-8 : Booleans and Comparisons

# Question no 6:
# Q 6-8 : Booleans and Comparison:
# Question no 6:
# Check if a number is even using a boolean condition.
# Ask the use r to enter an operator
operator = input("Enter an operator (+, -, *, /): ")
# Ask the user to enter two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
# Perform the calculation based on the operator
if operator == "+":
    result = num1 + num2
    print("Result:", result)
elif operator == "-":
    result = num1 - num2
    print("Result:", result)
elif operator == "*":
    result = num1 * num2
    print("Result:", result)
elif operator == "/":
    result = num1 / num2
    print("Result:", result)
else:
    print("Invalid operator")

# Question no 7:
# Evaluate and print the result of (10 > 5 and 5 < 2).
result = (10 > 5 and 5 < 2)
print(result)

# Question no 8:
# Ask the user to enter a string and check if it is empty.
user_input = input("Enter a string: ")
if user_input == "":
    print("The string is empty.")
else:
    print("The string is not empty.") 

# Q 9-12 : Operators:
# Question no 9:
# Write a calculator that takes two numbers and an operator (+,-,*,/).
# Ask the user to enter the first number
num1 = int(input("Enter the first number: "))
# Ask the user to enter the operator
operator = input("Enter the operator: ")
# Ask the user to enter the second number
num2 = int(input("Enter the second number: "))
# Perform the calculationis:", num2)
if num1 == num2:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")
# Check if the number is between 1 and 10 using logical operator "and"
# Ask the user to enter a number
num = int(input("Enter a number: "))
# Check if the number is between 1 and 10 using logical operator "and"
if num >= 1 and num <= 10:
    print("The number is between 1 and 10. ")
else:
    print("The number is not between 1 and 10. ")

# Question no 10:
# Use floor division to divide 23 by 5
result = 23 // 5
print("Result:", result)

# Question no 11:
# Write a program that compares two numbers and prints the larger.
# Ask the user to enter two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
# Compare the numbers 
if num1 > num2:
    print("The larger number is:", num1)
elif num2 > num1:
    print("The larger number # Check if a number is even using a boolean condition.")
number = int(input("Enter a number: "))
is_even = number % 2 == 0
if is_even:
    print(str(number) + " is even")
else:
    print(str(number) + " is odd")

# Question no 12:
# Use logical operators to check if a number is between 1 and 10.
# Ask the user to enter a number
num = int(input("Enter a number: "))

# Q 13-15 : if,elif,else,match:
# Question no 13:
# Write a program to check if a number is positive, negative, or zero.
# Ask the user to enter a number
num = int(input("Enter a number: "))
# Check if the number is positive, negative, or zero
if num > 0:
    print("The number is positive. ")
elif num < 0:
    print("The number is negative. ")
else:
    print("The number is zero. ")

# Question no 14:
# Use if-elif-else to assign a grade (A/B/C/F) based on marks.
# Ask the user to enter marks
marks = int(input("Enter your marks (0-100): "))
# Grade based on marks
if marks >= 90:
    print("Your grade is A. ")
elif marks >= 75:
    print("Your grade is B. ")
elif marks >= 50:
    print("Your grade is C. ")
else:
    print("Your grade is F. ")

# Question no 15:
# Take a number from 1 to 7 and print the corresponding weekday using match.
# Ask the user to enter a number
day = int(input("Enter a number between 1 and 7: "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid input. Please enter a number between 1 and 7. ")



print("-----------------------------")
