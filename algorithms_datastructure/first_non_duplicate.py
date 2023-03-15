
def first_non_duplicate(string:str)->str:
    # counter for occurence
    counter_dict = dict(zip([x for x in string], [0]*len(string)))

    for letter in string:
        counter_dict[letter] = counter_dict.get(letter) + 1

    for letter in string:
        if counter_dict.get(letter) == 1:
            return letter

if __name__=="__main__":
    string = "minimum"
    
    assert first_non_duplicate(string) == "n"