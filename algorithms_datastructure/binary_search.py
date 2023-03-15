
def binary_search_recursion(input:list, search_value)->int:
    # start at middle index
    length = len(input)
    if length == 1:
        return None

    mid = int(length / 2)

    if input[mid] == search_value:
        return mid
    if input[mid] < search_value:
        return binary_search_recursion(input[mid:len(input)], search_value)
    if input[mid] > search_value:
        return binary_search_recursion(input[:mid], search_value)
    else:
        return None

def binary_search_iterative(input:list, search_value)->int:
    lower_bound = 0
    upper_bound = len(input) - 1

    while lower_bound <= upper_bound:
        mid = int((lower_bound+upper_bound) / 2)

        if input[mid] == search_value:
            return mid
        if input[mid] < search_value:
            lower_bound = mid + 1
        if input[mid] > search_value:
            upper_bound = mid - 1
    
    return None

if __name__ == "__main__":
    sorted_array = [3,17,75,80,202]

    assert binary_search_recursion(sorted_array, 75) == 2
    assert binary_search_recursion(sorted_array, 433) is None

    assert binary_search_iterative(sorted_array, 80) == 3
