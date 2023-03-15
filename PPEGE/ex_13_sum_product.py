
# reproduce sum() and create a product(), argument should be a list of ints
def get_sum(loi: list[int])->int:
    if len(loi) == 0:
        return 0
    else:
        return loi[0] + get_sum(loi[1:])

def get_product(loi: list[int])->int:
    if len(loi) == 0:
        return 1
    else:
        return loi[0] * get_product(loi[1:])

if __name__ == "__main__":
    assert get_sum([1,2,3]) == 6
    assert get_sum([]) == 0
    
    assert get_product([1,1,1]) == 1
    assert get_product([]) == 1
    assert get_product([1,2,3]) == 6
    