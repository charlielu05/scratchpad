# encrypts string chars (A-Z) to a letter 13 characters ahead
# we can map int to unicode(A-Z) between 65 - 90
# if letter + 13 > 90 -> modulo by 90 and add to 65

def encrypt_function(secret_char:str)->str:
    if (ord(secret_char) < 65) or (ord(secret_char) > 90):
        return secret_char
    
    encrypted_char_int = ord(secret_char) + 13
    if encrypted_char_int <= 90:
        return chr(encrypted_char_int)

    return chr((encrypted_char_int % 90) + 64)
    
def encrypt(secret_string:str)->str:
    if len(secret_string) == 1:
        return encrypt_function(secret_string)
    else:
        return encrypt_function(secret_string[0]) + encrypt(secret_string[1:])
    
if __name__ == "__main__":
    assert encrypt('HELLO, WORLD') == 'URYYB, JBEYQ'