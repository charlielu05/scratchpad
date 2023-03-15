
from unittest.result import failfast


def pour_problem(X, Y, goal, start=(0,0)):
    
    if goal in start:
        return [start]
    explored = set()
    frontier = [ [start] ] # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        (x, y) = path[-1] # last state in the first path of the frontier
        for (state, action) in successor(x, y, X, Y).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if goal == state:
                    return path2
                else:
                    frontier.append(path2)
    
    return Fail

Fail = []

def successor(x, y, X, Y):

    assert x <= X and y <= Y # (x,y) is glass level state, X and Y are glass sizes
    return {((0, y+x) if y+x<=Y else (x-(Y-y), y+(Y-y))):'X->Y',
            ((x+y, 0) if x+y<=X else (x+(X-x), y-(X-x))):'X<-Y',
            (X, y):'fill X', (x, Y):'fill Y',
            (0, y):'empty X', (x, 0):'empty Y'}

if __name__=="__main__":
    X, Y = (9, 4)
    
    goal = (6, 0)
    solution = pour_problem(X, Y, goal)