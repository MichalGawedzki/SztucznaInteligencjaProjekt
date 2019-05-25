import Maze
import Algorithms
from pprint import pprint

boards = []
boards.append(Maze.board1)

new_maze = Algorithms.maze_generator()
boards.append(new_maze)
new_maze.bfs(new_maze.s.x, new_maze.s.y)
Maze.draw_maze(new_maze.grid, new_maze.Path)