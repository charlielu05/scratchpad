
def staircase(stairs:int)->int:
    if stairs == 1:
        return 1
    if stairs == 2:
        return 2
    if stairs == 3:
        return 4
    if stairs < 0:
        return 0
    
    return (staircase(stairs-1) + staircase(stairs-2) + staircase(stairs-3))

if __name__ == "__main__":
    stairs = 11
    print(staircase(stairs))
