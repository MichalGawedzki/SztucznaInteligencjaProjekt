import generator
import queue
from random import randrange, shuffle, random
import random
import numpy as np
from copy import copy, deepcopy

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
        self.dfsLen = 0
        self.bfsLen = 0
        self.GRID = grid
        self.s = Point(s_x, s_y)
        self.f = Point(f_x, f_y)
        self.Path = []
        self.been = []
        self.M = len(self.GRID[0])
        self.N = len(self.GRID)
        self.ifVisited = [[0 for x in range(self.M)] for y in range(self.N)]  # 2d array telling if we already visited particular block

    def get_dfsLen(self):
        return self.dfsLen

    def get_bfsLen(self):
        return self.bfsLen

    def prepare(self):
        self.Path = []
        self.been = []
        self.ifVisited = [[0 for x in range(self.M)] for y in range(self.N)]  # 2d array telling if we already visited particular block


    # recursive search with DFS (up -> right -> down -> left)
    def d_dfs(self, i, j):

        self.prepare()
        grid = deepcopy(self.GRID)
        
        def dfs(i, j):

            # adds to queue
            #if self.grid[self.s.x][self.s.y] != 'S':
            self.Path.append([i, j])
            if self.ifVisited[i][j] == 0:
                self.been.append([i, j])
            self.ifVisited[i][j] = 1

            if grid[i][j] == "F":
                # print("Found solution")
                return True # 'True' ends dfs and begins to roll recursion back


        
            # up
            if 0 <= i - 1 <= self.N - 1 and 0 <= j <= self.M - 1: # if block is still in maze's height and width
                if grid[i - 1][j] != "X" and self.ifVisited[i - 1][j] == 0: # if block is not 'X' and if not visited before
                    # print("u -> ", end = '')
                    if dfs(i - 1, j) == True:
                        grid[i][j] = "1"
                        return True

            # right
            if 0 <= i <= self.N - 1 and 0 <= j + 1 <= self.M - 1:
                if grid[i][j + 1] != "X" and self.ifVisited[i][j + 1] == 0:
                    # print("r -> ", end = '')
                    if dfs(i, j + 1) == True:
                        grid[i][j] = "1"
                        return True

            # down
            if 0 <= i + 1 <= self.N - 1 and 0 <= j <= self.M - 1:
                if grid[i + 1][j] != "X" and self.ifVisited[i + 1][j] == 0:
                    # print("d -> ", end = '')
                    if dfs(i + 1, j) == True:
                        grid[i][j] = "1"
                        return True

            # left
            if 0 <= i <= self.N - 1 and 0 <= j - 1 <= self.M - 1:
                if grid[i][j - 1] != "X" and self.ifVisited[i][j - 1] == 0:
                    # print("l -> ", end = '')
                    if dfs(i, j - 1) == True:
                        grid[i][j] = "1"
                        return True
            # Removes from queue
            self.Path.pop()
            return False

        
        dfs(i,j)
        grid[self.s.x][self.s.y] = "S"
        if len(self.Path)>0:    
            self.Path.pop(0)
        if len(self.been)>0:    
            self.been.pop(0)
        self.dfsLen = len(self.Path) - 1

        # print("GRID: ")
        # print(self.GRID)
        # print("grid: ")
        # print(grid)

        #print(self.dfsLen)


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

        self.prepare()
        grid = deepcopy(self.GRID)

        Q = queue.Queue(maxsize=0)

        Q.put([i, j])
        # Q.put([i,j])
        current = Q.get()

        self.ifVisited[i][j] = 1

        while grid[current[0]][current[1]] != "F":
            # up
            if 0 <= i - 1 <= self.N - 1 and 0 <= j <= self.M - 1:
                if grid[i - 1][j] != "X" and self.ifVisited[i - 1][j] == 0:
                    # print("u -> ", end = '')
                    Q.put([i - 1, j])

            # right
            if 0 <= i <= self.N - 1 and 0 <= j + 1 <= self.M - 1:
                if grid[i][j + 1] != "X" and self.ifVisited[i][j + 1] == 0:
                    # print("r -> ", end = '')
                    Q.put([i, j + 1])

            # down
            if 0 <= i + 1 <= self.N - 1 and 0 <= j <= self.M - 1:
                if grid[i + 1][j] != "X" and self.ifVisited[i + 1][j] == 0:
                    # print("d -> ", end = '')
                    Q.put([i + 1, j])

            # left
            if 0 <= i <= self.N - 1 and 0 <= j - 1 <= self.M - 1:
                if grid[i][j - 1] != "X" and self.ifVisited[i][j - 1] == 0:
                    # print("l -> ", end = '')
                    Q.put([i, j - 1])

            current = Q.get()
            i = current[0]
            j = current[1]
            if self.ifVisited[i][j] == 0:
                self.Path.append(current)
            self.ifVisited[current[0]][current[1]] = 1

        for a in self.Path:
            grid[a[0]][a[1]] = "1"

        # print(Path)
        grid[self.s.x][self.s.y] = "S"
        grid[self.f.x][self.f.y] = "F"



