
def get_sum(loi: list[int,float]):
    if len(loi) == 0:
        return 0
    else:
        return loi[0] + get_sum(loi[1:])
    
# create an average function, taking list of int and floats as input
def average(lon: list[int,float])->int:
    if len(lon) == 0:
        return None
    else:
        return get_sum(lon) / len(lon)
        

if __name__ == "__main__":
    assert average([1,2,3]) == 2
    assert average([]) == None
    
    assert average([2,2,2]) == 2
    assert average([1,1000,1]) == 334