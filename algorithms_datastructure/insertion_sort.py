
def insertion_sort(array: list[int])->list[int]:
    # compare each index to the index to the left of it
    # swap index with left if index is smaller
    array_length = len(array)

    for idx in range(array_length):
        comp_idx = idx - 1 
        while comp_idx != -1 and array[idx] < array[comp_idx]:
            array[comp_idx], array[idx] = array[idx], array[comp_idx]
            idx -= 1
            comp_idx -= 1
    
    return array



if __name__ == "__main__":
    unsorted_array = [5,3,2,1]

    print(insertion_sort(unsorted_array))
    assert insertion_sort(unsorted_array) == [1,2,3,5]