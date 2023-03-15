
def getChessSquareColor(col:int, row:int)->bool:
    if col > 7 or row > 7:
        return ''
    # black is odd, white is even
    elif ( (col + row) % 2 == 0 ):
        return 'white'
    else: 
        return 'black'
    
if __name__ == "__main__":
    assert getChessSquareColor(1, 1) == 'white'
    assert getChessSquareColor(2, 1) == 'black'
    assert getChessSquareColor(0, 8) == ''