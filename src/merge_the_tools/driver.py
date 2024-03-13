import logging
logging.basicConfig(level=logging.DEBUG, format="%(message)s" )
from util import merge_tools

string_input= (input("Enter the string value: "))
k = int(input("Enter the factor value: "))

merge_tools(string_input,k)
