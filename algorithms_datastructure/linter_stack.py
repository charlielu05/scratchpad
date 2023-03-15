
def check_lint(string:str)->str:
    linter_dict = {')': '(',
                    ']':'['}
    
    lint_stack = []

    for value in string:
        if value in {'(','['}:
            lint_stack.append(value)
        if value in {']',')'}:
            if len(lint_stack) <= 0:
                return "missing opening braces"
            if lint_stack.pop() != linter_dict.get(value): 
                return "Wrong closing braces"


if __name__ == "__main__":
    test_string = "var x = { y: [1,2,3]})"
    wrong_closing = "[var x = { y: [1,2,3]))"

    assert check_lint(test_string) == "missing opening braces" 

    assert check_lint(wrong_closing) == "Wrong closing braces"