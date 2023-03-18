# given a list of objects, shuffle them in place
from typing import List 
import random 

def shuffle(loo:List[object])->List[object]:
    for idx, _ in enumerate(loo):
        rand_idx = random.randint(0, len(loo) - 1)
        loo[idx], loo[rand_idx] = loo[rand_idx], loo[idx]

    return loo

if __name__ == "__main__":
    assert len(shuffle([1,2,3])) == 3
    