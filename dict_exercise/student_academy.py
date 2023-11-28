rows = int(input())
students_data = {}
good_students = {}
for row in range(rows):
    student_name = input()
    grade_data = float(input())
    if student_name not in students_data:
        students_data[student_name] = []
    students_data[student_name].append(grade_data)

for student, grade in students_data.items():
    final_grade = sum(grade) / len(grade)
    if final_grade >= 4.50:
        good_students[student] = final_grade

for key, value in good_students.items():
    print(f'{key} -> {value:.2f}')