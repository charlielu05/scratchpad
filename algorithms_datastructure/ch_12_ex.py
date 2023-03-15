
# add until 100
def add_until_100(array:list[int])->int:
    if len(array) == 0:
        return 0
    
    if array[0] + add_until_100(array[1:]) > 100:
        return add_until_100(array[1:])
    else:
        return array[0] + add_until_100(array[1:])

def add_until_100_improved(array:list[int])->int:
    if len(array) == 0:
        return 0
    
    array_sum = array[0] + add_until_100(array[1:])

    if array_sum > 100:
        return array_sum - array[0]
    else:
        return array_sum

# Golomb sequence
def golomb(n):
    if n == 1:
        return 1
   
    return 1 + golomb(n - golomb(golomb(n-1)))

def golomb_memo(n, memo={}):
    if n == 1:
        return 1
    
    if memo.get(n) is None:
        memo[n] = 1 + golomb_memo(n - golomb_memo(golomb_memo(n-1, memo), memo), memo) 

    return memo[n]

def unique_paths_memo(rows,columns,memo={}):
    if rows and columns == 1:
        return 1
    
    if rows < 1:
        return 0
        
    if columns < 1:
        return 0
    
    if (rows,columns) not in memo:
        memo[(rows, columns)] = unique_paths_memo(rows-1, columns, memo) + unique_paths_memo(rows, columns-1,memo)
    
    return memo[(rows, columns)]

if __name__ == "__main__":
    test_add_100 = [99,2,2,2]
    
    print(add_until_100(test_add_100))
    assert add_until_100(test_add_100) == 6
    assert add_until_100_improved(test_add_100) == 6

    print(f"Golomb: {golomb(6)}")
    print(f"Golomb: {golomb_memo(6)}")

    print(unique_paths_memo(8, 8))