name = input("Enter Student Name: ")
roll = int(input("Enter Roll Number: "))
math_score = float(input("Enter math Exam Score: "))
english_score = float(input("Enter english Exam Score: "))
physics_score = float(input("Enter physics Exam Score: "))
chemistry_score = float(input("Enter chemistry Exam Score: "))
python_score = float(input("Enter python Exam Score: "))
attendance = float(input("Enter Attendance Percentage: "))
assignment_score = float(input("Enter assignment Score: "))

total=math_score+english_score+physics_score+chemistry_score+python_score
percentage=total/5
average=total/5

if attendance>=75:
    attendance_status="Eligeble"
else:
    attendance_status="Not Eligeble"

if average>40:
    result_status="PASS"
else:
    result_status="FAILED"

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
else:
    grade = "D"



print()
print("Student Performance Dashboard")
print("=============================================================")
print("Marks Summary: ")
print(f"Math_score: {math_score}")
print(f"English_score: {english_score}")
print(f"Physics_score: {physics_score}")
print(f"Chemistry_score: {chemistry_score}")
print(f"Python_score: {python_score}")
print("=============================================================")
print(f"Average: {average}")
print("=============================================================")
print(f"Attendance: {attendance_status}")
print(f"Performace Index: {grade}")
print("=============================================================")
print(f"Result: {result_status}")
