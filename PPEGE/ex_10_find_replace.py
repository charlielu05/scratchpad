
def findAndReplace(text:str, oldText:str, newText:str):
    i = 0
    replacedText = ''
    while i < len(text):
        if text[i:i + len(oldText)] == oldText:
            replacedText += newText
            i += len(oldText)
        else:
            replacedText += text[i]  
            i += 1
    
    return replacedText

assert findAndReplace('The fox', 'fox', 'dog') == 'The dog'
assert findAndReplace('fox', 'fox', 'dog') == 'dog'
assert findAndReplace('the Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'
        