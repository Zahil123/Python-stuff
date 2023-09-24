from tkinter import *

#Everything in tkinter is a widget. 
# Root is the main widget inside which all other widgets are displayed. 
root = Tk()

#To give the O/P window a title
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def botton_click(number): #number -> parameter
    current = e.get()
    e.delete(0,END)
    e.insert(0, current + str(number))

def botton_clear():
    e.delete(0,END)

def botton_add():
    first_number = e.get()
    global f_num
    global math
    f_num = (first_number)
    e.delete(0,END)

def botton_equal():
    second_number = e.get()
    second_number = int(second_number)
    e.delete(0,END)
    e.insert(0, f_num + second_number)
    
#Defining the buttons

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: botton_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: botton_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: botton_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: botton_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: botton_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: botton_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: botton_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: botton_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: botton_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: botton_click(0))
button_clear = Button(root, text="Clear", padx=80, pady=20, command=botton_clear)
button_add = Button(root, text="+", padx=39, pady=20, command=botton_add)
button_equal = Button(root, text="=", padx=81, pady=20, command=botton_equal)

#Displaying the buttons

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)


button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

root.mainloop()
