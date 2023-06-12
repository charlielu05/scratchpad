# Using head-tail technique, create recursive concat() function.
# arg is an array of string and returns strings concated together into single string.

from typing import List

def concat(los:List[str])->str:
    if len(los) == 1:
        return los[0]
    else:
        head = los[0]
        tail = los[1:]
        return head + concat(tail)
    
assert concat(['Hello', 'World']) == 'HelloWorld'

# using head-tail, create recursive product() function, list of int as input

def product(loi:List[int])->int:
    if len(loi) == 1:
        return loi[0]
    else:
        head = loi[0]
        tail = loi[1:]
        return head * product(tail)
    
assert product([1,2,3]) == 6