import generator
import queue
import random
import numpy as np
from random import randrange, shuffle, random
from copy import copy, deepcopy
from heapq import *

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
        self.dfsLen = 0 # length of dfs on thisthe maze (without green and red)
        self.bfsLen = 0 # j.w with bfs
        self.GRID = grid # const array of the maze
        self.s = Point(s_x, s_y) # contains coordinates of S
        self.f = Point(f_x, f_y) # j.w with F
        self.Path = [] # path from s to f : [[a,b], [c,d], [e,f]]
        self.M = len(self.GRID[0]) # width
        self.N = len(self.GRID) # height
        self.ifVisited = [[0 for x in range(self.M)] for y in range(self.N)]  # 2d array telling if we already visited particular block


    def get_dfsLen(self):
        return self.dfsLen

    def get_bfsLen(self):
        return self.bfsLen


    def prepare(self):
        self.Path = []
        self.ifVisited = [[0 for x in range(self.M)] for y in range(self.N)]  # 2d array telling if we already visited particular block


    # recursive search with DFS (up -> right -> down -> left)
    def dfs(self, i, j):

        self.prepare()
        grid = deepcopy(self.GRID)

        def dfs_recursion(i, j):

            # adds to queue
            #if self.grid[self.s.x][self.s.y] != 'S':
            #self.Path.append([i, j])
            self.ifVisited[i][j] = 1

            if grid[i][j] == "F":
                # print("Found solution")
                return True # 'True' ends dfs and begins to roll recursion back


        
            # up
            if 0 <= i - 1 <= self.N - 1 and 0 <= j <= self.M - 1: # if block is still in maze's height and width
                if grid[i - 1][j] != "X" and self.ifVisited[i - 1][j] == 0: # if block is not 'X' and if not visited before
                    # print("u -> ", end = '')
                    if dfs_recursion(i - 1, j) == True:
                        grid[i][j] = "1"
                        self.Path.append([i, j])
                        return True

            # right
            if 0 <= i <= self.N - 1 and 0 <= j + 1 <= self.M - 1:
                if grid[i][j + 1] != "X" and self.ifVisited[i][j + 1] == 0:
                    # print("r -> ", end = '')
                    if dfs_recursion(i, j + 1) == True:
                        grid[i][j] = "1"
                        self.Path.append([i, j])
                        return True

            # down
            if 0 <= i + 1 <= self.N - 1 and 0 <= j <= self.M - 1:
                if grid[i + 1][j] != "X" and self.ifVisited[i + 1][j] == 0:
                    # print("d -> ", end = '')
                    if dfs_recursion(i + 1, j) == True:
                        grid[i][j] = "1"
                        self.Path.append([i, j])
                        return True

            # left
            if 0 <= i <= self.N - 1 and 0 <= j - 1 <= self.M - 1:
                if grid[i][j - 1] != "X" and self.ifVisited[i][j - 1] == 0:
                    # print("l -> ", end = '')
                    if dfs_recursion(i, j - 1) == True:
                        grid[i][j] = "1"
                        self.Path.append([i, j])
                        return True
            # Removes from queue
            #self.Path.pop()
            return False

        
        dfs_recursion(i,j)
        grid[self.s.x][self.s.y] = "S"
        self.Path.reverse() 
        if len(self.Path)>0:
            self.Path.pop(0)
        self.dfsLen = len(self.Path) # -1 in order not to count red block

        # print("GRID: ")
        # print(self.GRID)
        # print("grid: ")
        # print(grid)

        print(self.dfsLen)


    def dfsRandom(self, i, j):

        self.prepare()
        grid = deepcopy(self.GRID)

        def dfsRandom_recursion(i, j):

            # adds to queue
            #if self.grid[self.s.x][self.s.y] != 'S':
            self.Path.append([i, j])
            self.ifVisited[i][j] = 1

            if grid[i][j] == "F":
                print("Found solution")
                return True # 'True' ends dfs and begins to roll recursion back

            horizontal = self.f.x - i
            vertical   = self.f.y - j
            

            for x in range(1):
                rand = random.randint(0, 3)
                # up
                if vertical<0 and abs(vertical - horizontal) >= 0:
                    if 0 <= i - 1 <= self.N - 1 and 0 <= j <= self.M - 1: # if is still in maze's height and width
                        if grid[i - 1][j] != "X" and self.ifVisited[i - 1][j] == 0: # if block is not 'X' and if not visited before
                            print("u -> ", end = '')
                            if dfsRandom_recursion(i - 1, j) == True:
                                grid[i][j] = "1"
                                return True

                # right
                if horizontal>0 and abs(horizontal - vertical) >= 0:
                    if 0 <= i <= self.N - 1 and 0 <= j + 1 <= self.M - 1:
                        if grid[i][j + 1] != "X" and self.ifVisited[i][j + 1] == 0:
                            print("r -> ", end = '')
                            if dfsRandom_recursion(i, j + 1) == True:
                                grid[i][j] = "1"
                                return True

                # down
                if vertical>0 and abs(vertical - horizontal) >= 0:
                    if 0 <= i + 1 <= self.N - 1 and 0 <= j <= self.M - 1:
                        if grid[i + 1][j] != "X" and self.ifVisited[i + 1][j] == 0:
                            print("d -> ", end = '')
                            if dfsRandom_recursion(i + 1, j) == True:
                                grid[i][j] = "1"
                                return True

                # left
                if horizontal<0 and abs(horizontal - vertical) >= 0:
                    if 0 <= i <= self.N - 1 and 0 <= j - 1 <= self.M - 1:
                        if grid[i][j - 1] != "X" and self.ifVisited[i][j - 1] == 0:
                            print("l -> ", end = '')
                            if dfsRandom_recursion(i, j - 1) == True:
                                grid[i][j] = "1"
                                return True
            # Removes from queue
            self.Path.pop()
            print("RET -> ", end = '')
            return False

        
        dfsRandom_recursion(i,j)
        grid[self.s.x][self.s.y] = "S"
        if len(self.Path)>0:    
            self.Path.pop(0)
        self.dfsLen = len(self.Path) - 1 # '-1' in order not to count red block

        # print("GRID: ")
        # print(self.GRID)
        # print("grid: ")
        # print(grid)

        print(self.dfsLen)

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


    # Author: Christian Careaga (christian.careaga7@gmail.com)
    # A* Pathfinding in Python (2.7)
    # Please give credit if used

def heuristic(a, b):
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2

def astar(array, start, goal):

    neighbors = [(0,1),(0,-1),(1,0),(-1,0)]

    close_set = set()
    came_from = {}
    gscore = {start:0}
    fscore = {start:heuristic(start, goal)}
    oheap = []

    heappush(oheap, (fscore[start], start))
    
    while oheap:

        current = heappop(oheap)[1]

        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
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
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue
                
            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue
                
            if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heappush(oheap, (fscore[neighbor], neighbor))
                
    return False

'''Here is an example of using my algo with a numpy array,
astar(array, start, destination)
astar function returns a list of points (shortest path)'''

# nmap = numpy.array([
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [1,1,1,1,1,1,1,1,1,1,1,1,0,1],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [1,0,1,1,1,1,1,1,1,1,1,1,1,1],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [1,1,1,1,1,1,1,1,1,1,1,1,0,1],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [1,0,1,1,1,1,1,1,1,1,1,1,1,1],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [1,1,1,1,1,1,1,1,1,1,1,1,0,1],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
    
#print astar(nmap, (0,0), (10,13))