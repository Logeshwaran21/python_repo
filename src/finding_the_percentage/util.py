def read_student_marks():
    n = int(input("Enter the number of students? "))
    student_marks = {}
    for _ in range(n):
        name, *line = input("Enter the name of the student and their marks: ").split()
        scores = list(map(float, line))
        student_marks[name] = scores
    return student_marks

def calculate_average(student_marks, query_name):
    # Calculate average score for the queried student
    average_score = sum(student_marks[query_name]) / len(student_marks[query_name])
    return average_score
