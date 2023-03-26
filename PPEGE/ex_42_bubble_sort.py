# implement bubble sort
from typing import List

def bubble_sort(lon:List[int]):
    j = len(lon) - 1
    while j != 0:
        for i in range(j):
            if lon[i] > lon[j]:
                lon[i], lon[j] = lon[j], lon[i]
        j -= 1

    return lon

if __name__ == "__main__":
    assert bubble_sort([9,3,1,4,5]) == sorted([9,3,1,4,5])
