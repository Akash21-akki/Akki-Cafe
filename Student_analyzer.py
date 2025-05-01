# # Dictionary {}
student1 = {"name": "Amit", "roll": "Amit", "name": [80, 90, 85]}
print(student1["name"])
print(student1["roll"])
student2 = {"name": "Aman", "roll": 102, "marks": [81, 91, 86]}
student3 = {"name": "Amar", "roll": 103, "marks": [82, 91, 87]}

students = [student1, student2, student3] 

# Tuple ()
subjects = ("Maths", "Science", "English")

# Set {}
grades = {"A", "B", "C"}

# List []
averages = [sum(s["marks"]) / len(s["marks"]) for s in students]

topper = max(students, key=lambda s: sum(s["marks"]) / len(s["marks"]))

# Array ()
from array import array

all_marks = array('i', [mark for s in students for mark in s["marks"]])