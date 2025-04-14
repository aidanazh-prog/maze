import random

WALL = '#'
PATH = ''
VISITED = '.'

def create_maze(rows=10, cols=10):
    if rows <= 2 or cols <= 2:
        raise ValueError("Maze dimensions must be greater than 2.")

    maze = [[WALL for _ in range(cols)] for _ in range(rows)]

    def carve_passages(x, y):
        directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < rows - 1 and 1 <= ny < cols - 1 and maze[nx][ny] == WALL:
                maze[nx - dx // 2][ny - dy // 2] = PATH
                maze[nx][ny] = PATH
                carve_passages(nx, ny)


    maze[1][1] = PATH
    carve_passages(1, 1)

    maze[1][0] = PATH  
    maze[rows - 2][cols - 1] = PATH  

    return maze

def print_maze(maze):
    for row in maze:
        print(''.join(row))

def solve_maze(maze, x, y, end_x, end_y, visited):
    if x == end_x and y == end_y:
        maze[x][y] = VISITED
        return True
    if not (0 <= x < len(maze)) or not (0 <= y < len(maze[0])):
        return False
    if maze[x][y] != PATH:  
        return False
    if visited[x][y]:
        return False

    visited[x][y] = True
    maze[x][y] = VISITED

    if (solve_maze(maze, x+1, y, end_x, end_y, visited) or
        solve_maze(maze, x-1, y, end_x, end_y, visited) or
        solve_maze(maze, x, y+1, end_x, end_y, visited) or
        solve_maze(maze, x, y-1, end_x, end_y, visited)):
        return True

    maze[x][y] = PATH  # backtrack
    return False

def main():
    rows, cols = 15, 15
    maze = create_maze(rows, cols)

    start_x, start_y = 1, 0
    end_x, end_y = rows - 2, cols - 1

    visited = [[False for _ in range(cols)] for _ in range(rows)]
    solved = solve_maze(maze, start_x, start_y + 1, end_x, end_y - 1, visited)

    if solved:
        print("Maze with path:")
        print_maze(maze)
    else:
        print("No solution found.")

if __name__== "__main__":
    main()
    