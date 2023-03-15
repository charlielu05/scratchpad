
def return_even(array:list[int])->list[int]:
    if len(array) == 0:
        return []
    if array[0] % 2 == 0:
        return [array[0]] + return_even(array[1:])
    else:
        return return_even(array[1:])

if __name__=="__main__":
    ints = [1,2,3,4]
    
    print(return_even(ints))