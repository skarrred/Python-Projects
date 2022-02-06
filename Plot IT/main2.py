from cProfile import label
import tkinter as T
from constants import *
from pygeom import Axes, Point, Line

xcor1 = int(input("Enter first X cordinate: "))
ycor1 = int(input("Enter first Y cordinate: "))
xcor2 = int(input("Enter second X cordinate: "))
ycor2 = int(input("Enter second Y cordinate: "))

# initialize window
WIN = T.Tk()
WIN.geometry(WIN_SIZE)
WIN.title(WIN_TITLE)

def do_plot():
    ax = Axes(xlim=(-100, 100), ylim=(-100, 100), figsize=(6, 6))
    p1 = Point(xcor1, ycor1, color='#ffa500')
    p2 = Point(xcor2, ycor2, color='#0000ff')
    l = Line(p1=p1, p2=p2)
    ax.addMany([p1, p2, l])
    ax.draw()


plotit_btn = T.Button(master=WIN, command= do_plot, height=3, width=15, text="Draw line")
plotit_btn.pack()


WIN.mainloop()