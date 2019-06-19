import turtle
from functools import partial

import generator
import Algorithms
import tkinter as tk
import matplotlib.pyplot as plt

boards = []


class Window(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master


def generate(n, m):
    new_maze = generator.prim_generator(n, m)
    boards.append(new_maze)


def draw(maze):
    generator.draw_maze(maze.GRID, [], [])


def show_dfs(maze):
    maze.d_dfs(maze.s.x, maze.s.y)
    generator.draw_maze(maze.GRID, maze.Path, maze.been)


def show_bfs(maze):
    maze.bfs(maze.s.x, maze.s.y)
    generator.draw_maze(maze.GRID, maze.Path, maze.been)


def show_astar(maze):
    maze.astar(maze.GRID, (maze.s.x, maze.s.y), (maze.f.x, maze.f.y))
    generator.draw_maze(maze.GRID, maze.Path, maze.been)


# number - number of mazes you want to generate, n - breadth, m - height
def compare(number, n, m):

    # List contains informations about the best algorithm per iteration
    result = []
    count_astar = 0
    count_bfs = 0
    count_dfs = 0
    count_astar_dfs = 0

    labels = ["DFS", "BFS", "A*", "A* / DFS"]

    for y in range(number):
        maze = generator.prim_generator(n, m)
        maze.d_dfs(maze.s.x, maze.s.y)
        maze.bfs(maze.s.x, maze.s.y)
        maze.astar(maze.GRID, (maze.s.x, maze.s.y), (maze.f.x, maze.f.y))

        the_best = maze.dfsLen
        best_alg = "DFS"


        if maze.astarLen <= the_best:
            if maze.astarLen < the_best:
                the_best = maze.astarLen
                best_alg = "A*"
                count_astar += 1
            else:
                the_best = maze.astarLen
                best_alg = "A* / DFS"
                count_astar_dfs += 1
        if maze.bfsLen < the_best:
            the_best = maze.bfsLen
            best_alg = "BFS"
            count_bfs += 1

        else:
            count_dfs += 1

        result.append(best_alg)

    values = [count_dfs, count_bfs, count_astar, count_astar_dfs]

    plt.figure(figsize=(5, 5))
    plt.pie(values, labels=labels, autopct="%.1f%%")

    plt.show()


def close_turtle():
    window.bye()
    root.destroy()






# initiation of Tkinter
root = tk.Tk()
window = turtle.Screen()

# main window
app = Window(root)

#If you have a large number of widgets, like it looks like you will for your
#game you can specify the attributes for all widgets simply like this.
root.option_add("*Button.Background", "black")
root.option_add("*Button.Foreground", "red")

root.title('AI Project')
root.geometry("500x400")
root.resizable(0, 0)

back = tk.Frame(master=root,bg='black')
back.pack_propagate(0)
back.pack(fill=tk.BOTH, expand=1)


info = tk.Label(master=back, text='Choose:', bg='red', fg='black')
info.pack(padx=5, pady=5)

go = tk.Button(master=back, text='Generate maze', command=lambda: generate(18, 18))
go.pack(padx=5, pady=5)

go = tk.Button(master=back, text='Show generated maze', command=lambda: draw(boards[-1]))
go.pack(padx=5, pady=5)

go = tk.Button(master=back, text='Show DFS solution', command=lambda: show_dfs(boards[-1]))
go.pack(padx=5, pady=5)

go = tk.Button(master=back, text='SHOW BFS solution', command=lambda: show_bfs(boards[-1]))
go.pack(padx=5, pady=5)

go = tk.Button(master=back, text='Show A* solution', command=lambda: show_astar(boards[-1]))
go.pack(padx=5, pady=5)

go = tk.Button(master=back, text='Generate and compare 10 mazes and compare'
               , command=lambda: compare(10, 18, 18))
go.pack(padx=5, pady=5)

go = tk.Button(master=back, text='Generate and compare 100 mazes and compare'
               , command=lambda: compare(100, 18, 18))
go.pack(padx=5, pady=5)

go = tk.Button(master=back, text='Generate and compare 1000 mazes and compare'
               , command=lambda: compare(1000, 18, 18))
go.pack(padx=5, pady=5)


close = tk.Button(master=back, text='Quit', command=close_turtle)
close.pack(padx=5, pady=5)


root.mainloop()