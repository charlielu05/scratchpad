
# generate random password with at least 12 characters in length
import string
import random

def generate_password(length:int)->str:
    if length < 12:
        length = 12
        
    special_characters = "~!@#$%^&*()_+"
    lower_letters = string.ascii_lowercase
    upper_letters = string.ascii_uppercase
    numbers = "0123456789"
    
    # must haves
    required = [random.choice(special_characters),
                       random.choice(lower_letters),
                       random.choice(upper_letters),
                       random.choice(numbers)]
    
    # fills
    fill_count = length - 4
    fill = [random.choice(random.choice([special_characters, lower_letters, upper_letters, numbers])) 
            for _ in range(fill_count)]
    combined = required + fill
    random.shuffle(combined)
    
    return ''.join(combined)

if __name__ == "__main__":
    print(generate_password(12))