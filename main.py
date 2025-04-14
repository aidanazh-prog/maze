import random

WALL = '#'
PATH = ''

def create_maze(rows=10, cols=10):
    if rows <= 2 or cols <= 2:
        raise ValueError("Maze dimensions must be greater than 2.")
    maze = [[WALL for _ in range(cols)] for_in range(rows)]

def carve_passages(x, y, maze, rows, cols):
    directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
    random.shuffle(directions)
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 1 <= nx < rows - 1 and 1 <= ny < cols - 1 and maze[nx][ny] == WALL:
            maze[nx - dx // 2][ny - dy // 2] = PATH
            maze[nx][ny] = PATH
            carve_passages(nx, ny, maze, rows, cols)


maze[1][1] = PATH
carve_passages(1, 1, maze, rows, cols)

    return maze
def main():
    pass

if __name__== "__main__":
    main()
    