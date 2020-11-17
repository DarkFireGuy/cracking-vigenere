import matplotlib.pyplot as plt
import numpy as np
import string
import tkinter as tk
from tkinter import messagebox
from tools import *


def plot_alpha(fname: str,
               output: str = "output.png",
               sort: bool = False):
    alphabet = string.ascii_uppercase
    _plot(fname=fname, alphabet=alphabet, output=output, sort=sort)


def plot_alphanum(fname: str,
                  output: str = "output.png",
                  sort: bool = False):
    alphabet = string.digits + string.ascii_uppercase
    _plot(fname=fname, alphabet=alphabet, output=output, sort=sort)


def plot_printable(fname: str,
                   output: str = "output.png",
                   sort: bool = False,
                   figsize: tuple = (20, 9),
                   dpi: int = 600):
    alphabet = string.printable[:-5].replace(string.ascii_lowercase, '')
    _plot(fname=fname, alphabet=alphabet, output=output, sort=sort, figsize=figsize, dpi=dpi)


def freqs(alphabet: str, fname: str):
    frq = dict.fromkeys(list(alphabet), 0)
    with open(fname, "r") as file:
        for line in file:
            for char in line:
                char = char.upper()
                if char in frq:
                    frq[char] += 1
    return frq


def _plot(fname: str,
          alphabet: str,
          output: str = "output_img.png",
          sort: bool = False,
          figsize: tuple = (12, 9),
          dpi: int = 300):

    output, ext = os.path.splitext(output)
    root = tk.Tk()
    root.withdraw()
    while not ext and not messagebox.askyesno("Missing Extension", "Save with default extension [png]?"):
        ext = "." + str(input("Submit new extension: ")).lstrip(".")
    if not ext:
        ext = ".png"
    output = output + ext



    frq = freqs(alphabet, fname)

    if sort:
        frq = sort_dict(frq)

    keys, vals = frq.keys(), frq.values()

    # Makes the final graph larger
    plt.figure(figsize=figsize, dpi=dpi)

    # Creates all the bars
    plt.bar(keys, np.divide(list(vals), sum(vals)), label="File: " + fname)

    # Adds a label above each bar for the value of the bar
    for i in range(len(vals)):
        tmp = round(np.divide(list(vals), sum(vals))[i] * 100, 2)
        if tmp == 0:
            tmp = 0
        plt.annotate(str(tmp),
                     xy=(list(keys)[i], np.divide(list(vals), sum(vals))[i]), fontsize=12, horizontalalignment='center')

    # Set y-lim to the closest multiple of 0.05 lower than the max proportion
    ticks = [x / 100 for x in range(0, 100, 5)]
    ticks.append(max(vals) / sum(vals))
    ticks = sorted(ticks)

    plt.ylim(0, ticks[ticks.index(max(vals) / sum(vals)) + 1])
    plt.ylabel('Proportion')
    plt.xlabel('Character')
    plt.xticks(list(keys))
    plt.legend(bbox_to_anchor=(1, 1), loc="upper right", borderaxespad=0.)

    output = safe_fname(output)
    plt.savefig(output, bbox_inches='tight')

    root.mainloop()
