# given two sorted list, merge them into one single list 
from typing import List
    
def merge_two_list(list_one:List[int], list_two:List[int])->List[int]:
    if (len(list_one) == 0) and (len(list_two) == 0):
        return []
    elif (len(list_one) == 0) and (len(list_two) != 0):
        return list_two
    elif (len(list_one) != 0) and (len(list_two) == 0):
        return list_one
    elif (list_one[0] < list_two[0]):
        return [list_one[0]] + merge_two_list(list_one[1:], list_two)
    else:
        return [list_two[0]] + merge_two_list(list_one, list_two[1:])
    

if __name__ == "__main__":
    LIST_ONE = [1,3,5,7,9]
    LIST_TWO = [2,4,6,8]
    assert merge_two_list([1,3,5,7,9], [2,4,6,8]) == sorted(LIST_ONE + LIST_TWO)
    