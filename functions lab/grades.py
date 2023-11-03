def solve_grade(grade_as_num):
    if 2.00 <= grade_as_num <= 2.99:
        return 'Fail'
    elif 3.00 <= grade_as_num <= 3.49:
        return 'Poor'
    elif 3.49 <= grade_as_num <= 4.49:
        return 'Good'
    elif 4.49 <= grade_as_num <= 5.49:
        return 'Very Good'
    elif 5.50 <= grade_as_num <= 6.00:
        return 'Excellent'

grade = float(input())

print(solve_grade(grade))
