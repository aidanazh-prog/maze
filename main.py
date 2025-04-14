WALL = '#'

def create_maze(rows=10, cols=10):
    if rows <= 2 or cols <= 2:
        raise ValueError("Maze dimensions must be greater than 2.")
    maze = [[WALL for _ in range(cols)] for_in range(rows)]
    return maze
def main():
    pass

if __name__== "__main__":
    main()
    