
def recurse_sum(array:list)->int:
    if len(array) == 1:
        return array[0]

    return array[0] + recurse_sum(array[1:])

if __name__=="__main__":
    test_array = [1,2,3,4]
    
    print(recurse_sum(test_array))