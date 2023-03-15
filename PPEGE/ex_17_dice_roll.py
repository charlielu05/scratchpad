
# simulates rolling number of six sided dices
# and adding up the results
import random

def dice(num_dice:int)->int:
    return sum([random.randint(1,6) for x in range(num_dice)])

if __name__ == "__main__":
    assert 1 <= dice(1) <= 6
    assert 2 <= dice(2) <= 12
    assert 3 <= dice(3) <= 18