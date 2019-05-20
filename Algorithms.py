import Maze
import random
import queue

board1 = Maze.board1
N = len(board1) # rows
M = len(board1[0]) # columns

ifVisited = [[0 for x in range(M)] for y in range(N)] # 2d array telling if we already visited particular block

# searching for START and FINISH locations
for i in range(len(board1)):
    for j in range(len(board1[i])):
        if board1[i][j] == "S":
            s = [i,j] # coordinates of START
        if board1[i][j] == "F":
            f = [i,j] # coordinates of FINISH

Path = [] # Contains solution path (not in bfs yet)

# recursive search with DFS (random order of directions)
def dfsRandom(i, j):

    #adds to stack
    Path.append([i,j])
    ifVisited[i][j]=1

    if board1[i][j] == "F":
        #print("Found solution")
        return True

    for x in range(20):

        rand = random.randint(0,3)
        
        # up
        if rand == 0:
            if 0 <= i-1 <= N-1 and 0<=j<=M-1:
                if board1[i-1][j] != "X" and ifVisited[i-1][j]==0:
                    #print("u -> ", end = '')
                    if dfsRandom(i-1, j) == True:
                        board1[i][j] = "1"
                        board1[s[0]][s[1]] = "S"
                        return True
        
        # right
        elif rand == 1:
            
            if 0 <= i <= N-1 and 0<=j+1<=M-1:
                if board1[i][j+1] != "X" and ifVisited[i][j+1]==0:
                    #print("r -> ", end = '')
                    if dfsRandom(i, j+1) == True:
                        board1[i][j] = "1"
                        board1[s[0]][s[1]] = "S"
                        return True

        # down
        elif rand == 2:
            if 0 <= i+1 <= N-1 and 0<=j<=M-1:
                if board1[i+1][j] != "X" and ifVisited[i+1][j]==0:
                    #print("d -> ", end = '')
                    if dfsRandom(i+1, j) == True:
                        board1[i][j] = "1"
                        board1[s[0]][s[1]] = "S"
                        return True

        # left
        elif rand == 3:
            if 0 <= i <= N-1 and 0<=j-1<=M-1:
                if board1[i][j-1] != "X" and ifVisited[i][j-1]==0:
                    #print("l -> ", end = '')
                    if dfsRandom(i, j-1) == True:
                        board1[i][j] = "1"
                        board1[s[0]][s[1]] = "S"
                        return True

    # Removes from stack
    Path.pop()
    board1[s[0]][s[1]] = "S"
    return False
    

# recursive search with DFS (up -> right -> down -> left)
def dfs(i, j):
    #print("dfs")
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
            if dfs(i-1, j) == True:
                board1[i][j] = "1"
                board1[s[0]][s[1]] = "S"
                return True

    # right
    if 0 <= i <= N-1 and 0<=j+1<=M-1:
        if board1[i][j+1] != "X" and ifVisited[i][j+1]==0:
            #print("r -> ", end = '')
            if dfs(i, j+1) == True:
                board1[i][j] = "1"
                board1[s[0]][s[1]] = "S"
                return True

    # down
    if 0 <= i+1 <= N-1 and 0<=j<=M-1:
        if board1[i+1][j] != "X" and ifVisited[i+1][j]==0:
            #print("d -> ", end = '')
            if dfs(i+1, j) == True:
                board1[i][j] = "1"
                board1[s[0]][s[1]] = "S"
                return True

    # left
    if 0 <= i <= N-1 and 0<=j-1<=M-1:
        if board1[i][j-1] != "X" and ifVisited[i][j-1]==0:
            #print("l -> ", end = '')
            if dfs(i, j-1) == True:
                board1[i][j] = "1"
                board1[s[0]][s[1]] = "S"
                return True

    # Removes from queue
    Path.pop()
    board1[s[0]][s[1]] = "S"
    return False
    
def bfs(i, j):
    
    Q = queue.Queue(maxsize=0)

    Q.put([i,j])
    #Q.put([i,j])
    current = Q.get()

    ifVisited[i][j] = 1

    while board1[current[0]][current[1]] != "F":

        # up
        if 0 <= i-1 <= N-1 and 0<=j<=M-1:
            if board1[i-1][j] != "X" and ifVisited[i-1][j]==0:
                #print("u -> ", end = '')
                Q.put([i-1,j])

        # right
        if 0 <= i <= N-1 and 0<=j+1<=M-1:
            if board1[i][j+1] != "X" and ifVisited[i][j+1]==0:
                #print("r -> ", end = '')
                Q.put([i,j+1])

        # down
        if 0 <= i+1 <= N-1 and 0<=j<=M-1:
            if board1[i+1][j] != "X" and ifVisited[i+1][j]==0:
                #print("d -> ", end = '')
                Q.put([i+1,j])

        # left
        if 0 <= i <= N-1 and 0<=j-1<=M-1:
            if board1[i][j-1] != "X" and ifVisited[i][j-1]==0:
                #print("l -> ", end = '')
                Q.put([i,j-1])
        
        current = Q.get()
        Path.append(current)
        i = current[0]
        j = current[1]
        ifVisited[current[0]][current[1]] = 1
        

        '''if board1[current[0]][current[1]] == "F":
            print("Found solution!")'''

    for a in Path:
        board1[a[0]][a[1]] = "1"

    #print(Path)
    board1[s[0]][s[1]] = "S"
    board1[f[0]][f[1]] = "F"