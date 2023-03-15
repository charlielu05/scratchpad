
def selection_sort(array:list)->list:
    idx_len = len(array)

    for i in range(idx_len):
        lowest_idx = i
        for j in range(i, idx_len):
            if array[lowest_idx] > array[j]:
                lowest_idx = j
        if lowest_idx != i:
            array[i],array[lowest_idx] = array[lowest_idx], array[i]
    
    return array

if __name__ == "__main__":
    test_array = [1,2,7,4,3]

    assert selection_sort(test_array) == [1,2,3,4,7]