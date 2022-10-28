from queue import PriorityQueue

from typing import List
from Cell import Cell

from Maze import Maze


def main():
    maze_2d = [
        ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
        ["X", ".", ".", ".", "X", ".", ".", ".", ".", ".", ".", ".", "X"],
        ["X", ".", ".", ".", ".", "X", ".", "X", ".", "G", ".", ".", "X"],
        ["X", ".", ".", "X", ".", ".", ".", ".", "X", ".", "X", ".", "X"],
        ["X", ".", ".", ".", "X", ".", ".", ".", ".", "X", ".", ".", "X"],
        ["X", ".", "S", ".", ".", "X", ".", "X", ".", ".", ".", "X", "X"],
        ["X", ".", ".", "X", ".", ".", ".", ".", "X", ".", ".", ".", "X"],
    ]
    maze = Maze(maze_2d, (5,2), (2,9))
    print("result with A*")
    print(a_star(maze))
    #dfs([], maze, maze.start)
    print("result with DFS")
    print(newdfs(maze,maze.start))
    
    
def a_star(maze: Maze):
    path = []
    open_list = PriorityQueue()
    closed_list = PriorityQueue()
    open_list.put(maze.start)
    while open_list.not_empty:
        current_cell: Cell = open_list.get()
        closed_list.put(current_cell)
        if current_cell.x == maze.goal.x and current_cell.y == maze.goal.y:
            path = []
            current = current_cell
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path        
        
        
        neighbors: list[Cell] = maze.get_neighbors(current_cell.x, current_cell.y, maze.rows_length, maze.cols_length, current_cell)
        
        for neighbor in neighbors:
            if neighbor in closed_list.queue:
                continue
            neighbor.g = current_cell.g +1
            neighbor.f = current_cell.g + neighbor.heuristic
            for open_node in open_list.queue:
                if neighbor == open_node and neighbor.g > open_node.g:
                    continue
            open_list.put(neighbor)


def dfs(visted: List[Cell], maze: Maze, cell: Cell):
    if cell == maze.goal:
        print("success")
        return True
    if cell not in visted:
        print(cell.x, cell.y)
        visted.append(cell)
        neighbors = Maze.get_neighbors(maze, cell.x, cell.y, maze.rows_length, maze.cols_length)
        for neighbor in neighbors:
            isFound = dfs(visted, maze, neighbor)
            if isFound:
                return True
            
def newdfs(maze: Maze, cell: Cell):
    stack = [cell] # initilize the stack with the first node (cell)
    path = [] # initial the path the first node
    closed = [] # initilize the closed list with empty
    while stack: # while stack is not empty then continue the loop
        currentCell = stack.pop()# pop the fist cell
        path.append(currentCell.position) # add the position to the path, it might get removed later if we faced a dead end
        if currentCell.x == maze.goal.x and currentCell.y == maze.goal.y: # if the currentCell position is the same as the goal one
            # return our path
            return path
        else:
            # get the current neighbors form get_neighbors_dfs that will not allow for new nodes from the current path to be added to avoid infinite loop
            neighbors = Maze.get_neighbors_dfs(maze, currentCell.x, currentCell.y, maze.rows_length, maze.cols_length,path)
            # add the new nodes to the stack
            stack = stack + neighbors
            # add the node to the closed list
            closed.append(currentCell)
            # if a node has no neighbors that mean we faced a dead end, then we should remove it from our path
            if(neighbors == []):
                path.pop()
    # if we did not find the goal then just return an empty list instead of the path
    return []

if __name__ == "__main__":
    main()

