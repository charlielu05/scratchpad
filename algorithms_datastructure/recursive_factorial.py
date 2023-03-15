
def recursive_factorial(num:int):
    if num == 1:
        return 1
    else:
        return (num*recursive_factorial(num-1))
        
if __name__=="__main__":
    print(recursive_factorial(5))