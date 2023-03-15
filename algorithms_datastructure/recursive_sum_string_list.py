
def sum_list(string:list[str])->int:
    if len(string) == 0:
        return 0

    return len(string[0]) + sum_list(string[1:])

if __name__=="__main__":
    string = ["ab","c","def","ghij"]
    
    assert sum_list(string) == 10