import glob
import os.path
import tkinter as tk


# Sorts a dictionary in ascending order based on values


def sort_dict(dictionary: dict):
    output = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1])}
    return output


# Given a file name will return a name that does not conflict with an existing file

def safe_fname(fname):
    fname, fext = os.path.splitext(fname)
    tmp_name = fname + fext
    n = 1
    while does_it_exist(tmp_name):
        tmp_name = fname + "(" + str(n) + ")" + fext
        n += 1
    return tmp_name


def does_it_exist(name):
    return os.path.isdir(name) or os.path.isfile(name)


def extension(fname):
    return os.path.splitext(fname)[1]


def simple_popup(message="Error",
                 f1=lambda: True,
                 f2=lambda: True,
                 option1: str = "Yes",
                 option2: str = "No"):

    def func1():
        f1()
        popup.quit()


    def func2():
        f2()
        popup.quit()

    popup = tk.Tk()
    label = tk.Label(popup, text=message)
    button1 = tk.Button(popup, text=option1, command=func1)
    button2 = tk.Button(popup, text=option2, command=func2)

    for tmp in [label, button1, button2]:
        tmp.pack()

    popup.mainloop()


def simple_input(message="Input",
                 func1=lambda: True,
                 option1: str = "Ok"):
    popup = tk.Tk()
    popup.title(message)
