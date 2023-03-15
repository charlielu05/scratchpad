
def count_x(string:str)->int:
    if len(string) == 0: 
        return 0

    if string[0] == 'x':
        return 1 + count_x(string[1:])
    else:
        return count_x(string[1:])

if __name__=="__main__":
    string = "abxdexgx"
    
    assert count_x(string) == 3