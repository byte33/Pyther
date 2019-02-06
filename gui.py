from tkinter import *
from tkinter import messagebox

options = ["Manual Entry (Encode)", "File Entry (Encode)", "Manual Entry (Decode)", "File Entry (Decode)"]


def callback():
    if messagebox.askokcancel("Quit", "Do you really wanna quit?"):
        root.destroy()


def type():
    direc = direction()
    shift = variable.get()
    return shift, direc


def direction():
    if var.get() == 1:
        return "left"
    else:
        return "right"


root = Tk()
root.geometry("800x600")
root.protocol("WM_DELETE_WINDOW", callback)

title = Label(root, text="byte33's cipher program", font=("Comic Sans MS", 30)).pack(pady=30)
version = Label(root, text="02/06/19 V0.6", font=("Comic Sans MS", 10)).place(relx=0.97,rely=0.97,anchor=E)


variable = StringVar(root)
variable.set(options[0])

var = IntVar()

optionBox = OptionMenu(root,variable,*options)
optionBox.pack(pady=25)

Label(root, text="Please enter message below:",font=("Comic Sans MS", 14)).pack(pady=10)

messageEntry = Entry(root,width=100)
messageEntry.pack(pady=10)

Label(root, text="Please indicate the amount you would like to shift (integer):",font=("Comic Sans MS", 14)).pack(pady=10)

numShift = Entry(root,width=5)
numShift.pack(pady=10)

leftDirection = Radiobutton(root, text="Shift Left", variable=var, value=1, command=direction).pack()
rightDirection = Radiobutton(root, text="Shift Right", variable=var, value=2, command=direction).pack()


button = Button(root, text="Submit", command=type)
button.pack(pady=25)

root.mainloop()

