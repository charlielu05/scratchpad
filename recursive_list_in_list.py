# recurssion for creating a list of list 
from typing import List

def list_of_list(input_list:List, list_length:int)->List[List[str]]:
    # base case is the list is shorter than list_length
    if len(input_list) <= list_length:
        return [input_list]
        
    # recurse
    else:
        return [input_list[:list_length]] + list_of_list(input_list[list_length:], list_length)
    
if __name__=="__main__":
    test_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    
    LIST_LENGTH = 2
    
    a = list_of_list(test_list, LIST_LENGTH)
    
    print(a)