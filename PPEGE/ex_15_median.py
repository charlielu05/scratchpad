
from ex_14_average import average
        
# function to find the median value
def get_median(loi: list[int])->int:
    length_of_list = len(loi)
    sorted_list = sorted(loi)
    
    if length_of_list == 0:
        return None
    
    if length_of_list % 2 == 0:
        # even, average of two numbers
        midpoint = length_of_list // 2
        
        return average([sorted_list[midpoint-1], sorted_list[midpoint]])
    
    else:
        # odd, just take mid number    
        return sorted_list[length_of_list // 2]

if __name__ == "__main__":
    assert get_median([]) == None
    assert get_median([1,2,3]) == 2
    assert get_median([1,2,2,3]) == 2
    