
def stack_reverse_str(string:str)->str:
    stack = []

    for c in string:
        stack.append(c)
    
    reversed_string = []
    
    while len(stack) != 0:
        reversed_string.append(stack.pop())
    
    print(''.join(reversed_string))
    return ''.join(reversed_string)

if __name__=="__main__":
    test_string = "abcde" 

    assert stack_reverse_str(test_string) == 'edcba'