
def unique_paths(row:int, col:int)->int:
    if row and col == 1:
        return 1
    if row < 1:
        return 0
    if col < 1:
        return 0
    
    return (unique_paths(row-1,col) + unique_paths(row,col-1))

if __name__=="__main__":
    row = 8
    col = 8
    
    print(unique_paths(row=row, col=col))