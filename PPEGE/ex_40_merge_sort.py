# given two sorted list, merge them into one single list 
from typing import List
    
def merge_two_list(list_one:List[int], list_two:List[int])->List[int]:
    merged_list = []
    
    

if __name__ == "__main__":
    LIST_ONE = [1,3,5,7,9]
    LIST_TWO = [2,4,6,8]
    assert merge_two_list([1,3,5,7,9], [2,4,6,8]) == sorted(LIST_ONE + LIST_TWO)