import string, re

def valid(f:str)->bool:
    "Formula f is valid iff it has no numbers with leading zero and evals true."
    try:
        return eval(f)
    except ZeroDivisionError:
        return False

if __name__ == "__main__":
    # true case
    assert valid("1+2==3") == True

    # false case
    assert valid("1/0==3") == False