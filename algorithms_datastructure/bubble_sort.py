
def bubble_sort(array:list[int]):
    sorted = False
    unsorted_len_idx = len(array)

    while not sorted:
        sorted = True
        for i in range(unsorted_len_idx-1):
            if array[i] <= array[i+1]:
                continue
            else:
                array[i], array[i+1] = array[i+1], array[i]
                sorted = False
        unsorted_len_idx -= 1

    return array
        
if __name__ == "__main__":
    unsorted_array = [5,3,2,1]

    print(bubble_sort(unsorted_array))
    assert bubble_sort(unsorted_array) == [1,2,3,5]