from functools import reduce

def hash_index_subset(large:list[str], small:list[str])->bool:
    hash_dict = dict(zip(large, [True]*len(large)))
    
    # map to lambda
    small_in_large = map(lambda x: hash_dict.get(x), small)

    # reduce 
    small_in_large_bool = reduce(lambda x,y: x and y, small_in_large)

    return small_in_large_bool

if __name__=="__main__":
    large_array = ["a", "b", "c","d", "e", "f"]
    small_array = ["b", "d", "f"]
    small_not_subet_array = ["h", "i", "a"]

    assert hash_index_subset(large_array, small_array) is True
    assert hash_index_subset(large_array, small_not_subet_array) is None
