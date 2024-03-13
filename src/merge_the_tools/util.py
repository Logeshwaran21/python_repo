import logging
logging.basicConfig(level=logging.DEBUG, format="%(message)s" )
def merge_tools(string_input,k):
    n= len(string_input)
    for i in range(0,n,k):
        sub_string = string_input[i:i+k]
        unique_list=[]
        for j in sub_string:
            if j not in unique_list:
                unique_list.append(j)
        result=(''.join(unique_list))
        logging.debug(result)
    return result



