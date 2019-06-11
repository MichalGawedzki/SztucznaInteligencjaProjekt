import generator
import Algorithms
from pprint import pprint
import numpy as np

boards = []
boards.append(generator.board1)

# new_maze = Algorithms.maze_generator(18)
# boards.append(new_maze)
#new_maze.d_dfs(new_maze.s.x, new_maze.s.y)
#a = new_maze.get_dfsLen()

# new_maze = generator.maze_generator(10)

for x in range(100):
        new_maze = generator.maze_generator(10)
        new_maze.dfs(new_maze.s.x, new_maze.s.y)
        a = new_maze.get_dfsLen()
        if a < 25:
                print("caught")
                break

generator.draw_maze(new_maze.GRID, new_maze.Path)

# nmap = np.array([
# ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
# ['X', "F", ' ', ' ', ' ', 'X', ' ', ' ', 'X', 'X', "X", ' ', ' ', ' ', ' ', ' ', ' ', 'X'],
# ['X', ' ', 'X', 'X', ' ', 'X', ' ', ' ', 'X', 'X', ' ', ' ', 'X', ' ', 'X', ' ', ' ', 'X'],
# ['X', ' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X', 'X', ' ', ' ', 'X', 'X', 'X', ' ', ' ', 'X'],
# ['X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', ' ', ' ', ' ', ' ', 'X'],
# ['X', ' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X', 'X', 'X', 'X'],
# ['X', ' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X', 'X', 'X', 'X'],
# ['X', ' ', ' ', ' ', 'X', 'X', ' ', ' ', 'X', 'X', 'X', ' ', ' ', ' ', 'X', 'S', ' ', 'X'],
# ['X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', 'X', 'X', ' ', 'X', 'X', ' ', 'X', ' ', ' ', 'X'],
# ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', ' ', ' ', 'X', ' ', ' ', ' ', ' ', 'X'],
# ['X', ' ', 'X', 'X', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X'],
# ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
# ])


# # pth = Algorithms.astar(nmap, (7,15), (1,1))
# # print(len(pth))
# # print(pth)
# # generator.draw_maze(nmap, pth)

# nmap = Algorithms.maze_generator(18)
# nmap.f
# nmap = np.array(nmap)
# pth = Algorithms.astar(nmap, , (1,1))
# print(len(pth))
# print(pth)
# generator.draw_maze(nmap, pth)

# new_maze = Algorithms.maze_generator()
# boards.append(new_maze)
# new_maze.dfs(new_maze.s.x, new_maze.s.y)
# Maze.draw_maze(new_maze.grid, new_maze.Path)