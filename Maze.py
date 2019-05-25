import numpy as np
import turtle
import queue
from pprint import pprint
from random import randrange, shuffle, random

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


def draw_maze(board, Path):

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

    for x in range(len(Path)):
        sign = Path[x]

        if board[Path[x][0]][Path[x][1]] != 'F':
            x_navigate = -180 + (Path[x][1] * 24)
            y_navigate = 180 - (Path[x][0] * 24)

        b_block.goto(x_navigate, y_navigate)
        b_block.stamp()

    window.exitonclick()

w_block = Whiteblock()
g_block = Greenblock()
r_block = Redblock()
b_block = Blueblock()

boards = []
boards.append(board1)


def maze_generator(N=18):
    loop_counter = 0
    breadth, width = N, N
    maze = [['X' for _ in range(N)] for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    # vertical = [["|  "] * w + ['|'] for _ in range(b)] + [[]]
    # horizontal = [["+--"] * w + ['+'] for _ in range(w + 1)]

    for N in range(breadth):
        for N in range(width):
            maze[N][N] = "X"
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



                # if (x, y) == (s1 - 1, s2):
                #     visited[x + 1][y] = True
                #     visited[x][y - 1] = True
                #     visited[x][y + 1] = True
                #     maze[x + 1][y] = 'X'
                #     maze[x][y - 1] = 'X'
                #     maze[x][y + 1] = 'X'
                # if (x, y) == (s1 + 1, s2):
                #     visited[x - 1][y] = True
                #     visited[x][y + 1] = True
                #     visited[x][y - 1] = True
                #     maze[x - 1][y] = 'X'
                #     maze[x][y + 1] = 'X'
                #     maze[x][y - 1] = 'X'
                # if (x, y) == (s1, s2 - 1):
                #     visited[x + 1][y] = True
                #     visited[x - 1][y] = True
                #     visited[x][y + 1] = True
                #     maze[x + 1][y] = 'X'
                #     maze[x - 1][y] = 'X'
                #     maze[x][y + 1] = 'X'
                # if (x, y) == (s1, s2 + 1):
                #     visited[x + 1][y] = True
                #     visited[x - 1][y] = True
                #     visited[x][y - 1] = True
                #     maze[x + 1][y] = 'X'
                #     maze[x - 1][y] = 'X'
                #     maze[x][y - 1] = 'X'
                #print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                #                 for row in maze]))
                #print('\n')

                create_maze(y, x)

    create_maze(randrange(N), randrange(N))
    counter = 0

    start_x = randrange(1, int(breadth/4))
    start_y = randrange(1, int(width/4))
    finish_x = randrange(int(3*breadth/4), breadth-1)
    finish_y = randrange(int(3*width/4), width-1)
    maze[start_x][start_y] = "S"
    visited[start_x][start_y] = True
    maze[finish_x][finish_y] = "F"
    visited[finish_x][finish_y] = True

    #print('\n'.join([''.join(['{:4}'.format(item) for item in row])
    #                 for row in maze]))
    #print("TU HERE")
    #print(maze)
    boards.append(maze)
    board1 = maze
    return maze

#draw_maze(boards[0])