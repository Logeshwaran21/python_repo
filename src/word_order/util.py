import logging

logging.basicConfig(level=logging.DEBUG, format="%(message)s")
def word_order(n):

    word=[]
    count=[]
    for i in range(n):
        w=input("Enter the word: ")
        if w not in word:
            word.append(w)
            count.append(1)
        else:
            count[word.index(w)]+=1
    res = ""
    for i in count:
        res += str(i) + " "
    logging.debug(len(count))
    logging.debug(res)


