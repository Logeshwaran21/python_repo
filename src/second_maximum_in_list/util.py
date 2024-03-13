import logging
logging.basicConfig(level=logging.DEBUG, format="%(message)s")
def second_maximum():
    n = int(input("Enter no. of values to be inserted: "))
    arr = list(map(int, input("Enter the values: ").split()))
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr[-2]


