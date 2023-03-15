
# function to find mode of list of int
def mode(loi: list[int])->int:
    num_count = {}
    max_count = 0
    max_number = 0
    
    for number in loi:
        if num_count.get(number) is None:
            num_count[number] = 0
        else:
            num_count[number] = num_count.get(number) + 1
        
        # check if mode
        if num_count[number] > max_count:
            max_number = number
            max_count = num_count[number]
            
    return max_number
    
if __name__ == "__main__":
    assert mode([1,1,2,3,4]) == 1
    assert mode([1,2,3,4,4]) == 4
