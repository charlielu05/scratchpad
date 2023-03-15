import string

def missing_letter(array)->str:
    array_dict = {}

    for val in array:
        array_dict[val] = True

    for alphabet in string.ascii_lowercase:
        if array_dict.get(alphabet) is not True:
            return alphabet

if __name__=="__main__":
    # missing letter is f
    array = "the quick brown box jumps over a lazy dog"

    print(missing_letter((array)))
    assert missing_letter(array) == 'f'