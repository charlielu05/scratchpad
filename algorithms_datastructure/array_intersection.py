from functools import reduce

def array_intersection(array_1, array_2):
    array_1_dict = dict(zip(array_1, [True]*len(array_1)))

    # map to lambda
    intersection = map(lambda x: x if array_1_dict.get(x)==True else None, array_2)

    # reduce
    intersection_reduced = filter(lambda x: x != None, intersection)

    return list(intersection_reduced)



if __name__=="__main__":
    large_array = ["a", "b", "c","d", "e", "f"]
    small_array = ["b", "d", "f"]
    small_not_subet_array = ["h", "i", "a"]

    assert array_intersection(large_array, small_array) == ["b","d","f"]
    assert array_intersection(large_array, small_not_subet_array) == ["a"]
