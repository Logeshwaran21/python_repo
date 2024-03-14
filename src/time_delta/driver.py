from util import time_delta
if __name__ == '__main__':
    t = int(input("Enter the number of test cases: "))

    for t_itr in range(t):
        t1 = input("Enter datetime string 1: ")
        t2 = input("Enter datetime string 2: ")
        time_delta(t1, t2)

