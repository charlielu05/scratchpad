# --------------
# User Instructions
#
# Write a function, compile_word(word), that compiles a word
# of UPPERCASE letters as numeric digits. For example:
# compile_word('YOU') => '(1*U + 10*O +100*Y)' 
# Non-uppercase words should remain unchaged.

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    reversed = word[::-1]

    compiled = [f"{10**n}*{letter}" for n, letter in enumerate(reversed)]

    return '(' + '+'.join(compiled) + ')'

if __name__ == "__main__":
    assert compile_word('YOU') == '(1*U+10*O+100*Y)'