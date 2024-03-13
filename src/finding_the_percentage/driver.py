import logging
from util import read_student_marks, calculate_average

logging.basicConfig(level=logging.DEBUG, format="%(message)s" )

student_marks = read_student_marks()
query_name = input("Enter the name of the student to calculate average: ")
average_score = calculate_average(student_marks, query_name)
logging.info(f"The average of {query_name} is {average_score:.2f}")

