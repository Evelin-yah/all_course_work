command = input()
courses_data = {}

while command != 'end':
    course_name, student_name = command.split(' : ')
    if course_name not in courses_data:
        courses_data[course_name] = []
    courses_data[course_name].append(student_name)

    command = input()

for course, students in courses_data.items():
    print(f'{course}: {len(students)}')
    for student in students:
        print(f'-- {student}')