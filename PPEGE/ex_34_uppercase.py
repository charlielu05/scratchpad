# given a string, convert only the lowercase letters to uppercase
import string

ascii_lowercase = string.ascii_lowercase

lower_upper = {letter : letter.upper() 
               for letter 
               in ascii_lowercase}

def to_upper(input_string:str)->str:
    if len(input_string) == 0:
        return ''
    else:
        return lower_upper.get(input_string[0], input_string[0]) + to_upper(input_string[1:])
    

if __name__ == "__main__":
    assert to_upper('Hello') == 'HELLO'