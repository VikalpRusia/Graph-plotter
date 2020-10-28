from tkinter import Tk

from Tkinter.view.View import login
from Tkinter.view.plotting_view import home_view

root = Tk()
root.geometry('1000x700')
root.resizable(False, False)
login(root, None)
# home_view(root)
root.mainloop()
