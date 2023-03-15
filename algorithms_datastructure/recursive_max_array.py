
def max_array(array:list[int])->int:
    print("unoptimized calls")

    if len(array) == 1:
        return array[0]
    if array[0] > max_array(array[1:]):
        return array[0]
    else:
        return max_array(array[1:])

def max_array_optimal(array:list[int])->int:
    print("optimized calls")

    if len(array) == 1:
        return array[0]
    max_of_array = max_array_optimal(array[1:])

    if array[0] > max_of_array:
        return array[0]
    else:
        return max_of_array


if __name__=="__main__":
    test_array = [1,3,2,5]

    assert max_array(test_array) == 5

    assert max_array_optimal(test_array) == 5