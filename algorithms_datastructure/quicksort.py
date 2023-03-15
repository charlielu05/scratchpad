from dataclasses import dataclass, field
from typing import List

class QuickSort:

    def __init__(self, array):
        self.array = array

    def sort(self, left_pointer,right_pointer):
        # pivot is always the item to the right
        pivot_idx = right_pointer
        pivot = self.array[right_pointer]
        right_pointer -= 1

        while True:

            while self.array[left_pointer] < pivot and left_pointer <= right_pointer:
                left_pointer += 1
            
            while self.array[right_pointer] > pivot and left_pointer <= right_pointer:
                right_pointer -= 1

            if left_pointer >= right_pointer:
                break

            else:
                self.array[left_pointer], self.array[right_pointer] = self.array[right_pointer], self.array[left_pointer]

            
        self.array[left_pointer], self.array[pivot_idx] = self.array[pivot_idx], self.array[left_pointer]

        return left_pointer
    
    def quicksort(self, left_pointer, right_pointer):
        # basecase
        if len(self.array[left_pointer:right_pointer]) == 0:
            return self.array
        
        # get left pointer as pivot
        pivot_pointer = self.sort(left_pointer, right_pointer)

        # recurse on left side of pivot
        self.quicksort(left_pointer, pivot_pointer-1)

        # recurse on right side of pivot
        self.quicksort(pivot_pointer+1, right_pointer)

if __name__=="__main__":
    test_array = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]

    sort = QuickSort(test_array)
    sort.quicksort(0, len(test_array) - 1)
    print(sort.array)
    #assert quicksort(test_array) == [2,3,5,12,21,78,274]