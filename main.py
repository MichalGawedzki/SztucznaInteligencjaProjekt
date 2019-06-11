import generator
import Algorithms
from pprint import pprint
import tkinter as tk


class Window(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master


new_maze = generator.prim_generator(18, 18)

# boards = []
# boards.append(generator.board1)

# new_maze = generator.maze_generator(18)
# boards.append(new_maze)

# for x in range(1000):
#         new_maze = generator.prim_generator(18, 18)
#         new_maze.d_dfs(new_maze.s.x, new_maze.s.y)
#         a = new_maze.get_dfsLen()
#
#
# generator.draw_maze(new_maze.GRID, new_maze.Path, new_maze.been)


# initiation of Tkinter
root = tk.Tk()

# main window
app = Window(root)

#If you have a large number of widgets, like it looks like you will for your
#game you can specify the attributes for all widgets simply like this.
root.option_add("*Button.Background", "black")
root.option_add("*Button.Foreground", "red")

root.title('AI Project')
root.geometry("500x500")
root.resizable(0, 0)

back = tk.Frame(master=root,bg='black')
back.pack_propagate(0)
back.pack(fill=tk.BOTH, expand=1)


close = tk.Button(master=back, text='Quit', command=root.destroy)
close.pack()

go = tk.Button(master=back, text='Show generated maze', command=lambda: generator.draw_maze(new_maze.GRID, [], []))
go.pack()

info = tk.Label(master=back, text='Made by me!', bg='red', fg='black')
info.pack()

root.mainloop()