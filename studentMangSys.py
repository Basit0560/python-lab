# 4. Student Result Management System

# Maintain a student result system using sorting and searching:

# Add student details (ID, name, marks)

# Search student by ID

# Sort students by marks

# Count number of failed students

# Find Top 5 students


students = [
    {"id": 1, "marks": 85},
    {"id": 2, "marks": 40},
    {"id": 3, "marks": 90},
    {"id": 4, "marks": 30},
    {"id": 5, "marks": 70}
]

print("Sorted by marks:")
print(sorted(students, key=lambda x: x["marks"], reverse=True))

fail = sum(1 for s in students if s["marks"] < 40)
print("Fail count:", fail)

print("Top students:", sorted(students, key=lambda x: x["marks"], reverse=True)[:5])