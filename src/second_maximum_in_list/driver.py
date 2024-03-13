from python_repo.src.second_maximum_in_list.util import second_maximum
import logging
logging.basicConfig(level=logging.DEBUG, format="%(message)s")
num= int(input("Enter the number of values: "))
List_Input = list(map(int, input("Enter the values: ").split()))
logging.debug(f"The second_maximum in the list is {second_maximum(num,List_Input)}")