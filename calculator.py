# Making a Calculator Using only Python
operator = input("Enter operator (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
else:
    print(f"{operator} is not a valid operator!")

"""
If you want to update you can use 
        print(round(result))
instead of 
        print(result)
So in this way you wil not gonna get long answers of divisions "/" after the decimal point and 
if you want just 3 letters after the decimal point just write this instead 
        print(round(result, 3))
In this way you will gonna get only 3 numbers after the decimal point
"""
