# Making an Email Slicer Program Using Only Python
# This program will take an email as input and slice it to generate a username and domain.
# For example, if the input email is "abc@gmail.com", the output will be:
# Username: abc
# Domain: gmail.com

email = input("Enter your email: ")

index = email.index("@")

username = email[:index]
domain = email[index + 1:]

print("Username:", username)
print("Domain:", domain)
