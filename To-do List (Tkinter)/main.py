
import tkinter
from tkinter import font
from tkinter.font import Font
from tkinter.constants import ANCHOR, BOTH, END, LEFT, NONE, RIGHT


root = tkinter.Tk()
root.title("Con-list application")
root.geometry("550x480")

#creating frame
the_frame = tkinter.Frame(root)
the_frame.pack(pady=10)

#font declaration
list_item_font = Font (
    family="courier new",
    size=20,

)

#creating listbox
the_list = tkinter.Listbox(the_frame,
    bg='black',
    bd=0,
    width=60,
    height=10,
    highlightthickness=0,
    selectbackground='green',
    activestyle='none',
    fg='white',
    font=list_item_font,
    selectforeground="yellow",
    
    )

the_list.pack(side=LEFT, fill=BOTH)

#adding random list items to the list
rand_stuff = ["calculus", "solid state drive", "bootstrap front-end", "tkinter framework", "Arithmetic mean calculator", "linkedin profile scraper", "whatsapp message automation script"]
for item in rand_stuff:
    the_list.insert(END, item)

#creating and adding scrollbar
the_scrollbar = tkinter.Scrollbar(the_frame)
the_scrollbar.pack(side=RIGHT, fill=BOTH)

the_list.config(yscrollcommand=the_scrollbar.set)
the_scrollbar.config(command=the_list.yview)

#Entry box
entry_box = tkinter.Entry(root)
entry_box.pack(pady=20)

#creating a button frame
buttons_frame = tkinter.Frame(root)
buttons_frame.pack(pady=20)

#functions
def del_item():
    the_list.delete(ANCHOR)

def add_item():
    if entry_box.get() != "":
        the_list.insert(END, entry_box.get())
    entry_box.delete(0, END)

def crossoff_item():
    the_list.itemconfig(
        the_list.curselection(),
        fg="#4d4d4d",
        selectforeground="#4d4d4d",
        selectbackground="#262626",
    )
    the_list.selection_clear(0, END)

def uncross_item():
    the_list.itemconfig(
        the_list.curselection(),
        fg="white",
        selectforeground="yellow",
        selectbackground="green",
    )
    the_list.selection_clear(0, END)

def delete_crossed_item():
    count = 0
    while count < the_list.size:
        if the_list.itemcget(count, "fg"):
            pass



#adding buttons in the button frame
del_button = tkinter.Button(buttons_frame, text="Delete selection", command=del_item)
add_button = tkinter.Button(buttons_frame, text="Add an item", command=add_item)
crossoff_button = tkinter.Button(buttons_frame, text="Cross off selection", command=crossoff_item)
uncross_button = tkinter.Button(buttons_frame, text="Uncross selection", command=uncross_item)


del_button.grid(row=0, column=2, padx=5)
add_button.grid(row=0, column=0, padx=5)
crossoff_button.grid(row=0, column=1, padx=5)
uncross_button.grid(row=0, column=3, padx=5)



root.mainloop()
