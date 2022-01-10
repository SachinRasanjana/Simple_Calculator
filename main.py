from tkinter import *

root = Tk()
root.title("Simple Calculator")

global g_number
g_number = 0
global method
method = 0

def click(number):
    current = input_field_01.get()
    input_field_01.delete(0, END)
    input_field_01.insert(0, str(current) + str(number))


def clear():
    input_field_01.delete(0, END)


def delete():
    current = (input_field_01.get())
    input_field_01.delete(0, END)
    input_field_01.insert(0, current[:-1])


def add():
    global g_number
    global method
    if input_field_01.get() == '':
        g_number=0
    else:
        g_number = int(input_field_01.get())
    method = 1
    input_field_01.delete(0, END)


def minus():
    global g_number
    global method

    if input_field_01.get() == '':
        g_number = 0
    else:
        g_number = int(input_field_01.get())

    method = 2
    input_field_01.delete(0, END)


def multiply():
    global g_number
    global method

    if input_field_01.get() == '':
        g_number = 0
    else:
        g_number = int(input_field_01.get())

    method = 3
    input_field_01.delete(0, END)


def divide():
    global g_number
    global method

    if input_field_01.get() == '':
        g_number = 0
    else:
        g_number = int(input_field_01.get())

    method = 4
    input_field_01.delete(0, END)


def result():
    print("result called")
    print(method)

    if (input_field_01.get()) == '':
        second_number = 0
    else:
        second_number = int(input_field_01.get())

    input_field_01.delete(0, END)

    if method == 1:
        input_field_01.insert(0, g_number + second_number)

    if method == 2:
        input_field_01.insert(0, g_number - second_number)

    if method == 3:
        input_field_01.insert(0, g_number * second_number)

    if method == 4:
        input_field_01.insert(0, g_number / second_number)

    if method == 0:
        print("default called")


input_field_01 = Entry(root, width=50, borderwidth=5)
input_field_01.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_0 = Button(root, text="0", padx=88, pady=20, command=lambda: click(0))
button_01 = Button(root, text="1", padx=40, pady=20, command=lambda: click(1))
button_02 = Button(root, text="2", padx=40, pady=20, command=lambda: click(2))
button_03 = Button(root, text="3", padx=40, pady=20, command=lambda: click(3))
button_04 = Button(root, text="4", padx=40, pady=20, command=lambda: click(4))
button_05 = Button(root, text="5", padx=40, pady=20, command=lambda: click(5))
button_06 = Button(root, text="6", padx=40, pady=20, command=lambda: click(6))
button_07 = Button(root, text="7", padx=40, pady=20, command=lambda: click(7))
button_08 = Button(root, text="8", padx=40, pady=20, command=lambda: click(8))
button_09 = Button(root, text="9", padx=40, pady=20, command=lambda: click(9))

button_plus = Button(root, text="+", padx=40, pady=52, command=add)
button_minus = Button(root, text="-", padx=40, pady=20, command=minus)
button_multiply = Button(root, text="x", padx=40, pady=20, command=multiply)
button_divide = Button(root, text="/", padx=40, pady=20, command=divide)
button_clear = Button(root, text="Clear", padx=30, pady=20, command=clear)
button_enter = Button(root, text="Enter", padx=30, pady=52, command=result)
button_delete = Button(root, text="Delete", padx=27, pady=20, command=delete)

button_0.grid(row=5, column=0, columnspan=2)
button_delete.grid(row=5, column=2)

button_01.grid(row=4, column=0)
button_02.grid(row=4, column=1)
button_03.grid(row=4, column=2)
button_enter.grid(row=4, column=3, rowspan=2)

button_04.grid(row=3, column=0)
button_05.grid(row=3, column=1)
button_06.grid(row=3, column=2)

button_07.grid(row=2, column=0)
button_08.grid(row=2, column=1)
button_09.grid(row=2, column=2)
button_plus.grid(row=2, column=3, rowspan=2)

button_clear.grid(row=1, column=0)
button_divide.grid(row=1, column=1)
button_multiply.grid(row=1, column=2)
button_minus.grid(row=1, column=3)

root.mainloop()
