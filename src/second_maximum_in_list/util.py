import logging
logging.basicConfig(level=logging.DEBUG, format="%(message)s")
def second_maximum(n,List):
    num = int(input("Enter the number of values: "))
    List_Input = list(map(int, input("Enter the values: ").split()))
    for i in range(len(List)):
        for j in range(i + 1, len(List)):
            if List[i] > List[j]:
                List[i], List[j] = List[j], List[i]
    second_max=List[-2]
    logging.debug(f"The second largest value is {second_max}")
    return second_max

