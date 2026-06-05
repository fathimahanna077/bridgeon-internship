# Input 10 student marks

marks = []

for i in range(10):
    mark = int(input(f"Enter mark {i + 1}: "))
    marks.append(mark)

# Average
average = sum(marks) / len(marks)

# Highest and Lowest
highest = max(marks)
lowest = min(marks)

# Remove duplicates
unique_marks = list(set(marks))
unique_marks.sort()

# Marks above average using list comprehension
above_average = [mark for mark in marks if mark > average]

# Formatted Report
print("\n" + "=" * 40)
print("      STUDENT MARKS REPORT")
print("=" * 40)

print(f"Original Marks      : {marks}")
print(f"Unique Marks        : {unique_marks}")
print(f"Average Mark        : {average:.2f}")
print(f"Highest Mark        : {highest}")
print(f"Lowest Mark         : {lowest}")
print(f"Marks Above Average : {above_average}")

print("=" * 40)