
def double_array(array:list, idx=0)->list:
    if idx >= len(array):
        return array
    else:
        array[idx] *= 2
        double_array(array, idx+1)

if __name__=="__main__":
    test_array = [1,2,3,4]
    double_array(test_array)
    print(test_array)