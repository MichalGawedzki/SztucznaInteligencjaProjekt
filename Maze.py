import numpy as np
import turtle

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

    window.exitonclick()


w_block = Whiteblock()
g_block = Greenblock()
r_block = Redblock()

boards = []
boards.append(board1)

draw_maze(boards[0])
