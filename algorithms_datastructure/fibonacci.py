
def fib(n:int)->int:

    if n == 0 or n == 1:
        return n

    else:
        return fib(n-2) + fib(n-1)

def fib_memo(n:int, memo={})->int:
 
    if n == 0 or n == 1:
        return n

    if memo.get(n) is None:
        memo[n] = fib_memo(n-2, memo) + fib_memo(n-1, memo)

    return memo[n]

def fib_bottom_up(n:int)->int:
    if n == 0:
        return 0
    
    a = 0
    b = 1

    for i in range(1,n):
        temp = a
        a = b
        b = a + temp
    
    return b

if __name__=="__main__":
    n = 12
    
    assert fib(n) == 144
    assert fib_memo(n) == 144
    assert fib_bottom_up(n) == 144