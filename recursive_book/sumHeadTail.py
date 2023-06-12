# recursive sum
from typing import List

def sum_recurse(loi:List[int])->int:
    if len(loi) == 0:
        return 0
    else:
        return loi[0] + sum_recurse(loi[1:])

assert sum_recurse([1,2,3]) == 6

# reverse string

def reverse_str(string:str)->str:
    if len(string) == 0:
        return ''
    else:
        head = string[0]
        tail = string[1:]
        
        return reverse_str(tail) + head
    
assert reverse_str('cat') == 'tac'

def is_palindrome(string:str)->bool:
    if len(string) == 0 or len(string) == 1:
        return True
    else:
        head = string[0]
        mid = string[1:-1]
        tail = string[-1]
        
        return head == tail and is_palindrome(mid)

assert is_palindrome('tacocat') == True
assert is_palindrome('panama') == False