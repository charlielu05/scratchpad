# given an input dollar amount, create the number of change
# 1: penny,5: nickel,10: dime,25: quarters are available denominations
# input is int and represents cents 
from typing import List, Tuple

denominations = [('quarter', 25), ('dime', 10), ('nickel', 5), ('penny', 1)]

def give_change(cents:int)->dict:
    change = {}
    running_total = cents 
    
    for denomination, value in denominations:
        if running_total == 0:
            return change 
        
        change_qty = running_total // value 
        
        if change_qty != 0:
            change[denomination] = change_qty
            running_total = running_total % value 
    
    return change 
     
if __name__ == "__main__":
    assert give_change(127) == {'quarter': 5, 'penny': 2}