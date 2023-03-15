
def recursive_countdown(num:int):
    if num == 0:
        return None
    else:
        print(num)
        recursive_countdown(num-1)
        
if __name__=="__main__":
    recursive_countdown(10)