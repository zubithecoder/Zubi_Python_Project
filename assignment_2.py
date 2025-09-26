# Assignment number 2:
# ~~~~~~~~~ Student Performance Tracker ~~~~~~~~~

# ---------- Step 1: Data Entry Module ----------
students = {}
roll_numbers = set()

# Sample data (replace this with dynamic input in a local environment)
sample_data = [
    (101, "Ali", (78, 85, 90)),
    (102, "Sara", (88, 92, 79)),
    (103, "Ahmed", (60, 70, 65))
]

for data in sample_data:
    roll, name, marks = data
    if roll not in roll_numbers:
        roll_numbers.add(roll)
        students[roll] = (name, marks)

# ---------- Step 2: Display Module ----------
print("\n--- Student Records ---")
for roll, data in students.items():
    print(f"\nRoll No: {roll}")
    print(f"Name: {data[0]}")
    print(f"Marks: {data[1][0]}, {data[1][1]}, {data[1][2]}")

# ---------- Step 3: Performance Analysis ----------

def calculate_total(marks_tuple):
    total = 0
    for mark in marks_tuple:
        total = total + mark
    return total

def calculate_average(marks_tuple):
    total = calculate_total(marks_tuple)
    average = total / 3  # since we know there are 3 subjects
    return average

def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

# ---------- Step 4: Summary Report ----------
print("\n--- Summary Report ---")
for roll, data in students.items():
    name, marks = data
    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = get_grade(average)

    print(f"\nRoll No: {roll}")
    print(f"Name: {name}")
    print(f"Total Marks: {total}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")

# ---------- Reflections ----------
# What was the most difficult part?
# - Handling the data without using built-in functions like sum(), len(), etc.
#
# What did you learn about data structures?
# - Learned how to use list, set, tuple, and dictionary together in a real-world task.
# - Understood how to loop through and access values stored in different data structures.

