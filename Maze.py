from Cell import Cell


class Maze:
    def __init__(self, grid, start: tuple, goal: tuple) -> None:
        self.grid = grid
        self.start = Cell(start[0], start[1], self.find_heu(start, goal), 0, self.find_g(start, start))
        self.goal: Cell = Cell(goal[0], goal[1], self.find_heu(goal, goal), 0, self.find_g(goal, goal))
        self.cells = self.create_cells_grid(grid, goal, start)
        self.cols_length = len(grid[0])
        self.rows_length = len(grid)
    def create_cells_grid(self, grid, goal: tuple, start: tuple):
        cells = [[0 for x in range(len(grid))] for y in range(len(grid[0]))] 
        for i in range(len(cells)):
            for j in range(len(cells[i])):
                cell = Cell(i, j, self.find_heu((i, j), goal), 0, self.find_g((i,j), start))
                cells[i][j] = cell
        return cells
 
    def find_heu(self, point: Cell, goal: Cell):
        return abs(goal[0] - point[0]) + abs(goal[1] - point[1])
    
    def find_g(self, point, start):
        return abs(start[0] - point[0]) + abs(start[1] - point[1])
    
    def get_neighbors(self, x: int, y: int, rows: int, cols: int, parent=None) -> list:
        neighbors = []
        if x - 1 >= 0 and self.grid[x - 1][y] != "X":
            neighbors.append(Cell(x-1, y, self.find_heu((x, y-1), (self.goal.x, self.goal.y)), 0, self.find_g((x, y-1), (self.start.x, self.start.y)), parent))
        if x + 1 < rows and self.grid[x + 1][y] != "X":
            neighbors.append(Cell(x + 1 , y, self.find_heu((x + 1 , y), (self.goal.x, self.goal.y)), 0, self.find_g((x + 1 , y), (self.start.x, self.start.y)), parent))
        if y - 1 >= 0 and self.grid[x][y - 1] != "X":
            neighbors.append(Cell(x, y - 1, self.find_heu((x, y - 1), (self.goal.x, self.goal.y)), 0, self.find_g((x, y - 1), (self.start.x, self.start.y)), parent))
        if y + 1 < cols and self.grid[x][y + 1] != "X":
            neighbors.append(Cell(x, y + 1, self.find_heu((x, y + 1), (self.goal.x, self.goal.y)), 0, self.find_g((x, y + 1), (self.start.x, self.start.y)), parent))
        return neighbors

        