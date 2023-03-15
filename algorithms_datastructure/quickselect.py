from quicksort import QuickSort

class QuickSort_2(QuickSort):

    def quickselect(self, kth_lowest, left_idx, right_idx):
        if len(self.array[left_idx:right_idx]) == 1:
            return self.array[left_idx]

        # get index of pivot
        pivot_idx = self.sort(left_idx, right_idx) 

        if pivot_idx == kth_lowest:
            # if kth_lowest and pivot is same location, we have found our vale
            return self.array[pivot_idx]

        elif pivot_idx > kth_lowest:
            self.quickselect(kth_lowest, left_idx, pivot_idx - 1)
               # if what we are looking for is to the left of the pivot
        else:
            self.quickselect(kth_lowest, pivot_idx + 1, right_idx)
     

if __name__=="__main__":
    # test kth value
    test_array_kth = [0, 50, 20, 10, 60, 30]
    sort2 = QuickSort_2(test_array_kth)
    print(sort2.quickselect(2, 0, len(test_array_kth) - 1))
