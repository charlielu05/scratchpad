# Say, an organization issues ID cards to its employees with unique ID codes. The ID code for an employee named Jigarius Caesar looks as follows: CAJI202002196.

# Here’s how the ID code is derived:

# CA: First 2 characters of the employee’s last name.
# JI: First 2 characters of the employee’s first name.
# 2020: Full year of joining.
# 02: 2 digit representation of the month of joining.
# 19: Indicates that this is the 19th employee who joined in Feb 2020.
# This will have at least 2 digits, starting with 01, 02, and so on.
# 6: The last digit is a verification digit which is computed as follows:
# Take the numeric part of the ID code (without the verification digit).
# Sum all digits in odd positions. Say this is O.
# Sum all digits in even positions. Say this is E.
# Difference between O & E. Say this is V.
# If V is negative, ignore the sign, e.g., -6 is treated as 6. Say this is V.
# If V is greater than 9, divide it by 10 and take the reminder. Say this is V.
# V is the verification code.
from typing import List

# verify the first 4 letters
def verify_name(employee_name:str, employee_id:str):
    employee_id_name = extract_str(employee_id, 0, 4)
    if convert_name_to_id(employee_name) != employee_id_name:
        return False
    else:
        return True

def get_odd_digits(id_digits:str)->List[int]:
    odd_parts = id_digits[::2]

    return [int(x) for x in odd_parts]

def get_even_digits(id_digits:str)->List[int]:
    even_parts = id_digits[1::2]

    return [int(x) for x in even_parts]

def verify_digit(employee_id:str):
    # extract digit part
    id_digits:int = extract_str(employee_id, 4,12)
    o_digits = get_odd_digits(id_digits)
    e_digits = get_even_digits(id_digits)

    # extract verification digit
    verification_digit:int = int(extract_str(employee_id, 12,13))

    # vertification logic
    result = abs(sum(o_digits) - sum(e_digits))
    if result <= 9:
        if result == verification_digit:
            return True
        else:
            return False

    if result > 9:
        if result % 10 == verification_digit:
            return True
        else: 
            return False

def extract_str(string_data:str, start:int, end:int):
    return string_data[start:end]

def convert_name_to_id(employee_name:str)->tuple[str,str]:
    name_split:tuple[str,str] = employee_name.split()
    name_sub_string = [name[:2].upper() for name in name_split]
    name_string:str = name_sub_string[1]+name_sub_string[0]

    return name_string

def verify_id(employee_id:str, employee_name:str):
    # verify name
    id_correctness:bool = verify_name(employee_name, employee_id)
    if not id_correctness:
        print("User name_id error")
    else:
        print("Correct")
    # verify digit
    id_digit_correctness:bool = verify_digit(employee_id)
    if not id_digit_correctness:
        print("Digits not correct")
    else:
        print("Digit correct")


if __name__ == "__main__":
    test_case = "CAJI202002196"
    employee_name = "Jigarius Caesar"
    employee_name_fail = "Charlie Lu"

    
    assert extract_str(test_case, 0,4) == "CAJI"
    assert extract_str(test_case, 4,12) == "20200219"
    assert extract_str(test_case, 12,13) == "6"
    print(convert_name_to_id(employee_name))

    verify_id(test_case, employee_name)
    verify_id(test_case, employee_name_fail)

    assert get_odd_digits('12345') == [1,3,5]
    assert get_even_digits('12345') == [2,4]
    verify_digit(test_case)