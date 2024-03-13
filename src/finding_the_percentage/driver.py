import logging
from util import read_student_marks, calculate_average

logging.basicConfig(level=logging.DEBUG, format="%(message)s" )
student_marks = read_student_marks()
query_name = input("Enter the name of the student to calculate average: ")

# Call function from util.py to calculate average score
average_score = calculate_average(student_marks, query_name)

# logging the average score with two decimal places
logging.debug(f"The average of {query_name} is {average_score:.2f}")

