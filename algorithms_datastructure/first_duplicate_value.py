
def first_duplicate(array)->str:
    array_dict = {}

    for val in array:
        if array_dict.get(val) is None:
            array_dict[val] = True
        else:
            return val

if __name__=="__main__":
    array = ["a", "b", "c","d", "c", "e", "f"]

    assert first_duplicate(array) == "c"
