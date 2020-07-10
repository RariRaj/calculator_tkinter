from tkinter import *

window = Tk()
window.title("calculator")
window.geometry("420x460")

# for picture label
pic = PhotoImage(file='img/calculator.png')
picLabel = Label(window, image=pic).grid(sticky="w", row=0, column=2)

# for heading label
headingLabel = Label(window, text="MY CALCULATOR", font=("Arial", 20, 'bold')).grid(row=0, column=2, columnspan=4)


# method for Delete
def delete():
    entryText.set(entryText.get()[:-1])


# method for clear all inputs
def clear():
    entryText.set("")


# method for adding inputs while button click
def add(text):
    oldtextValue = entryText.get()
    entryText.set(oldtextValue + text)


# for Entry field(getting input from user and display result) fg="white",
entryText = StringVar()
Entry(window, relief=RIDGE, textvariable=entryText, justify='right', bd=26, bg='powder blue',
      font=("Times", "24")).grid(sticky="WE", row=2, column=2, columnspan=4)

# for Button widgets
Button(window, text="7", command=lambda: add("7"), bg='light blue', activebackground='orange', font="Times 18", width=6,
       height=2).grid(row=3,
                      column=2)
Button(window, text="8", command=lambda: add("8"), bg='light blue', activebackground='orange', font="Times 18", width=6,
       height=2).grid(row=3,
                      column=3)
Button(window, text="9", command=lambda: add("9"), bg='light blue', activebackground='orange', font="Times 18", width=6, height=2).grid(row=3,
                                                                                                              column=4)

Button(window, text="4", command=lambda: add("4"), bg='light blue', activebackground='orange', font="Times 18", width=6, height=2).grid(row=4,
                                                                                                              column=2)
Button(window, text="5", command=lambda: add("5"), bg='light blue', activebackground='orange', font="Times 18", width=6, height=2).grid(row=4,
                                                                                                              column=3)
Button(window, text="6", command=lambda: add("6"), bg='light blue', activebackground='orange', font="Times 18", width=6, height=2).grid(row=4,
                                                                                                              column=4)

Button(window, text="1", command=lambda: add("1"), bg='light blue', activebackground='orange', font="Times 18", width=6, height=2).grid(row=5,
                                                                                                              column=2)
Button(window, text="2", command=lambda: add("2"), bg='light blue', activebackground='orange', font="Times 18", width=6, height=2).grid(row=5,
                                                                                                              column=3)
Button(window, text="3", command=lambda: add("3"), bg='light blue', activebackground='orange', font="Times 18", width=6, height=2).grid(row=5,
                                                                                                              column=4)

Button(window, text="0", command=lambda: add("0"), bg='light blue', activebackground='orange', font="Times 18", width=6, height=2).grid(row=6,
                                                                                                              column=2)
Button(window, text=".", command=lambda: add("."), bg='light blue', activebackground='orange', font="Times 18", width=6, height=2).grid(row=6,
                                                                                                              column=3)
Button(window, text="DEL", command=delete, bg='light blue', activebackground='orange', font="Times 18", width=6,
       height=2).grid(row=6, column=4)

Button(window, text="/", command=lambda: add("/"), bg='light blue', activebackground='orange', font="Times 18", width=6, height=2).grid(row=3,
                                                                                                              column=5)
Button(window, text="x", command=lambda: add("*"), bg='light blue', activebackground='orange', font="Times 18", width=6, height=2).grid(row=4,
                                                                                                              column=5)
Button(window, text="-", command=lambda: add("-"), bg='light blue', activebackground='orange', font="Times 18", width=6, height=2).grid(row=5,
                                                                                                              column=5)
Button(window, text="+", command=lambda: add("+"), bg='light blue', activebackground='orange', font="Times 18", width=6, height=2).grid(row=6,
                                                                                                              column=5)
Button(window, text="Clear", command=clear, bg='light blue', activebackground='orange', font="Times 18", width=15,
       height=2).grid(
    row=7, column=2, columnspan=2)
Button(window, text="=", bg='light blue', activebackground='red', font="Times 18", width=15, height=2).grid(row=7,
                                                                                                            column=4,
                                                                                                            columnspan=2)

window.mainloop()
