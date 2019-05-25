import Maze
import queue
from random import randrange, shuffle, random
import random
import numpy as np

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Maze:

    def __init__(self, grid, s_x, s_y, f_x, f_y):
        # self.s_x = s_x
        # self.s_y = s_y
        # self.f_x = f_x
        # self.f_y = f_y
        self.grid = grid
        self.s = Point(s_x, s_y)
        self.f = Point(f_x, f_y)
        self.Path = []
        self.M = len(self.grid[0])
        self.N = len(self.grid)
        self.ifVisited = [[0 for x in range(self.M)] for y in range(self.N)]  # 2d array telling if we already visited particular block

    # recursive search with DFS (up -> right -> down -> left)
    def dfs(self, i, j):

        # adds to queue
        #if self.grid[self.s.x][self.s.y] != 'S':
        self.Path.append([i, j])
        self.ifVisited[i][j] = 1

        if self.grid[i][j] == "F":
            # print("Found solution")
            return True # 'True' ends dfs and begins to roll recursion back

        # up

        if 0 <= i - 1 <= self.N - 1 and 0 <= j <= self.M - 1: # if block is still in maze's height and width
            if self.grid[i - 1][j] != "X" and self.ifVisited[i - 1][j] == 0: # if block is not 'X' and if not visited before
                # print("u -> ", end = '')
                if self.dfs(i - 1, j) == True:
                    self.grid[i][j] = "1"
                    self.grid[self.s.x][self.s.y] = "S"
                    return True

        # right
        if 0 <= i <= self.N - 1 and 0 <= j + 1 <= self.M - 1:
            if self.grid[i][j + 1] != "X" and self.ifVisited[i][j + 1] == 0:
                # print("r -> ", end = '')
                if self.dfs(i, j + 1) == True:
                    self.grid[i][j] = "1"
                    self.grid[self.s.x][self.s.y] = "S"
                    return True

        # down
        if 0 <= i + 1 <= self.N - 1 and 0 <= j <= self.M - 1:
            if self.grid[i + 1][j] != "X" and self.ifVisited[i + 1][j] == 0:
                # print("d -> ", end = '')
                if self.dfs(i + 1, j) == True:
                    self.grid[i][j] = "1"
                    self.grid[self.s.x][self.s.y] = "S"
                    return True

        # left
        if 0 <= i <= self.N - 1 and 0 <= j - 1 <= self.M - 1:
            if self.grid[i][j - 1] != "X" and self.ifVisited[i][j - 1] == 0:
                # print("l -> ", end = '')
                if self.dfs(i, j - 1) == True:
                    self.grid[i][j] = "1"
                    self.grid[self.s.x][self.s.y] = "S"
                    return True
        # Removes from queue
        self.Path.pop()
        self.grid[self.s.x][self.s.y] = "S"
        return False

    def dfsRandom(self, i, j):

        # adds to queue
        #if self.grid[self.s.x][self.s.y] != 'S':
        self.Path.append([i, j])
        self.ifVisited[i][j] = 1

        if self.grid[i][j] == "F":
            # print("Found solution")
            return True # 'True' ends dfs and begins to roll recursion back
        for x in range(20):
            rand = random.randint(0, 3)
            # up
            if rand == 0:
                if 0 <= i - 1 <= self.N - 1 and 0 <= j <= self.M - 1: # if is still in maze's height and width
                    if self.grid[i - 1][j] != "X" and self.ifVisited[i - 1][j] == 0: # if block is not 'X' and if not visited before
                        # print("u -> ", end = '')
                        if self.dfsRandom(i - 1, j) == True:
                            self.grid[i][j] = "1"
                            self.grid[self.s.x][self.s.y] = "S"
                            return True

            # right
            if rand == 1:
                if 0 <= i <= self.N - 1 and 0 <= j + 1 <= self.M - 1:
                    if self.grid[i][j + 1] != "X" and self.ifVisited[i][j + 1] == 0:
                        # print("r -> ", end = '')
                        if self.dfsRandom(i, j + 1) == True:
                            self.grid[i][j] = "1"
                            self.grid[self.s.x][self.s.y] = "S"
                            return True

            # down
            if rand == 2:
                if 0 <= i + 1 <= self.N - 1 and 0 <= j <= self.M - 1:
                    if self.grid[i + 1][j] != "X" and self.ifVisited[i + 1][j] == 0:
                        # print("d -> ", end = '')
                        if self.dfsRandom(i + 1, j) == True:
                            self.grid[i][j] = "1"
                            self.grid[self.s.x][self.s.y] = "S"
                            return True

            # left
            if rand == 3:
                if 0 <= i <= self.N - 1 and 0 <= j - 1 <= self.M - 1:
                    if self.grid[i][j - 1] != "X" and self.ifVisited[i][j - 1] == 0:
                        # print("l -> ", end = '')
                        if self.dfsRandom(i, j - 1) == True:
                            self.grid[i][j] = "1"
                            self.grid[self.s.x][self.s.y] = "S"
                            return True
        # Removes from queue
        self.Path.pop()
        self.grid[self.s.x][self.s.y] = "S"
        return False

    def bfs(self, i, j):
        Q = queue.Queue(maxsize=0)

        Q.put([i, j])
        # Q.put([i,j])
        current = Q.get()

        self.ifVisited[i][j] = 1

        while self.grid[current[0]][current[1]] != "F":
            # up
            if 0 <= i - 1 <= self.N - 1 and 0 <= j <= self.M - 1:
                if self.grid[i - 1][j] != "X" and self.ifVisited[i - 1][j] == 0:
                    # print("u -> ", end = '')
                    Q.put([i - 1, j])

            # right
            if 0 <= i <= self.N - 1 and 0 <= j + 1 <= self.M - 1:
                if self.grid[i][j + 1] != "X" and self.ifVisited[i][j + 1] == 0:
                    # print("r -> ", end = '')
                    Q.put([i, j + 1])

            # down
            if 0 <= i + 1 <= self.N - 1 and 0 <= j <= self.M - 1:
                if self.grid[i + 1][j] != "X" and self.ifVisited[i + 1][j] == 0:
                    # print("d -> ", end = '')
                    Q.put([i + 1, j])

            # left
            if 0 <= i <= self.N - 1 and 0 <= j - 1 <= self.M - 1:
                if self.grid[i][j - 1] != "X" and self.ifVisited[i][j - 1] == 0:
                    # print("l -> ", end = '')
                    Q.put([i, j - 1])

            current = Q.get()
            i = current[0]
            j = current[1]
            if self.ifVisited[i][j] == 0:
                self.Path.append(current)
            self.ifVisited[current[0]][current[1]] = 1

        for a in self.Path:
            self.grid[a[0]][a[1]] = "1"

        # print(Path)
        self.grid[self.s.x][self.s.y] = "S"
        self.grid[self.f.x][self.f.y] = "F"


def maze_generator(N=18):
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
    labirynth = Maze(maze, start_x, start_y, finish_x, finish_y)
    
    #board1 = Maze.board1
    N = len(maze)  # rows
    M = len(maze[0])  # columns
    ifVisited = [[0 for x in range(M)] for y in range(N)]  # 2d array telling if we already visited particular block

    return labirynth
