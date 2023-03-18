# given a string, reverse the order

def reverse_string(input_string:str)->str:
    if len(input_string) == 0:
        return ''

    else:
        return input_string[-1] + reverse_string(input_string[:-1])

if __name__ == "__main__":
    assert reverse_string('Hello') == 'olleH'
