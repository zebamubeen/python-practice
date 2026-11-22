name = input("Enter student's name: ")
marks = float(input("Enter marks (out of 100): "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "F"

print(f"\nStudent: {name}")
print(f"Marks: {marks}")
print(f"Grade: {grade}")

if marks >= 40:
    print("Result: Pass ✅")
else:
    print("Result: Fail ❌")