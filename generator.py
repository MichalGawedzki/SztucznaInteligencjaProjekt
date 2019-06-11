import numpy as np
import turtle
import queue
import Algorithms
from pprint import pprint
from random import randrange, shuffle, random, randint

# S - start, F - finish, X - the wall, blank space - path

'''board1 = [
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', "F", ' ', ' ', ' ', 'X', ' ', ' ', 'X', 'X', "X", ' ', ' ', ' ', ' ', ' ', ' ', 'X'],
    ['X', ' ', 'X', 'X', ' ', 'X', ' ', ' ', 'X', 'X', ' ', ' ', 'X', ' ', 'X', ' ', ' ', 'X'],
    ['X', ' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X', 'X', ' ', ' ', 'X', 'X', 'X', ' ', ' ', 'X'],
    ['X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', ' ', ' ', ' ', ' ', 'X'],
    ['X', ' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X', 'X', 'X', 'X'],
    ['X', ' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X', 'X', 'X', 'X'],
    ['X', ' ', ' ', ' ', 'X', 'X', ' ', ' ', 'X', 'X', 'X', ' ', ' ', ' ', 'X', 'S', ' ', 'X'],
    ['X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', 'X', 'X', ' ', 'X', 'X', ' ', 'X', ' ', ' ', 'X'],
    ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', ' ', ' ', 'X', ' ', ' ', ' ', ' ', 'X'],
    ['X', ' ', 'X', 'X', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
]'''

board1 = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', ' ', 'X', ' ', 'X', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X', ' ', 'X', ' ', 'X'], ['X', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', 'X'], ['X', ' ', 'S', ' ', 'X', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X', ' ', 'X', ' ', 'X'], ['X', ' ', 'X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', 'X'], ['X', 'X', ' ', ' ', ' ', ' ', 'X', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', 'X'], ['X', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', 'X', ' ', ' ', ' ', 'X'], ['X', 'X', ' ', 'X', ' ', ' ', ' ', ' ', 'X', ' ', 'X', ' ', ' ', 'X', ' ', 'X', ' ', 'X'], ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X'], ['X', ' ', ' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X'], ['X', 'X', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', 'X', ' ', 'X'], ['X', ' ', ' ', 'X', ' ', 'X', ' ', 'X', ' ', ' ', 'X', ' ', ' ', ' ', ' ', 'X', ' ', 'X'], ['X', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ', 'X'], ['X', ' ', 'X', ' ', 'X', 'X', ' ', ' ', 'X', 'X', ' ', ' ', ' ', ' ', ' ', 'X', ' ', 'X'], ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X'], ['X', ' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X', 'X', ' ', ' ', 'X', ' ', ' ', ' ', ' ', 'X'], ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'F', ' ', ' ', ' ', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]


