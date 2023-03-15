def get_biggest(lon: list[int], biggest:int=None):
    if len(lon) == 0:
        return biggest
    current = lon[0]
    if biggest is None:
        biggest = current
    if current >= biggest:
        biggest = current
    return get_biggest(lon=lon[1:], biggest=biggest)    


def helper_biggest(lon: list[int], biggest:int):
    if len(lon) == 0:
        return biggest
    
    if lon[0] <= biggest:
        return helper_biggest(lon[1:], biggest)
    
    elif lon[0] >= biggest:
        biggest = lon[0]
        return helper_biggest(lon[1:], biggest)

# reproduce max()
def get_biggest_charlie(lon: list[int])->int:
    if len(lon) == 0:
        return None
    else:
        return helper_biggest(lon[1:], lon[0])
    

if __name__ == "__main__":
    a = [1,2,3,4]
    assert get_biggest(a) == 4
    
    b = []
    assert get_biggest(b) == None

    c = [-99, -20, -10]
    assert get_biggest(c) == -10
    
    d = [1,2]
    assert get_biggest(d) == 2