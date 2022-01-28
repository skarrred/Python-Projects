
from tkinter import *

calculation = ""

#Funcitons
def add_to_calc(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calc():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation) 
    except:
        clear_field()
        text_result.insert(1.0, "Error Encountered")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

#instantiating the window
window = Tk()

#designing the window
window.geometry("638x500")
window.title("TKtutFT")
window.config(background="#8fffdd")


#result area declaration
text_result = Text(window,font=('Arial',50),fg='red',bg='black',height=2,width=17)
text_result.grid(columnspan=5)

#buttons
btn_1 = Button(window, text="1", command=lambda: add_to_calc(1), width=20, height=3, bg='#d9ffeb')
btn_1.grid(row=2, column=1, padx=5, pady=5)
btn_2 = Button(window, text="2", command=lambda: add_to_calc(2), width=20, height=3, bg='#d9ffeb')
btn_2.grid(row=2, column=2, padx=5, pady=5)
btn_3 = Button(window, text="3", command=lambda: add_to_calc(3), width=20, height=3, bg='#d9ffeb')
btn_3.grid(row=2, column=3, padx=5, pady=5)
btn_4 = Button(window, text="4", command=lambda: add_to_calc(4), width=20, height=3, bg='#d9ffeb')
btn_4.grid(row=3, column=1, padx=5, pady=5)
btn_5 = Button(window, text="5", command=lambda: add_to_calc(5), width=20, height=3, bg='#d9ffeb')
btn_5.grid(row=3, column=2, padx=5, pady=5)
btn_6 = Button(window, text="6", command=lambda: add_to_calc(6), width=20, height=3, bg='#d9ffeb')
btn_6.grid(row=3, column=3, padx=5, pady=5)
btn_7 = Button(window, text="7", command=lambda: add_to_calc(7), width=20, height=3, bg='#d9ffeb')
btn_7.grid(row=4, column=1, padx=5, pady=5)
btn_8 = Button(window, text="8", command=lambda: add_to_calc(8), width=20, height=3, bg='#d9ffeb')
btn_8.grid(row=4, column=2, padx=5, pady=5)
btn_9 = Button(window, text="9", command=lambda: add_to_calc(9), width=20, height=3, bg='#d9ffeb')
btn_9.grid(row=4, column=3, padx=5, pady=5)
btn_0 = Button(window, text="0", command=lambda: add_to_calc(0), width=20, height=3, bg='#d9ffeb')
btn_0.grid(row=5, column=2, padx=5, pady=5)
btn_open_paren = Button(window, text="(", command=lambda: add_to_calc("("), width=20, height=3, bg='#d9ffeb')
btn_open_paren.grid(row=5, column=1, padx=5, pady=5)
btn_close_paran = Button(window, text=")", command=lambda: add_to_calc(")"), width=20, height=3, bg='#d9ffeb')
btn_close_paran.grid(row=5, column=3, padx=5, pady=5)
btn_subtract = Button(window, text="-", command=lambda: add_to_calc("-"), width=20, height=3, bg='#d9ffeb')
btn_subtract.grid(row=2, column=4, padx=5, pady=5)
btn_add = Button(window, text="+", command=lambda: add_to_calc("+"), width=20, height=3, bg='#d9ffeb')
btn_add.grid(row=3, column=4, padx=5, pady=5)
btn_multiply = Button(window, text="*", command=lambda: add_to_calc("*"), width=20, height=3, bg='#d9ffeb')
btn_multiply.grid(row=4, column=4, padx=5, pady=5)
btn_divide = Button(window, text="/", command=lambda: add_to_calc("/"), width=20, height=3, bg='#d9ffeb')
btn_divide.grid(row=5, column=4, padx=5, pady=5)
btn_clear = Button(window, text="C", command=clear_field, width=20, height=3, bg='#d9ffeb')
btn_clear.grid(row=6, column=1, padx=5, pady=5)
btn_decimal = Button(window, text=".", command=lambda: add_to_calc("."), width=20, height=3, bg='#d9ffeb')
btn_decimal.grid(row=6, column=2, padx=5, pady=5)
btn_equal = Button(window, text="=", command=evaluate_calc, width=42, height=3, bg='#d9ffeb')
btn_equal.grid(row=6, column=3, columnspan=2, padx=5, pady=5)

# btn_ = Button(window, text="", command=None, width=20, height=3)
# btn_.grid(row=, column=)

window.mainloop() #Running the main loop