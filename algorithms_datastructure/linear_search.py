# binary search 

def linear_search(input_array:list, search_value:int)->int:
    for i,value in enumerate(input_array):
        if value == search_value:
            return i
        elif value > search_value:
            return None

    return None

if __name__ == "__main__":
    sorted_array = [3,17,75,80,202]
    sorted_array_2 = [3,17,80,202] 

    assert linear_search(sorted_array, 75) == 2
    assert linear_search(sorted_array_2, 75) is None

