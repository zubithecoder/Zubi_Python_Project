# Right Angled Triangle Pattern
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("w", end=" ")
    print()



# Left Angled Triangle Pattern
rows = 5
for i in range(1, rows+1):
    print("  " * (rows - i), end="")     
    for j in range(1, i+1):
        print("s", end=" ")
    print()





# Pyramid Pattern
rows = 5
for i in range(1, rows+1):
    print(" " * (rows - i), end="")
    for j in range(1, i+1):
        print("i", end=" ")
    print()

