from re import X


class Cell:
    def __init__(self, x, y, heuristic, cost, g, parent=None) -> None:
        # f = g + h
        self.x = x
        self.y = y
        self.heuristic = heuristic
        self.cost = cost
        self.g = g
        self.f = g + heuristic
        self.parent = parent
        self.position = (x,y)
        
    def __str__(self):
        return f"({self.x}, {self.y})"
    def __repr__ (self):
        return self.__str__()
    def __lt__(self, other):
        selfPriority = (self.g)
        otherPriority = (other.g)
        return selfPriority < otherPriority
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y