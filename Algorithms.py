import Maze
import queue
from random import randrange, shuffle, random
import numpy as np

board1 = Maze.board1
N = len(board1)  # rows
M = len(board1[0])  # columns

ifVisited = [[0 for x in range(M)] for y in range(N)]  # 2d array telling if we already visited particular block

# searching for START and FINISH locations
for i in range(len(board1)):
    for j in range(len(board1[i])):
        if board1[i][j] == "S":
            s = [i, j]  # coordinates of START
        if board1[i][j] == "F":
            f = [i, j]  # coordinates of FINISH

Path = []  # Contains solution path (not in bfs yet)


# recursive search with DFS (random order of directions)
def dfsRandom(i, j):
    # adds to stack
    Path.append([i, j])
    ifVisited[i][j] = 1

    if board1[i][j] == "F":
        # print("Found solution")
        return True

    for x in range(20):

        rand = random.randint(0, 3)

        # up
        if rand == 0:
            if 0 <= i - 1 <= N - 1 and 0 <= j <= M - 1:
                if board1[i - 1][j] != "X" and ifVisited[i - 1][j] == 0:
                    # print("u -> ", end = '')
                    if dfsRandom(i - 1, j) == True:
                        board1[i][j] = "1"
                        board1[s[0]][s[1]] = "S"
                        return True

        # right
        elif rand == 1:

            if 0 <= i <= N - 1 and 0 <= j + 1 <= M - 1:
                if board1[i][j + 1] != "X" and ifVisited[i][j + 1] == 0:
                    # print("r -> ", end = '')
                    if dfsRandom(i, j + 1) == True:
                        board1[i][j] = "1"
                        board1[s[0]][s[1]] = "S"
                        return True

        # down
        elif rand == 2:
            if 0 <= i + 1 <= N - 1 and 0 <= j <= M - 1:
                if board1[i + 1][j] != "X" and ifVisited[i + 1][j] == 0:
                    # print("d -> ", end = '')
                    if dfsRandom(i + 1, j) == True:
                        board1[i][j] = "1"
                        board1[s[0]][s[1]] = "S"
                        return True

        # left
        elif rand == 3:
            if 0 <= i <= N - 1 and 0 <= j - 1 <= M - 1:
                if board1[i][j - 1] != "X" and ifVisited[i][j - 1] == 0:
                    # print("l -> ", end = '')
                    if dfsRandom(i, j - 1) == True:
                        board1[i][j] = "1"
                        board1[s[0]][s[1]] = "S"
                        return True

    # Removes from stack
    Path.pop()
    board1[s[0]][s[1]] = "S"
    return False


# recursive search with DFS (up -> right -> down -> left)
def dfs(i, j):
    # print("dfs")
    # adds to queue
    Path.append([i, j])
    ifVisited[i][j] = 1

    if board1[i][j] == "F":
        # print("Found solution")
        return True

    # up
    if 0 <= i - 1 <= N - 1 and 0 <= j <= M - 1:
        if board1[i - 1][j] != "X" and ifVisited[i - 1][j] == 0:
            # print("u -> ", end = '')
            if dfs(i - 1, j) == True:
                board1[i][j] = "1"
                board1[s[0]][s[1]] = "S"
                return True

    # right
    if 0 <= i <= N - 1 and 0 <= j + 1 <= M - 1:
        if board1[i][j + 1] != "X" and ifVisited[i][j + 1] == 0:
            # print("r -> ", end = '')
            if dfs(i, j + 1) == True:
                board1[i][j] = "1"
                board1[s[0]][s[1]] = "S"
                return True

    # down
    if 0 <= i + 1 <= N - 1 and 0 <= j <= M - 1:
        if board1[i + 1][j] != "X" and ifVisited[i + 1][j] == 0:
            # print("d -> ", end = '')
            if dfs(i + 1, j) == True:
                board1[i][j] = "1"
                board1[s[0]][s[1]] = "S"
                return True

    # left
    if 0 <= i <= N - 1 and 0 <= j - 1 <= M - 1:
        if board1[i][j - 1] != "X" and ifVisited[i][j - 1] == 0:
            # print("l -> ", end = '')
            if dfs(i, j - 1) == True:
                board1[i][j] = "1"
                board1[s[0]][s[1]] = "S"
                return True

    # Removes from queue
    Path.pop()
    board1[s[0]][s[1]] = "S"
    return False


