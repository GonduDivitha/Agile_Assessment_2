# Student Marks Report Generator (No user input)

students = {
    "Arjun": [78, 82, 88],
    "Rahul": [90, 91, 89],
    "Kiran": [65, 70, 72],
    "Vikram": [50, 45, 60],
    "Manoj": [92, 95, 94],
    "Sanjay": [55, 58, 52]
}

def calculate_average(marks):
    return sum(marks) / len(marks)

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

report = []

for name, marks in students.items():
    avg = calculate_average(marks)
    grade = calculate_grade(avg)
    report.append((name, marks, avg, grade))

# sort by average descending
report.sort(key=lambda x: x[2], reverse=True)

print("STUDENT REPORT")
print("-" * 40)

for r in report:
    print(f"Name   : {r[0]}")
    print(f"Marks  : {r[1]}")
    print(f"Average: {r[2]:.2f}")
    print(f"Grade  : {r[3]}")
    print("-" * 40)

# class statistics
averages = [r[2] for r in report]
highest = max(averages)
lowest = min(averages)
class_avg = sum(averages) / len(averages)

print("\nCLASS STATISTICS")
print(f"Highest Average : {highest:.2f}")
print(f"Lowest Average  : {lowest:.2f}")
print(f"Class Average   : {class_avg:.2f}")

# save report to file
with open("student_report.txt", "w") as file:
    for r in report:
        file.write(f"{r[0]} | Avg: {r[2]:.2f} | Grade: {r[3]}\n")

print("\nReport saved to student_report.txt")
