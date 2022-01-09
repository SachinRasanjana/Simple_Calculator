from tkinter import *

root = Tk()
root.title("Simple Calculator")


def add():
    return


input_field_01 = Entry(root, width=50, borderwidth=5)
input_field_01.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_0 = Button(root, text="0", padx=88, pady=20, command=add)
button_01 = Button(root, text="1", padx=40, pady=20, command=add)
button_02 = Button(root, text="2", padx=40, pady=20, command=add)
button_03 = Button(root, text="3", padx=40, pady=20, command=add)
button_04 = Button(root, text="4", padx=40, pady=20, command=add)
button_05 = Button(root, text="5", padx=40, pady=20, command=add)
button_06 = Button(root, text="6", padx=40, pady=20, command=add)
button_07 = Button(root, text="7", padx=40, pady=20, command=add)
button_08 = Button(root, text="8", padx=40, pady=20, command=add)
button_09 = Button(root, text="9", padx=40, pady=20, command=add)

button_plus = Button(root, text="9", padx=40, pady=20, command=add)
button_minus = Button(root, text="9", padx=40, pady=20, command=add)
button_multiply = Button(root, text="9", padx=40, pady=20, command=add)
button_divide = Button(root, text="9", padx=40, pady=20, command=add)
button_clear = Button(root, text="9", padx=40, pady=20, command=add)
button_enter = Button(root, text="9", padx=40, pady=20, command=add)
button_equal = Button(root, text="=", padx=40, pady=20, command=add)

button_0.grid(row=4, column=0, columnspan=2)
button_equal.grid(row=4, column=2)

button_01.grid(row=3, column=0)
button_02.grid(row=3, column=1)
button_03.grid(row=3, column=2)

button_04.grid(row=2, column=0)
button_05.grid(row=2, column=1)
button_06.grid(row=2, column=2)

button_07.grid(row=1, column=0)
button_08.grid(row=1, column=1)
button_09.grid(row=1, column=2)



root.mainloop()
