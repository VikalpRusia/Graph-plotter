from tkinter import *

from Tkinter.view.ellipse import ellipse_creation
from Tkinter.view.parabola import parabola_creation

side_bar_width = 300
side_bar_height = 700
main_area_width = 698
button_width = 41
old_frame = None
lastCall = None


def frame_control(parent: Frame, current_call: str):
    global lastCall
    global old_frame
    if lastCall == current_call:
        return
    if old_frame is not None:
        old_frame.destroy()
    new_frame = Frame(parent, width=main_area_width, height=side_bar_height)
    new_frame.pack()
    old_frame = new_frame

    if current_call == 'parabola':
        lastCall = 'parabola'
        parabola_creation(new_frame)
    if current_call == 'ellipse':
        lastCall = 'ellipse'
        ellipse_creation(new_frame)


def home_view(top_level: Tk):
    parent = Frame(top_level)
    parent.pack()
    sidebar = Frame(parent, width=side_bar_width, bg='white', height=side_bar_height, relief='sunken', borderwidth=2)
    sidebar.pack(expand=False, fill='both', side='left', anchor=NW)

    # main content area
    main_area = Frame(parent, bg='#CCC', width=main_area_width, height=side_bar_height)
    main_area.pack(expand=True, fill='both', side='right')

    # Buttons in side bar
    switch_variable = StringVar(value="straight line")

    conic_section = Label(sidebar, text='Conic Section :', bg='white', width=button_width, anchor='w')
    conic_section.grid(row=0)
    straight_line = Radiobutton(sidebar, text='Straight Line', width=button_width, variable=switch_variable,
                                indicatoron=False, value="straight line")
    straight_line.grid(row=1)
    parabola = Radiobutton(sidebar, text='Parabola', width=button_width, variable=switch_variable,
                           indicatoron=False, value="parabola",
                           command=lambda: frame_control(main_area, 'parabola'))
    parabola.grid(row=2)
    ellipse = Radiobutton(sidebar, text='Ellipse', width=button_width,
                          variable=switch_variable,
                          indicatoron=False, value="ellipse",
                          command=lambda: frame_control(main_area, 'ellipse'))
    ellipse.grid(row=3)
    mixed = Radiobutton(sidebar, text='5 or more points plot', width=button_width, variable=switch_variable,
                        indicatoron=False, value="all conic")
    mixed.grid(row=4)

    sinusoidal_section = Label(sidebar, text='Sinusoidal Section :', bg='white', width=button_width, anchor='w')
    sinusoidal_section.grid(row=5)

    sin = Radiobutton(sidebar, text='Sin', width=button_width, variable=switch_variable,
                      indicatoron=False, value="sin")
    sin.grid(row=6)
    cos = Radiobutton(sidebar, text='Cos', width=button_width, variable=switch_variable,
                      indicatoron=False, value="cos")
    cos.grid(row=7)
    tan = Radiobutton(sidebar, text='Tan', width=button_width, variable=switch_variable,
                      indicatoron=False, value="tan")
    tan.grid(row=8)
    random = Label(sidebar, text='Equation :', bg='white', width=button_width, anchor='w')
    random.grid(row=9)
    all_mixed = Radiobutton(sidebar, text='Equation', width=button_width, variable=switch_variable,
                            indicatoron=False, value="equation")
    all_mixed.grid(row=10)
