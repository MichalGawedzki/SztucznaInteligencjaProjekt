import generator
import Algorithms
from pprint import pprint

boards = []
boards.append(generator.board1)

new_maze = generator.maze_generator(18)
boards.append(new_maze)
#new_maze.d_dfs(new_maze.s.x, new_maze.s.y)
#a = new_maze.get_dfsLen()

for x in range(1000):
        new_maze = generator.prim_generator(18, 18)
        new_maze.d_dfs(new_maze.s.x, new_maze.s.y)
        a = new_maze.get_dfsLen()
        print("")
        print(new_maze.s.x, end=' ')
        print(new_maze.s.y)
        print(new_maze.f.x, end=' ')
        print(new_maze.f.y)
        if a <= -1:
                print("caught")
                print(new_maze.s.x, end=' ')
                print(new_maze.s.y)
                print(new_maze.f.x, end=' ')
                print(new_maze.f.y)
                break

generator.draw_maze(new_maze.GRID, new_maze.Path, new_maze.been)

# new_maze = generator.maze_generator()
# boards.append(new_maze)
# new_maze.dfs(new_maze.s.x, new_maze.s.y)
# Maze.draw_maze(new_maze.grid, new_maze.Path)
#print("halo")
#a = generator.prim_generator(18, 18)
#print("hejlo")
#a.bfs(a.s.x, a.s.y)
#print("main")
#generator.draw_maze(a.GRID, a.Path, a.been)
