from tkinter import Frame, Label, Entry, Button
from tkinter.messagebox import showinfo

import numpy as np
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

main_area_width = 698
side_bar_height = 700
ln = None


def fig_creation():
    return Figure(figsize=(7, 5),  # 7,6.5
                  dpi=100)


fig = fig_creation()
plot1 = fig.add_subplot(111)
frame = None


def parabola_input(new_frame):
    bottomFrame = Frame(new_frame, width=main_area_width, height=100)
    equation_label = Label(bottomFrame, text='Equation: y = ax^2 + bx + c')
    equation_label.grid(row=0, columnspan=2)
    a_label = Label(bottomFrame, text='A value: ', pady=5)
    a_label.grid(row=1)
    a_value = Entry(bottomFrame)
    a_value.grid(row=1, column=1, padx=10)
    b_label = Label(bottomFrame, text='B value: ', pady=5)
    b_label.grid(row=2)
    b_value = Entry(bottomFrame)
    b_value.grid(row=2, column=1, padx=10)
    c_label = Label(bottomFrame, text='C value: ', pady=5)
    c_label.grid(row=3)
    c_value = Entry(bottomFrame)
    c_value.grid(row=3, column=1, padx=10)
    submit = Button(bottomFrame, text='display', pady=5, command=lambda: type_cast(a_value, b_value, c_value))
    submit.grid(row=4, columnspan=2)
    bottomFrame.grid(row=3, pady=10)


def parabola_creation(new_frame: Frame):
    global frame
    frame = new_frame
    draw(1, 1, 1)


def type_cast(a_value, b_value, c_value):
    if a_value is None or b_value is None or c_value is None:
        return
    try:
        draw(int(a_value.get()), int(b_value.get()), int(c_value.get()))
    except ValueError:
        showinfo('Error', 'Enter all value in integer format')


def draw(a, b, c):
    # print(a)
    # print(b)
    # print(c)
    global ln
    if ln is not None:
        ln.pop(0).remove()
    x = np.arange(-1000, 1000, 1)
    y = a * (x ** 2) + b * x + c
    plot1.set_title('$y_1 = {}x^2+{}x+{}$'.format(a, b, c))
    # plotting the graph
    ln = plot1.plot(x, y, color='black')
    canvas = FigureCanvasTkAgg(fig,
                               master=frame)
    canvas.draw()
    # placing the canvas on the Tkinter window
    toolbar = NavigationToolbar2Tk(canvas,
                                   frame, pack_toolbar=False)
    toolbar.grid(row=2, padx=10)

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().grid(row=0)
    parabola_input(frame)
