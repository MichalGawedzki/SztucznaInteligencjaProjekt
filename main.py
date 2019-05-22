import Maze
import Algorithms
from pprint import pprint

boards = []
boards.append(Maze.board1)

#Algorithms.dfs(Algorithms.s[0], Algorithms.s[1])
#Maze.draw_maze(Maze.boards[0], Algorithms.Path)

#Algorithms.dfsRandom(Algorithms.s[0], Algorithms.s[1])
#Maze.draw_maze(Maze.boards[0], Algorithms.Path)

# Algorithms.dfs(Algorithms.s[0], Algorithms.s[1])
# Maze.draw_maze(Maze.boards[0], Algorithms.Path)
new_maze = []
new_maze = Algorithms.maze_generator()
print(new_maze)

# Algorithms.dfs(Algorithms.s[0], Algorithms.s[1])
Maze.draw_maze(new_maze, Algorithms.Path)
