import generator
import queue
from random import randrange, shuffle, random
import random
import numpy as np
from copy import copy, deepcopy
from heapq import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Maze:

    def __init__(self, grid, s_x, s_y, f_x, f_y):
        self.dfsLen = 0
        self.bfsLen = 0
        self.astarLen = 0
        self.GRID = grid
        self.s = Point(s_x, s_y)
        self.f = Point(f_x, f_y)
        #self.Path = {}
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
                return True # 'True' ends dfs and begins to roll recursion back


        
            # up
            if 0 <= i - 1 <= self.N - 1 and 0 <= j <= self.M - 1: # if block is still in maze's height and width
                if grid[i - 1][j] != "X" and self.ifVisited[i - 1][j] == 0: # if block is not 'X' and if not visited before
                    if dfs(i - 1, j) == True:
                        grid[i][j] = "1"
                        return True

            # right
            if 0 <= i <= self.N - 1 and 0 <= j + 1 <= self.M - 1:
                if grid[i][j + 1] != "X" and self.ifVisited[i][j + 1] == 0:
                    if dfs(i, j + 1) == True:
                        grid[i][j] = "1"
                        return True

            # down
            if 0 <= i + 1 <= self.N - 1 and 0 <= j <= self.M - 1:
                if grid[i + 1][j] != "X" and self.ifVisited[i + 1][j] == 0:
                    if dfs(i + 1, j) == True:
                        grid[i][j] = "1"
                        return True

            # left
            if 0 <= i <= self.N - 1 and 0 <= j - 1 <= self.M - 1:
                if grid[i][j - 1] != "X" and self.ifVisited[i][j - 1] == 0:
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


    def bfs(self, i, j):

        self.prepare()
        grid = deepcopy(self.GRID)

        Pred = [None] * self.N * self.M

        Q = queue.Queue(maxsize=0)

        Q.put([i, j])
        current = Q.get()

        self.ifVisited[i][j] = 1

        while grid[current[0]][current[1]] != "F":
            # up
            if 0 <= i - 1 <= self.N - 1 and 0 <= j <= self.M - 1:
                if grid[i - 1][j] != "X" and self.ifVisited[i - 1][j] == 0:
                    Q.put([i - 1, j])
                    Pred[(i-1)*self.M + j] = i*self.M + j

            # right
            if 0 <= i <= self.N - 1 and 0 <= j + 1 <= self.M - 1:
                if grid[i][j + 1] != "X" and self.ifVisited[i][j + 1] == 0:
                    Q.put([i, j + 1])
                    Pred[(i)*self.M + j + 1] = i*self.M + j

            # down
            if 0 <= i + 1 <= self.N - 1 and 0 <= j <= self.M - 1:
                if grid[i + 1][j] != "X" and self.ifVisited[i + 1][j] == 0:
                    Q.put([i + 1, j])
                    Pred[(i+1)*self.M + j] = i*self.M + j

            # left
            if 0 <= i <= self.N - 1 and 0 <= j - 1 <= self.M - 1:
                if grid[i][j - 1] != "X" and self.ifVisited[i][j - 1] == 0:
                    Q.put([i, j - 1])
                    Pred[(i)*self.M + j - 1] = i*self.M + j

            current = Q.get()
            i = current[0]
            j = current[1]
            if self.ifVisited[i][j] == 0:
                self.been.append(current)
            self.ifVisited[current[0]][current[1]] = 1

        tmp = i*self.M + j
        self.Path.append([i,j])

        while self.GRID[i][j] != 'S':
            tmp = Pred[tmp]
            i = tmp // self.M
            j = tmp % self.M
            self.Path.append([i,j])
        self.Path.reverse()

        self.Path.pop(-1)
        self.Path.pop(0)

        grid[self.s.x][self.s.y] = "S"
        grid[self.f.x][self.f.y] = "F"
        self.bfsLen = len(self.Path)


    def astar(self, array, start, goal):

        def heuristic(a, b):
            return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2

        self.prepare()
        neighbors = [(0,1),(0,-1),(1,0),(-1,0)]

        close_set = set()
        came_from = {}
        gscore = {start:0}
        fscore = {start:heuristic(start, goal)}
        oheap = []

        heappush(oheap, (fscore[start], start))
        
        while oheap:

            current = heappop(oheap)[1]
            self.been.append(current)

            if current == goal:
                data = []
                while current in came_from:
                    data.append(current)
                    current = came_from[current]
                self.Path = data
                self.Path.reverse()
                self.astarLen = len(self.Path) -1
                self.been.pop(0)
                return data

            close_set.add(current)
            for i, j in neighbors:
                neighbor = current[0] + i, current[1] + j            
                tentative_g_score = gscore[current] + heuristic(current, neighbor)
                if 0 <= neighbor[0] < array.shape[0]:
                    if 0 <= neighbor[1] < array.shape[1]:                
                        if array[neighbor[0]][neighbor[1]] == 'X':
                            continue
                    else:
                        continue
                else:
                    continue
                    
                if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                    continue
                    
                if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                    came_from[neighbor] = current
                    gscore[neighbor] = tentative_g_score
                    fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    heappush(oheap, (fscore[neighbor], neighbor))
                    
        return False

