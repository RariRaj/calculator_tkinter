from tkinter import *
from tkinter.messagebox import *

window = Tk()
window.title("calculator")
window.geometry("420x495")

# for picture label
pic = PhotoImage(file='img/calculator.png')
picLabel = Label(window, image=pic)
picLabel.pack(side=TOP)
# picLabel.grid(sticky="w", row=0, column=2)

# for heading label
headingLabel = Label(window, text="MY CALCULATOR", font=("Arial", 20, 'bold'))
headingLabel.pack(side=TOP)


# headingLabel .grid(row=0, column=2, columnspan=4)


# method for Delete
def delete():
    entryText.set(entryText.get()[:-1])


# method for clear all inputs
def clear():
    entryText.set("")


# method for adding inputs while button click
def add(text):
    oldtextvalue = entryText.get()
    if oldtextvalue == "Error":
        entryText.set(text)

    else:
        entryText.set(oldtextvalue + text)


# method for equal button
def calc():
    try:
        entryText.set(eval(entryText.get()))

    except:
        entryText.set("Error")
        showinfo("Error", "Please enter a valid operation")


# for Entry field(getting input from user and display result)
entryText = StringVar()
entry_field = Entry(window, relief=RIDGE, textvariable=entryText, justify='right', bd=26, bg='powder blue',
                    font=("Times", "24"))
# entry_field.grid(sticky="WE", row=2, column=2, columnspan=4)
entry_field.pack(side=TOP, ipadx=20)

# Place a frame to include all buttons
frame = Frame(window)
frame.pack(side=TOP)

# for Button widgets
btn7 = Button(frame, text="7", command=lambda: add("7"), bg='light blue', activebackground='orange', font="Times 18",
              width=6, height=2)

btn7.grid(row=3, column=2)

btn8 = Button(frame, text="8", command=lambda: add("8"), bg='light blue', activebackground='orange', font="Times 18",
              width=6,
              height=2)
btn8.grid(row=3, column=3)

btn9 = Button(frame, text="9", command=lambda: add("9"), bg='light blue', activebackground='orange', font="Times 18",
              width=6,
              height=2)
btn9.grid(row=3, column=4)

btn4 = Button(frame, text="4", command=lambda: add("4"), bg='light blue', activebackground='orange', font="Times 18",
              width=6,
              height=2)
btn4.grid(row=4, column=2)

btn5 = Button(frame, text="5", command=lambda: add("5"), bg='light blue', activebackground='orange', font="Times 18",
              width=6,
              height=2)
btn5.grid(row=4, column=3)

btn6 = Button(frame, text="6", command=lambda: add("6"), bg='light blue', activebackground='orange', font="Times 18",
              width=6,
              height=2)
btn6.grid(row=4, column=4)

btn1 = Button(frame, text="1", command=lambda: add("1"), bg='light blue', activebackground='orange', font="Times 18",
              width=6,
              height=2)
btn1.grid(row=5, column=2)

btn2 = Button(frame, text="2", command=lambda: add("2"), bg='light blue', activebackground='orange', font="Times 18",
              width=6,
              height=2)
btn2.grid(row=5, column=3)

btn3 = Button(frame, text="3", command=lambda: add("3"), bg='light blue', activebackground='orange', font="Times 18",
              width=6,
              height=2)
btn3.grid(row=5, column=4)

btn0 = Button(frame, text="0", command=lambda: add("0"), bg='light blue', activebackground='orange', font="Times 18",
              width=6,
              height=2)
btn0.grid(row=6, column=2)

btn_dot = Button(frame, text=".", command=lambda: add("."), bg='light blue', activebackground='orange',
                 font="Times 18", width=6,
                 height=2)
btn_dot.grid(row=6, column=3)

btn_del = Button(frame, text="DEL", command=delete, bg='light blue', activebackground='orange', font="Times 18",
                 width=6,
                 height=2)
btn_del.grid(row=6, column=4)

btn_div = Button(frame, text="/", command=lambda: add("/"), bg='light blue', activebackground='orange',
                 font="Times 18", width=6,
                 height=2)
btn_div.grid(row=3, column=5)

btn_mul = Button(frame, text="x", command=lambda: add("*"), bg='light blue', activebackground='orange',
                 font="Times 18", width=6,
                 height=2)
btn_mul.grid(row=4, column=5)

btn_sub = Button(frame, text="-", command=lambda: add("-"), bg='light blue', activebackground='orange',
                 font="Times 18", width=6,
                 height=2)
btn_sub.grid(row=5, column=5)

btn_add = Button(frame, text="+", command=lambda: add("+"), bg='light blue', activebackground='orange',
                 font="Times 18", width=6,
                 height=2)
btn_add.grid(row=6, column=5)

btn_clear = Button(frame, text="Clear", command=clear, bg='light blue', activebackground='orange', font="Times 18",
                   width=15,
                   height=2)
btn_clear.grid(row=7, column=2, columnspan=2)

btn_equal = Button(frame, text="=", command=calc, bg='light blue', activebackground='red', font="Times 18", width=15,
                   height=2)
btn_equal.grid(row=7, column=4, columnspan=2)

# code for Scientific Mode
# menu bar to show scientic mode
menubar = Menu(window)
mode = Menu(menubar,tearoff=0)
mode.add_checkbutton(label="Scientific Calculator")
menubar.add_cascade(label="Menu",menu=mode)
window.config(menu=menubar)

# create a frame for scientic mode buttons
sc_frame = Frame(window)
sc_frame.pack(side=TOP)

window.mainloop()
