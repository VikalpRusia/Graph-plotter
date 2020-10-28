# prefer MVC design for large model as it is small, designing roughly
from sys import exit
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import Combobox

from Tkinter.controller.Controller import register_request, login_request
from Tkinter.view.plotting_view import home_view


def frame_creation(parent):
    frame2 = Frame(parent, width=50, height=50)
    frame2.place(relx=.5, rely=.5, anchor="c")
    return frame2


def plotting_figures(parent, frame1):
    frame1.destroy()
    home_view(parent)
    # frame2 = frame_creation(parent)
    # Label(frame2, text='Successful').pack()


def display_username_password(parent):
    frame2 = frame_creation(parent)
    user_name_label = Label(frame2, text='User Name: ')
    user_name_label.grid(row=0, column=0)
    user_name = Entry(frame2)
    user_name.grid(row=0, column=1)
    password_label = Label(frame2, text='Password: ')
    password_label.grid(row=1, column=0, pady=10)
    password = Entry(frame2, show='*')
    password.grid(row=1, column=1, pady=10)

    user_name.focus_set()
    return frame2, user_name, password


def registration(parent, frame1: Frame):
    if frame1 is not None:
        frame1.destroy()

    def submit():
        if username.get() == '':
            showinfo("Error", "Name is needed!")
        elif not is_checked.get():
            showinfo('Error', 'Please give us consent before proceeding further!')
        else:  # database connectivity required
            is_commit, exception = register_request(username.get(), password.get(), student_class.get(), gender.get())
            if not is_commit:
                showinfo('Error', exception)

    parent.title('Registration Form')

    frame2, username, password = display_username_password(parent)

    # Class
    label_class = Label(frame2, text='Class: ')
    label_class.grid(row=2, column=0, pady=10)
    student_class = StringVar()
    class_chosen = Combobox(frame2, state="readonly", textvariable=student_class)
    class_chosen['values'] = ('CSE - A',
                              'CSE - B',
                              'IT - A',
                              'IT - B')
    class_chosen.current(1)
    class_chosen.grid(row=2, column=1, pady=10)

    # RadioButton
    label_gender = Label(frame2, text='Gender: ')
    label_gender.grid(row=3, column=0)
    gender = StringVar(value='Female')
    r1 = Radiobutton(frame2, text='Male', variable=gender, value='Male')
    r1.grid(row=4, column=0)
    r2 = Radiobutton(frame2, text='Female', variable=gender, value='Female')
    r2.grid(row=4, column=1)
    r3 = Radiobutton(frame2, text='Prefer not to choose', variable=gender, value='Unknown')
    r3.grid(row=4, column=2)

    # Privacy Policy
    is_checked = BooleanVar(value=FALSE)
    privacy_policy = Checkbutton(frame2, text='You give you consent to use your data as per our privacy policy',
                                 onvalue=TRUE, offvalue=FALSE, variable=is_checked)
    privacy_policy.grid(row=5, column=0, columnspan=20)

    # submit Button
    exit_button = Button(frame2, text="Exit", command=exit, fg='red')
    exit_button.grid(row=6, column=0, pady=10, columnspan=2)
    submit_button = Button(frame2, text="Submit", command=submit, fg='green')
    submit_button.grid(row=6, column=3, pady=10)
    already_registered_button = Button(frame2, text="Already Registered?", command=lambda: login(parent, frame2),
                                       fg='purple')
    already_registered_button.grid(row=7, column=1, pady=10, columnspan=5)


# still in progress
def login(parent: Tk, frame1):
    def submit():
        if username.get() == '':
            showinfo("Error", "Name is needed!")
        else:
            successful = login_request(username.get(), password.get())
            if successful:
                plotting_figures(parent, frame2)
            else:
                showinfo('Error', "Invalid Username or password :(")

    if frame1 is not None:
        frame1.destroy()

    frame2, username, password = display_username_password(parent)
    exit_button = Button(frame2, text="Exit", command=exit, fg='red')
    exit_button.grid(row=2, column=0, pady=10)
    submit_button = Button(frame2, text="Submit", command=submit, fg='green')
    submit_button.grid(row=2, column=1, pady=10)
    registration_button = Button(frame2, text="New User?", command=lambda: registration(parent, frame2), fg='purple')
    registration_button.grid(row=3, column=0, pady=10, columnspan=2)
