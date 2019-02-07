from Pyther import cipher
from tkinter import *
from tkinter import messagebox

print("Hello and welcome to byte33's cipher program")
print("02/06/19 V0.8\n")

options = ["Manual Entry (Encode)", "File Entry (Encode)", "Manual Entry (Decode)", "File Entry (Decode)"]


def callback():
    if messagebox.askokcancel("Don't leave me :c", "Do you really wanna go?"):
        root.destroy()


def types():
    direc = direction()
    shift = numShift.get()
    message = messageEntry.get()
    fileName = fileInput.get()

    if variable.get() == "Manual Entry (Encode)":
        whatToDo = 1
    elif variable.get() == "File Entry (Encode)":
        whatToDo = 2
    elif variable.get() == "Manual Entry (Decode)":
        whatToDo = 3
    elif variable.get() == "File Entry (Decode)":
        whatToDo = 4

    cipher.generateUppercase()
    cipher.generateLowercase()
    saveToFile(cipher.inputStuff(whatToDo, message, int(shift), direc, fileName))


def direction():
    if var.get() == 1:
        return "L"
    else:
        return "R"


def saveToFile(message1):
    i = messagebox.askyesno(title="Success!", message="Message has been successfully encoded/decoded. Store to file?")
    if i:
        try:
            stfName = "encodedmessage"
            stfFile = open(stfName + ".txt", "w")
            stfFile.write(message1)
            stfFile.close()
            messagebox.askokcancel("Success", "Write to file successful. Enjoy.")
        except:
            messagebox.showerror("ERROR", "There was an error writing to file, please try again.")

    else:
        messagebox.askokcancel("sneekybeeky", message1)


root = Tk()


root.geometry("800x600")
root.protocol("WM_DELETE_WINDOW", callback)

title = Label(root, text="byte33's cipher program", font=("Comic Sans MS", 30)).pack(pady=30)
version = Label(root, text="02/06/19 V0.8", font=("Comic Sans MS", 10)).place(relx=0.97, rely=0.97, anchor=E)

variable = StringVar(root)
variable.set(options[0])

var = IntVar()

optionBox = OptionMenu(root, variable, *options)
optionBox.pack(pady=25)

Label(root, text="If using file entry, enter full PATH below",
      font=("Comic Sans MS", 14)).pack(pady=10)

fileInput = Entry(root, width=75)
fileInput.pack(pady=10)

Label(root, text="Please enter message below:", font=("Comic Sans MS", 14)).pack(pady=10)

messageEntry = Entry(root, width=100)
messageEntry.pack(pady=10)

Label(root, text="Please indicate the amount you would like to shift (integer):", font=("Comic Sans MS", 14)).pack(
    pady=10)

numShift = Entry(root, width=5)
numShift.pack(pady=10)

leftDirection = Radiobutton(root, text="Shift Left", variable=var, value=1, command=direction).pack()
rightDirection = Radiobutton(root, text="Shift Right", variable=var, value=2, command=direction).pack()

button = Button(root, text="Submit", command=types)
button.pack(pady=25)

root.mainloop()
