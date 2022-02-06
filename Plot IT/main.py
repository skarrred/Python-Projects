
import imp
import tkinter as T
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import *
from constants import *


WIN = T.Tk()
WIN.geometry(WIN_SIZE)
WIN.title(WIN_TITLE)



def plot():
    figg = Figure(figsize=(10,10), dpi=100)
    the_plot = figg.add_subplot(111)
    the_plot.plot([12,23,45,56], [13,34,46,67])

    the_canvas = FigureCanvasTkAgg(figg, master=WIN)
    the_canvas.draw()
    the_canvas.get_tk_widget().pack()

    pass


plotit_btn = T.Button(master=WIN, command= plot, height=3, width=15, text="p_button")

plotit_btn.pack()


WIN.mainloop()