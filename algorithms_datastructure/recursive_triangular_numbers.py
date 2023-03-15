
def triangular_number(number:int)->int:
    if number == 1:
        return 1
    return number + triangular_number(number - 1)

if __name__=="__main__":
    n = 7
    assert triangular_number(n) == 28