import numpy as np
import turtle
import queue
from pprint import pprint

# S - start, F - finish, X - the wall, blank space - path

board1 = [
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', "F", ' ', ' ', ' ', 'X', ' ', ' ', 'X', 'X', "X", ' ', ' ', ' ', ' ', ' ', ' ', 'X'],
    ['X', ' ', 'X', 'X', ' ', 'X', ' ', ' ', 'X', 'X', ' ', ' ', 'X', ' ', 'X', ' ', ' ', 'X'],
    ['X', ' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X', 'X', ' ', ' ', 'X', 'X', 'X', ' ', ' ', 'X'],
    ['X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', ' ', ' ', ' ', ' ', 'X'],
    ['X', ' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X', 'X', 'X', 'X'],
    ['X', ' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X', 'X', 'X', 'X'],
    ['X', ' ', ' ', ' ', 'X', 'X', ' ', ' ', 'X', 'X', "X", ' ', ' ', ' ', 'X', 'S', ' ', 'X'],
    ['X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', 'X', 'X', ' ', 'X', 'X', ' ', 'X', ' ', ' ', 'X'],
    ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', ' ', ' ', 'X', ' ', ' ', ' ', ' ', 'X'],
    ['X', ' ', 'X', 'X', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
]

N = len(board1) # rows
M = len(board1[0]) # columns

ifVisited = [[0 for x in range(M)] for y in range(N)] # 2d array telling if we already visited particular block

# searching for START and FINISH locations
for i in range(len(board1)):
    for j in range(len(board1[i])):
        if board1[i][j] == "S":
            s = [i,j]
        if board1[i][j] == "F":
            f = [i,j]

Path = [] # Contains solution path

# recursive search with BFS (up -> right -> down -> left)
def bfs(i, j):

    #adds to queue
    Path.append([i,j])
    ifVisited[i][j]=1

    if board1[i][j] == "F":
        #print("Found solution")
        return True

    # up
    if 0 <= i-1 <= N-1 and 0<=j<=M-1:
        if board1[i-1][j] != "X" and ifVisited[i-1][j]==0:
            #print("u -> ", end = '')
            if bfs(i-1, j) == True:
                board1[i][j] = "1"
                return True

    # right
    if 0 <= i <= N-1 and 0<=j+1<=M-1:
        if board1[i][j+1] != "X" and ifVisited[i][j+1]==0:
            #print("r -> ", end = '')
            if bfs(i, j+1) == True:
                board1[i][j] = "1"
                return True

    # down
    if 0 <= i+1 <= N-1 and 0<=j<=M-1:
        if board1[i+1][j] != "X" and ifVisited[i+1][j]==0:
            #print("d -> ", end = '')
            if bfs(i+1, j) == True:
                board1[i][j] = "1"
                return True

    # left
    if 0 <= i <= N-1 and 0<=j-1<=M-1:
        if board1[i][j-1] != "X" and ifVisited[i][j-1]==0:
            #print("l -> ", end = '')
            if bfs(i, j-1) == True:
                board1[i][j] = "1"
                return True

    # Removes from queue
    Path.pop()
    return False
    

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


def draw_maze(board):

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
            if sign == '1':
                b_block.goto(x_navigate, y_navigate)
                b_block.stamp()

    window.exitonclick()


bfs(s[0], s[1])
board1[s[0]][s[1]] = "S"

w_block = Whiteblock()
g_block = Greenblock()
r_block = Redblock()
b_block = Blueblock()

boards = []
boards.append(board1)

draw_maze(boards[0])