from tkinter import *

root = Tk()

#For creating I/P fields
#Borderwidth defines the width (thickness) of border 
e = Entry(root, width=50, bg="black", fg="yellow", borderwidth=50)
e.pack() 
#e.insert(0, "Enter your name: ")   Commented because e.get() also displays "Enter your name:" along with the name 

'''def myClick():
    myLabel = Label(root, text="Button clicked!")
    myLabel.pack()'''

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

#Can use state state=disabled to stop the button from clicking.
#padx, pady can be used to change the X and Y dims of the button
#While calling funcs using command, no () are used
#fg and bg used to set fore/backgrd colour. Hex colour codes can also be used
#command used to give utility to buttons

myButton = Button(root, padx=50, pady=50, command=myClick, fg="green", bg="black", text="Enter your name")
myButton.pack()

root.mainloop()