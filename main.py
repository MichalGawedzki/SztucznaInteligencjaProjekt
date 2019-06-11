import generator
import Algorithms
from pprint import pprint
import numpy

boards = []
boards.append(generator.board1)

new_maze = generator.maze_generator(18)
boards.append(new_maze)
#new_maze.d_dfs(new_maze.s.x, new_maze.s.y)
#a = new_maze.get_dfsLen()

new_maze = generator.prim_generator(18, 18)


#new_maze = numpy.array(new_maze)


#new_maze.astar(new_maze.GRID, (new_maze.s.x, new_maze.s.y), (new_maze.f.x, new_maze.f.y))
new_maze.bfs(new_maze.s.x, new_maze.s.y)


generator.draw_maze(new_maze.GRID, new_maze.Path, new_maze.been)