class Block(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.shapesize(1, 1, 1)
        self.penup()
        self.speed(0)


class Whiteblock(Block):
    def __init__(self):
        Block.__init__(self)
        self.color("white")


class Redblock(Block):
    def __init__(self):
        Block.__init__(self)
        self.color("red")


class Greenblock(Block):
    def __init__(self):
        Block.__init__(self)
        self.color("green")


class Blueblock(Block):
    def __init__(self):
        Block.__init__(self)
        self.color("blue")


class Greyblock(Block):
    def __init__(self):
        Block.__init__(self)
        self.color("purple")


def draw_maze(board, Path, been):

    w_block = Whiteblock()
    g_block = Greenblock()
    r_block = Redblock()
    b_block = Blueblock()
    gr_block = Greyblock()

    window = turtle.Screen()
    window.bgcolor("black")
    window.setup(width=0.6, height=0.6, startx=None, starty=None)
    for x in range(len(board)):
        for y in range(len(board[x])):
            sign = board[x][y]

            x_navigate = -180 + (y * 24)
            y_navigate = 180 - (x * 24)

            if sign == 'X':
                w_block.goto(x_navigate, y_navigate)
                w_block.stamp()
            if sign == 'S':
                g_block.goto(x_navigate, y_navigate)
                g_block.stamp()
            if sign == 'F':
                r_block.goto(x_navigate, y_navigate)
                r_block.stamp()

    for x in range(len(been)):
        sign = been[x]

        if board[been[x][0]][been[x][1]] != 'F':
            x_navigate = -180 + (been[x][1] * 24)
            y_navigate = 180 - (been[x][0] * 24)

        gr_block.goto(x_navigate, y_navigate)
        gr_block.stamp()

    for x in range(len(Path)):
        sign = Path[x]

        if board[Path[x][0]][Path[x][1]] != 'F':
            x_navigate = -180 + (Path[x][1] * 24)
            y_navigate = 180 - (Path[x][0] * 24)

        b_block.goto(x_navigate, y_navigate)
        b_block.stamp()

    window.exitonclick()


boards = []
boards.append(board1)

#draw_maze(boards[0])

def maze_generator(N):

    loop_counter = 0
    breadth, width = N, N
    maze = [['X' for _ in range(N)] for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    # vertical = [["|  "] * w + ['|'] for _ in range(b)] + [[]]
    # horizontal = [["+--"] * w + ['+'] for _ in range(w + 1)]

    for N in range(breadth):
        for N in range(width):
            maze[N][N] = 'X'
    for N in range(breadth):
        for N in range(width):
            visited[N][N] = False

    def create_maze(s2, s1):

        if s2 == 0 or s2 == N or s1 == 0 or s1 == N and loop_counter == 0:
            counter = 1
            return create_maze(2, 2)

        visited[s2][s1] = True  # Start
        maze[s2][s1] = ' '

        neighbours = [(s1 - 1, s2), (s1, s2 + 1), (s1 + 1, s2), (s1, s2 - 1)]
        shuffle(neighbours)

        for (y, x) in neighbours:
            if 1 <= x <= N - 1 and 1 <= y <= N - 1:
                if visited[y][x]:
                    continue
                if visited[y-1][x] and visited[y][x-1]:
                    visited[y-1][x-1] = True
                    # maze[x-1][y-1] = 'X'
                if visited[y-1][x] and visited[y][x+1]:
                    visited[y-1][x+1] = True
                    # maze[x-1][y+1] = 'X'
                if visited[y+1][x] and visited[y][x+1]:
                    visited[y+1][x+1] = True
                    # maze[x+1][y+1] = 'X'
                if visited[y+1][x] and visited[y][x-1]:
                    visited[y+1][x-1] = True
                    # maze[x+1][y-1] = 'X'


                create_maze(y, x)

    create_maze(randrange(N), randrange(N))
    counter = 0

    start_x = randrange(1, int(breadth/4))
    start_y = randrange(1, int(width/4))
    finish_x = randrange(int(3*breadth/4), breadth-1)
    finish_y = randrange(int(3*width/4), width-1)
    maze[start_x][start_y] = 'S'
    visited[start_x][start_y] = True
    maze[finish_x][finish_y] = 'F'
    visited[finish_x][finish_y] = True

    #print('\n'.join([''.join(['{:4}'.format(item) for item in row])
    #                 for row in maze]))
    labirynth = Algorithms.Maze(maze, start_x, start_y, finish_x, finish_y)
    
    #board1 = Maze.board1
    N = len(maze)  # rows
    M = len(maze[0])  # columns
    ifVisited = [[0 for x in range(M)] for y in range(N)]  # 2d array telling if we already visited particular block

    return labirynth


def prim_generator(N,M):

    grid = np.full((N,M), "X")
    neighbours = np.full((N,M), 0) # N
    ifVisited = np.full((N,M), 0) # pogrubione
    #print(grid)
    height, width = N, M
    walls = []
    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0

    sx, sy = 1, 5

    sx = randrange(1, int(width-1))
    sy = randrange(1, int(height-1))

    ifVisited[sx][sy] = 1
    grid[sx][sy] = "S"

    walls.append([sx+1, sy])
    neighbours[sx+1][sy] = 1

    walls.append([sx-1, sy])
    neighbours[sx-1][sy] = 1

    walls.append([sx, sy+1])
    neighbours[sx][sy+1] = 1

    walls.append([sx, sy-1])
    neighbours[sx][sy-1] = 1

    while walls:
        counter = 0
        counter1 = 0
        counter2 = 0
        counter3 = 0
        counter4 = 0
        ind = randint(0, len(walls)-1)
        current = walls[ind]
        
        x, y = current[0], current[1]

        if 1 < x+1 < N-1 and 1 < y < M-1:
            if ifVisited[x+1][y] == 1:
                counter1 += 1
        
        if 1 < x-1 < N-1 and 1 < y < M-1:
            if ifVisited[x-1][y] == 1:
                counter1 += 1
        
        if 1 < x < N-1 and 1 < y+1 < M-1:
            if ifVisited[x][y+1] == 1:
                counter2 += 1
        
        if 1 < x < N-1 and 1 < y-1 < M-1:
            if ifVisited[x][y-1] == 1:
                counter2 += 1

        
        if 1 < x-1 < N-1 and 1 < y-1 < M-1:
            if ifVisited[x-1][y-1] == 1:
                counter3 += 1

        if 1 < x-1 < N-1 and 1 < y+1 < M-1:
            if ifVisited[x-1][y+1] == 1:
                counter3 += 1

        if 1 < x+1 < N-1 and 1 < y-1 < M-1:
            if ifVisited[x+1][y-1] == 1:
                counter4 += 1

        if 1 < x+1 < N-1 and 1 < y+1 < M-1:
            if ifVisited[x+1][y+1] == 1:
                counter4 += 1

        
        counter = counter1 + counter2 + counter3 + counter4


        if counter1 <= 1 and counter2 <= 1 and counter3 <= 1 and counter4 <= 1 and counter <= 2:

            grid[x][y] = " "
            ifVisited[x][y] = 1

            if 0 < x+1 < N-1 and 0 < y < M-1:
                if [x+1,y] not in walls and neighbours[x+1][y] == 0:
                    walls.append([x+1,y])
                    neighbours[x+1][y] = 1


            if 0 < x-1 < N-1 and 0 < y < M-1:
                if [x-1,y] not in walls and neighbours[x-1][y] == 0:
                    walls.append([x-1,y])
                    neighbours[x-1][y] = 1

            if 0 < x < N-1 and 0 < y+1 < M-1:
                if [x,y+1] not in walls and neighbours[x][y+1] == 0:
                    walls.append([x,y+1])
                    neighbours[x][y+1] = 1

            if 0 < x < N-1 and 0 < y-1 < M-1:
                if [x,y-1] not in walls and neighbours[x][y-1] == 0:
                    walls.append([x,y-1])
                    neighbours[x][y-1] = 1

        
        walls.pop(ind)

    for x in range(N):
        grid[x][0], grid[x][M-1] = "X", "X"

    for x in range(M):
        grid[0][x], grid[N-1][x] = "X", "X"

    fx = 0
    fy = 0
    while grid[fx][fy] != " " or fx == sx or fy == sy:
        fx = randrange(int(1), width-1)
        fy = randrange(int(1), height-1)
    grid[sx][sy] = "S"
    grid[fx][fy] = "F"
    labirynth = Algorithms.Maze(grid, sx, sy, fx, fy)
    return labirynth

