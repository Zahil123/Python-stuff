from tkinter import *

#Everything in tkinter is a widget. You define it and then put it on screen.

#Creates a root widget
root = Tk()

#Creating a Label widget
#myLabel = Label(root, text="Hello World!")

#Displaying it on the screen
#myLabel.pack()


myLabel1 = Label(root, text="Hello World!")#.grid(row=0, column=0)
myLabel2 = Label(root, text="Hi there!")#.grid(row=1, column=0)

# The grid system is a relative one.
# If we put col=5 in 2nd label, O/P remains the same.
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

#Event loop
root.mainloop()