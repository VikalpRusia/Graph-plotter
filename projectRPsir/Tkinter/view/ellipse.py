from tkinter import Frame, Label, Entry, Button
from tkinter.messagebox import showinfo

import matplotlib.pyplot as plt
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.patches import Ellipse

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
    equation_label = Label(bottomFrame, text='Equation: x^2/a^2 + y^2/b^2 = 1')
    equation_label.grid(row=0, columnspan=2)
    a_label = Label(bottomFrame, text='A value: ', pady=5)
    a_label.grid(row=1)
    a_value = Entry(bottomFrame)
    a_value.grid(row=1, column=1, padx=10)
    b_label = Label(bottomFrame, text='B value: ', pady=5)
    b_label.grid(row=2)
    b_value = Entry(bottomFrame)
    b_value.grid(row=2, column=1, padx=10)
    submit = Button(bottomFrame, text='display', pady=5, command=lambda: type_cast(a_value, b_value))
    submit.grid(row=4, columnspan=2)
    bottomFrame.grid(row=3, pady=10)


def ellipse_creation(new_frame: Frame):
    global frame
    frame = new_frame
    draw(1, 1)


def type_cast(a_value, b_value):
    if a_value is None or b_value is None:
        return
    try:
        draw(int(a_value.get()), int(b_value.get()))
    except ValueError:
        showinfo('Error', 'Enter all value in integer format')


def draw(a, b):
    plt.axes()

    ellipse = Ellipse(xy=(0, 0), width=1, height=2,
                      edgecolor='r', fc='None')
    plt.gca().add_patch(ellipse)

    plt.axis('scaled')
    plt.show()
    global ln
    if ln is not None:
        ln.pop(0).remove()
    plot1.set_title('$y_1 = x^2/{}^2+y^2{}^2 = 1$'.format(a, b))
    # plotting the graph
    ellipse = Ellipse(xy=(0, 0), width=a, height=b)
    # placing the canvas on the Tkinter window
    toolbar = NavigationToolbar2Tk(ellipse,
                                   frame, pack_toolbar=False)
    toolbar.grid(row=2, padx=10)

    # placing the toolbar on the Tkinter window
    parabola_input(frame)
