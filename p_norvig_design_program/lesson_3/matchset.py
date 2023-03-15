#----------------
# User Instructions
#
# The function, matchset, takes a pattern and a text as input
# and returns a set of remainders. For example, if matchset 
# were called with the pattern star(lit(a)) and the text 
# 'aaab', matchset would return a set with elements 
# {'aaab', 'aab', 'ab', 'b'}, since a* can consume one, two
# or all three of the a's in the text.
#
# Your job is to complete this function by filling in the 
# 'dot' and 'oneof' operators to return the correct set of 
# remainders.
#
# dot:   matches any character.
# oneof: matches any of the characters in the string it is 
#        called with. oneof('abc') will match a or b or c.

def matchset(pattern, text):
    "Match pattern at start of text; return a set of remainders of text."
    op, x, y = components(pattern)
    if 'lit' == op:
        return set([text[len(x):]]) if text.startswith(x) else null
    elif 'seq' == op:
        # x is the first pattern to match
        return set(t2 for t1 in matchset(x, text) for t2 in matchset(y, t1))
    elif 'alt' == op:
        return matchset(x, text) | matchset(y, text)
    elif 'dot' == op:
        return set([text[1:]]) if text else null
    elif 'oneof' == op:
        return set([text[1:]]) if text[0] in x else null
    elif 'eol' == op:
        return set(['']) if text == '' else null
    elif 'star' == op:
        return (set([text]) |
                set(t2 for t1 in matchset(x, text)
                    for t2 in matchset(pattern, t1) if t1 != text))
    else:
        raise ValueError('unknown pattern: %s' % pattern)
        
null = frozenset()

def components(pattern):
    "Return the op, x, and y arguments; x and y are None if missing."
    x = pattern[1] if len(pattern) > 1 else None
    y = pattern[2] if len(pattern) > 2 else None
    return pattern[0], x, y
   
def test():
    assert matchset(('lit', 'abc'), 'abcdef')            == set(['def'])
    # the literal 'hi' would be matched and the remainder returned, the lit 'there' would then be matched and remainder returned
    # t1: 'there nice to meet you'
    # t2: 'nice to meet you'
    assert matchset(('seq', ('lit', 'hi '),
                     ('lit', 'there ')), 
                   'hi there nice to meet you')          == set(['nice to meet you'])
    # alternative, either dog or cat
    assert matchset(('alt', ('lit', 'dog'), 
                    ('lit', 'cat')), 'dog and cat')      == set([' and cat'])
    assert matchset(('dot',), 'am i missing something?') == set(['m i missing something?'])
    assert matchset(('oneof', 'bac'), 'aabc123')           == set(['abc123'])
    assert matchset(('eol',),'')                         == set([''])
    assert matchset(('eol',),'not end of line')          == frozenset([])
    assert matchset(('star', ('lit', 'hey')), 'heyhey!') == set(['!', 'heyhey!', 'hey!'])
    
    return 'tests pass'

if __name__ == "__main__":
    print(test())

    
