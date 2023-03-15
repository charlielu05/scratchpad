
def find_x(string:str, idx=0)->int:
    
    if string[idx] == 'x':
        return idx
    else:
        return find_x(string, idx+1)

if __name__=="__main__":
    string = "abcxefgx"

    assert find_x(string) == 3