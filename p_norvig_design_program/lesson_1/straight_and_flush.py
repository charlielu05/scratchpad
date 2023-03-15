# -----------
# User Instructions
# 
# Define two functions, straight(ranks) and flush(hand).
# Keep in mind that ranks will be ordered from largest
# to smallest.
from functools import reduce

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    # difference for each value is always 1 

    dif = [ranks[i] - ranks[i+1] for i in range(0, len(ranks)-1, 1)]
    
    return True if len(list(filter(lambda x: x==1, dif))) == len(ranks)-1 else False

def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r,s in hand]

    return True if len(set(suits)) == 1 else False
    
def test():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert flush(sf) == True
    assert flush(fk) == False

    return 'tests pass'

if __name__=="__main__":
    test()