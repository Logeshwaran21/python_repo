from util import read_student_marks, calculate_average
student_marks = read_student_marks()
query_name = input("Enter the name of the student to calculate average: ")
# Call function from util.py to calculate average score
average_score = calculate_average(student_marks, query_name)
# Print the average score with two decimal places
print(f"The average of {query_name} is {average_score:.2f}")

