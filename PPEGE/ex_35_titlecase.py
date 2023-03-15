# given a collection of strings, convert only the first letter of each word to uppercase
import string

ascii_lowercase = string.ascii_lowercase

lower_upper = {letter : letter.upper() 
               for letter 
               in ascii_lowercase}

def to_upper_title_case(input_string:str)->str:
    words_list = input_string.split()
    upper_case_list = []
    
    for word in words_list:
        upper_case_list.append(word[0].upper() + word[1:])
    
    return ' '.join(upper_case_list)
    

if __name__ == "__main__":
    assert to_upper_title_case('hello ba sheep') == 'Hello Ba Sheep'