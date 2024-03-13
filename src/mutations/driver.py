import logging
from python_repo.src.mutations.util import mutate_string
logging.basicConfig(level=logging.DEBUG, format="%(message)s" )

s = input("Enter the string: ")
i, c = input("enter the position and character: ").split()
s_new = mutate_string(s, int(i), c)
