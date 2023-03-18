# beging with a positive int: n
# if n is 1, sequence terminates 
# if n is even, next value is n /2
# if n is odd, next value is 3n + 1
from typing import List

def collatz(n: int)->List[int]:
    if n == 0:
        return []
    
    elif n == 1:
        return [1]
    
    # if even 
    elif n % 2 == 0:
        return [n] + collatz(n // 2)
    
    # if odd 
    else:
        return [n] + collatz(3 * n + 1)
    
if __name__ == "__main__":
    assert collatz(0) == []
    assert collatz(10) == [10, 5, 16, 8, 4, 2, 1]