def bfs(i, j):
    Q = queue.Queue(maxsize=0)

    Q.put([i, j])
    # Q.put([i,j])
    current = Q.get()

    ifVisited[i][j] = 1

    while board1[current[0]][current[1]] != "F":

        # up
        if 0 <= i - 1 <= N - 1 and 0 <= j <= M - 1:
            if board1[i - 1][j] != "X" and ifVisited[i - 1][j] == 0:
                # print("u -> ", end = '')
                Q.put([i - 1, j])

        # right
        if 0 <= i <= N - 1 and 0 <= j + 1 <= M - 1:
            if board1[i][j + 1] != "X" and ifVisited[i][j + 1] == 0:
                # print("r -> ", end = '')
                Q.put([i, j + 1])

        # down
        if 0 <= i + 1 <= N - 1 and 0 <= j <= M - 1:
            if board1[i + 1][j] != "X" and ifVisited[i + 1][j] == 0:
                # print("d -> ", end = '')
                Q.put([i + 1, j])

        # left
        if 0 <= i <= N - 1 and 0 <= j - 1 <= M - 1:
            if board1[i][j - 1] != "X" and ifVisited[i][j - 1] == 0:
                # print("l -> ", end = '')
                Q.put([i, j - 1])

        current = Q.get()
        Path.append(current)
        i = current[0]
        j = current[1]
        ifVisited[current[0]][current[1]] = 1

        '''if board1[current[0]][current[1]] == "F":
            print("Found solution!")'''

    for a in Path:
        board1[a[0]][a[1]] = "1"

    # print(Path)
    board1[s[0]][s[1]] = "S"
    board1[f[0]][f[1]] = "F"


def maze_generator(b=11, w=11):
    breadth, width = b, w
    maze = [['X' for _ in range(b)] for _ in range(w)]
    visited = [[False for _ in range(b)] for _ in range(w)]
    # vertical = [["|  "] * w + ['|'] for _ in range(b)] + [[]]
    # horizontal = [["+--"] * w + ['+'] for _ in range(w + 1)]

    for b in range(breadth):
        for w in range(width):
            maze[w][b] = 'X'
    for b in range(breadth):
        for w in range(width):
            visited[w][b] = False

    def create_maze(s2, s1):

        visited[s2][s1] = True  # Start
        maze[s2][s1] = ' '

        neighbours = [(s1 - 1, s2), (s1, s2 + 1), (s1 + 1, s2), (s1, s2 - 1)]
        shuffle(neighbours)

        for (x, y) in neighbours:
            if 0 <= x <= b - 1 and 0 <= y <= w - 1:
                if visited[y][x]:
                    continue
                if visited[x-1][y] and visited[x][y-1]:
                    visited[x-1][y-1] = True
                    maze[x-1][y-1] = 'X'
                if visited[x-1][y] and visited[x][y+1]:
                    visited[x-1][y+1] = True
                    maze[x-1][y+1] = 'X'
                if visited[x+1][y] and visited[x][y+1]:
                    visited[x+1][y+1] = True
                    maze[x+1][y+1] = 'X'
                if visited[x+1][y] and visited[x][y-1]:
                    visited[x+1][y-1] = True
                    maze[x+1][y-1] = 'X'



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
                print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                                 for row in maze]))
                print('\n')
                create_maze(y, x)

    create_maze(randrange(b), randrange(w))

    start_x = randrange(0, int(breadth/4))
    start_y = randrange(0, int(width/4))
    finish_x = randrange(int(3*breadth/4), breadth-1)
    finish_y = randrange(int(3*width/4), width-1)
    maze[start_x][start_y] = 'S'
    visited[start_x][start_y] = True
    maze[finish_x][finish_y] = 'F'
    visited[finish_x][finish_y] = True

    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in maze]))

    return maze

#
# def maze_generator(height, weigth):
#     counter = 0
#     maze = [['X' for _ in range(height)] for _ in range(weigth)]
#     set_list = [set() for _ in range(height*weigth)]
#     set_union = set()
#     for h in range(height):
#         for w in range(weigth):
#             set_list[counter] = set(maze[w][h])
#             counter += 1
#
#     for x in set_list:
#         set_union |= x
#
#     # counter = 0
#     # for h in range(height):
#     #     for w in range(weigth):
#     #         print(set_list[counter])
#     #         counter+=1
#
#     print(set_union)
